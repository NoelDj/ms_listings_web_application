from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ListingSerializer
# Create your views here.


def index(request):
    return render(request, 'listings_app/index.html')


def listing_partial(request):
    listings = Listing.objects.all()
    return render(request, 'listings_app/listing_partial.html', context={'listings': listings})


def listing_details_partial(request, pk):
    listing = get_object_or_404(Listing, pk=pk)

    if request.method == 'GET':
        return render(request, 'listings_app/listing_details_partial.html', context={'l': listing})
    elif request.method == 'DELETE':
        listing.delete()

    elif request.method == 'PUT':
        listing.title = request.PUT[f'listing_{listing.pk}_title']
        listing.text = request.PUT[f'listing_{listing.pk}_text']
        listing.save()

    listings = Listing.objects.all()
    return render(request, 'listings_app/listing_partial.html', context={'listings': listings})


def create(request):
    Listing.create(title=request.POST['title'], text=request.POST['text'])
    response = render(request, 'listings_app/index.html', {})
    response['HX-Redirect'] = request.META['HTTP_HX_CURRENT_URL']
    return response


def rerank(request):
    reranked = [int(listing)
                for listing in request.POST.getlist('listing_order')]
    print(reranked)
    Listing.rerank_by_list(reranked)
    return HttpResponse(status=204)


class ListingListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDetailAPIView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
