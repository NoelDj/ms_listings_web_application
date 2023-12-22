from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Listing, User
from rest_framework import generics, status
from .serializers import ListingSerializer, TokenObtainPairSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == "GET":
        context = f"Hello {request.user.username}"
        return Response({'response': context}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


def getRoute(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]

    return JsonResponse(routes, safe=False)


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
