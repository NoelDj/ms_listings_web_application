from django.urls import path
from . import views

app_name = 'listings_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('listing_partial', views.listing_partial, name='listing_partial'),
    path('listing_details_partial/<int:pk>/',
         views.listing_details_partial, name='listing_details_partial'),
    path('create', views.create, name='create'),
    path('rerank', views.rerank, name='rerank'),
    path('api/listings/', views.ListingListAPIView.as_view(), name='listing-api'),
    path('api/listings/<int:pk>/',
         views.ListingDetailAPIView.as_view(), name='listing-detail'),

]
