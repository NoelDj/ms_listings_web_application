import { error,} from '@sveltejs/kit';
import { API_BASE_URL } from '$env/static/private';
import { isValid } from '../../../utils/auth';
import UserFetch from '../../../utils/userFetch';
import { jwtDecode } from 'jwt-decode';

/** @type {import('./$types').PageLoad} */
export async function load({ params, request, cookies }) {
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
  return {
    listing,
    isAuthenticated,
    comments,
    userId,
    isLiked,
    likeId
  }
}

export const actions = {
	postComment: async ({event, request, cookies}) => {
    const token = cookies.get('authToken')
    const formData = await request.formData()
    const useFetch = new UserFetch(`${API_BASE_URL}`, token)
    const response = await useFetch.postForm('comments', formData)
    const data = await response.json()
    
    const isAuthenticated = isValid(token)
    
	},
  deleteComment: async ({request, cookies}) => {
    const token = cookies.get('authToken')
    const formData = await request.formData()
    const commentId = formData.get('comment_id')
    const useFetch = new UserFetch(`${API_BASE_URL}`, token)
    const response = await useFetch.delete(`comments/${commentId}`)
    const data = await response.json()
  },
  likeListing: async ({request, cookies}) => {
    const token = cookies.get('authToken')
    const formData = await request.formData()
    const useFetch = new UserFetch(`${API_BASE_URL}`, token)
    const response = await useFetch.postForm('likes', formData)
    const data = await response.json()
  },
  deleteLike: async ({request, cookies}) => {
    const token = cookies.get('authToken')
    const formData = await request.formData()
    const likeId = formData.get('like_id')
    const useFetch = new UserFetch(`${API_BASE_URL}`, token)
    const response = await useFetch.delete(`likes/${likeId}`)
    const data = await response.json()
  },
}