from .models import Listing, User, Category, Comment, Like
from .serializers import ListingSerializer, TokenObtainPairSerializer, UserSerializer, LikeSerializer, CategorySerializer, CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import os


def validate_uploads(uploads, max_uploads, allowed_file_types, required=True):

    errors = []

    print(uploads)
    print(len(uploads))

    if required and len(uploads) == 0:
        return Response({'error': 'No file uploaded'},
                        status=status.HTTP_400_BAD_REQUEST)

    if len(uploads) > max_uploads:
        return Response({'error': f'Maximum of {max_uploads} images are allowed'},
                        status=status.HTTP_400_BAD_REQUEST)

    for upload in uploads:
        filename, file_extension = os.path.splitext(str(upload))
        try:
            if file_extension.lower() not in allowed_file_types:
                errors.append(
                    f'File type not allowed for extension: {file_extension}')

        except Exception as e:
            print(
                f'An unexpected error occurred for file: {filename}{file_extension}')
            errors.append(
                f'An unexpected error occurred for file: {filename}{file_extension}')

    if errors:
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

    return None


amount = 20
paginator = PageNumberPagination()
paginator.page_size = amount


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

# users


@api_view(['GET', 'POST'])
def users_collection(request):

    if request.method == 'GET':
        username = request.GET.get('username')
        if username:
            queryset = User.objects.filter(
                username__icontains=username).order_by('id')
        else:
            queryset = User.objects.all()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Invalid request method'},
                    status=status.HTTP_400_BAD_REQUEST)


# user
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_detail(request, username):
    try:
        queryset = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT' or request.method == 'DELETE':
        if not request.user.id == queryset.id:
            return Response({'message': 'Not authorised'},
                            status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = UserSerializer(queryset)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = UserSerializer(
            instance=queryset,
            data=request.data,
            partial=True,
            context={
                'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'User: {username} has been updated',
                            'listing': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queryset.delete_user()
        return Response(
            {'message': f'User: {username} has been deleted'}, status=status.HTTP_200_OK)

    return Response({'message': 'Invalid request method'},
                    status=status.HTTP_400_BAD_REQUEST)


# listing
# @permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET', 'DELETE', 'PUT'])
def listing_detail(request, id):
    try:
        queryset = Listing.objects.get(pk=id)
    except Listing.DoesNotExist:
        return Response({'message': 'Listing not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT' or request.method == 'DELETE':
        if not request.user.id == queryset.owner.id:
            return Response({'message': 'Not authorised'},
                            status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        try:
            serializer = ListingSerializer(queryset)
            user_serializer = UserSerializer(queryset.owner)
            return Response({
                'listing': serializer.data,
                'user': user_serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queryset.delete_listing()
        return Response(
            {'message': f'Listing: {id} has been deleted'}, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        images = request.data.getlist('images')
        remove_images = request.data.getlist('remove_images')
        files = request.data.getlist('files')
        remove_files = request.data.getlist('remove_files')

        serializer = ListingSerializer(
            queryset, data=request.data, context={
                'request': request})
        if serializer.is_valid():
            serializer.save(
                images=images,
                files=files,
                remove_images=remove_images,
                remove_files=remove_files)
            return Response({'message': f'Listing {id} has been updated',
                            'listing': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


# listings
@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET', 'POST'])
def listings_collection(request):
    if request.method == 'GET':
        search_param = request.GET.get('search')
        owner_param = request.GET.get('owner_id')
        category_param = request.GET.get('category_id')
        queryset = Listing.filter_listings(
            search_param=search_param,
            owner_param=owner_param,
            category_param=category_param).order_by('-created_at')
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = ListingSerializer(paginated_queryset, many=True)
        response_data = {
            'amount': amount,
            'listings': serializer.data,
        }
        response = paginator.get_paginated_response(response_data)

        return response
    elif request.method == 'POST':
        category_id = request.POST.get('category')
        category = Category.objects.get(pk=category_id)
        serializer = ListingSerializer(
            data=request.data, context={
                'request': request})

        images = request.data.getlist('images', [])
        files = request.data.getlist('files', [])

        validation_result_images = validate_uploads(
            images, max_uploads=10, allowed_file_types=[
                '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.eps'])

        if validation_result_images:
            return validation_result_images

        validation_result_files = validate_uploads(
            files, max_uploads=10, allowed_file_types=[
                '.txt', '.pdf'], required=False)

        if validation_result_files:
            return validation_result_files

        if serializer.is_valid():
            serializer.save(
                category=category,
                user=request.user,
                images=request.data.getlist('images'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'message': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({}, status.HTTP_400_BAD_REQUEST)


# comments
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comments_collection(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing')
    elif request.method == 'GET':
        listing_id = request.GET.get('listing')

    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        return Response({'message': 'Listing not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = CommentSerializer(
            data=request.data, context={
                'request': request})

        if serializer.is_valid():
            serializer.save(listing=listing, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        comments = Comment.objects.filter(listing_id=listing_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_detail(request, id):
    try:
        queryset = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        return Response({'message': 'Comment not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT' or request.method == 'DELETE':
        if not request.user.id == queryset.user.id:
            return Response({'message': 'Not authorised'},
                            status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = CommentSerializer(queryset)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(
            queryset, data=request.data, context={
                'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Comment: {id} has been updated',
                            'listing': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        queryset.delete()
        return Response(
            {'message': f'Comment: {id} has been deleted'}, status=status.HTTP_200_OK)


# category
@api_view(['GET'])
def category_detail(request, name):
    try:
        category_instance = Category.objects.get(name=name)
    except Category.DoesNotExist:
        return Response({'message': 'Category not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category_instance)
        return Response({
            'category': serializer.data,
        }, status=status.HTTP_200_OK)

    return Response({'message': 'Invalid request method'},
                    status=status.HTTP_400_BAD_REQUEST)


# categories
@api_view(['GET'])
def categories_collection(request):
    if request.method == 'GET':
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response({'categories': serializer.data},
                        status=status.HTTP_200_OK)

    return Response({}, status.HTTP_400_BAD_REQUEST)

# likes


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def likes_collection(request):

    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
    elif request.method == 'GET':
        listing_id = request.GET.get('listing_id')

    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        return Response({'message': 'Listing does not exist.'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        listing_id = request.GET.get('listing_id')
        user = request.user
        try:
            like = Like.objects.get(listing=listing_id, user=user)
        except Like.DoesNotExist:
            return Response({'message': 'Like does not exist.'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = LikeSerializer(like)
        user_likes_listing = Like.user_likes_listing(user, listing_id)
        return Response({'like': serializer.data,
                         'user_likes_listing': user_likes_listing},
                        status=status.HTTP_200_OK)
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        user = request.user
        existing_like = Like.objects.filter(
            user=user, listing=listing).exists()
        if existing_like:
            return Response({'message': 'User already likes listing.'},
                            status=status.HTTP_400_BAD_REQUEST)
        queryset = Like.create_like(user=user, listing=listing)
        serializer = LikeSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'categories': serializer.data}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def like_detail(request, id):
    try:
        like = Like.objects.get(id=id)
    except Like.DoesNotExist:
        return Response({'message': 'Like does not exist.'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        like.delete_listing()
        return Response(
            {'message': f'Like: {id} has been deleted'}, status=status.HTTP_200_OK)
