import { error,} from '@sveltejs/kit';
import { API_BASE_URL, BASE_URL } from '$env/static/private';
import { isValid } from '../../../utils/auth';
import UserFetch from '../../../utils/userFetch';
import { jwtDecode } from 'jwt-decode';
import { fail } from '@sveltejs/kit';


/** @type {import('./$types').PageLoad} */
export async function load({ params, cookies }) {
  const response = await fetch(`${API_BASE_URL}/listings/${params.id}`)
  const data = await response.json()
  
  const listing = data.listing
  
  if (!response.ok) {
    error(404, {
      message: 'Not found'
    });
  }

  const token = cookies.get('authToken') || '';
  const isAuthenticated = isValid(token);
  const userId = token ? jwtDecode(token)?.user_id || '' : '';
  let isLiked = false
  let likeId = ''

  if (isAuthenticated) {
    const useFetchGet = new UserFetch(API_BASE_URL, token)
    const getResponse = await useFetchGet.get(`likes?listing_id=${params.id}`)
    const dataIsliked = await getResponse.json()
    if (getResponse.ok) {
      isLiked = dataIsliked.user_likes_listing
      likeId = dataIsliked.like.id
    }
  }

  const responseComments = await fetch(`${API_BASE_URL}/comments?listing=${params.id}`)
  const dataComments = await responseComments.json()
  
  const comments = dataComments
  const baseImagePath = BASE_URL
  return {
    listing,
    isAuthenticated,
    comments,
    userId,
    isLiked,
    likeId,
    baseImagePath
  }
}

interface DataObject {
  [key: string]: { value?: string; missing?: boolean; incorrect?: boolean }
}

export const actions = {
	postComment: async ({request, cookies}) => {
    const token = cookies.get('authToken')
    const formData = await request.formData()
    const commentValue:string = formData.get('authToken')
    
    const useFetch = new UserFetch(`${API_BASE_URL}`, token)
    const response = await useFetch.postForm('comments', formData)
    const data = await response.json()
    
    const dataObject: DataObject = {
      comment: { value: commentValue || '' }
    }

    if (!response.ok) {
      if (data.message.text[0]) {
          dataObject.comment.missing = true
      }

      if (Object.values(dataObject).some(field => field.missing || field.incorrect)) {
          return fail(400, dataObject);
      }
  }
       
	},
  deleteComment: async ({request, cookies}) => {
    const token = cookies.get('authToken')
    const formData = await request.formData()
    const commentId = formData.get('comment_id')
    const useFetch = new UserFetch(`${API_BASE_URL}`, token)
    await useFetch.delete(`comments/${commentId}`)
    },
  likeListing: async ({request, cookies}) => {
    const token = cookies.get('authToken')
    const formData = await request.formData()
    const useFetch = new UserFetch(`${API_BASE_URL}`, token)
    await useFetch.postForm('likes', formData)
  },
  deleteLike: async ({request, cookies}) => {
    const token = cookies.get('authToken')
    const formData = await request.formData()
    const likeId = formData.get('like_id')
    const useFetch = new UserFetch(`${API_BASE_URL}`, token)
    await useFetch.delete(`likes/${likeId}`)
  },
}