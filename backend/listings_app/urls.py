from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenRefreshView,)

app_name = 'listings_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('listing_partial', views.listing_partial, name='listing_partial'),
    path('listing_details_partial/<int:pk>/',
         views.listing_details_partial, name='listing_details_partial'),
    path('create', views.create, name='create'),
    path('rerank', views.rerank, name='rerank'),
    path('api/listings/', views.ListingListAPIView.as_view(), name='listing-api'),
    path('api/listings/<int:pk>/',
         views.ListingDetailAPIView.as_view(), name='listing-detail'),

]
