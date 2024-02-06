from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView,)

app_name = 'listings_app'

urlpatterns = [
    path('auth/token', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', views.users_collection, name='users_collection'),
    path('users/<str:username>', views.user_detail, name='user_detail'),
    path('listings', views.listings_collection, name='listings_collection'),
    path('listings/<int:id>', views.listing_detail, name='listing_detail'),
    path('categories', views.categories_collection, name='categories_collection'),
    path('categories/<str:name>', views.category_detail, name='category_detail'),
    path('comments', views.comments_collection, name='comments_collection'),
    path('comments/<int:id>', views.comment_detail, name='comment_detail'),
    path('likes', views.likes_collection, name='likes_collection'),
    path('likes/<int:id>', views.like_detail, name='like_detail'),
]