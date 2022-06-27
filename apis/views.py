from django.shortcuts import render
from rest_framework import generics

# Create your views here.

from shops.models import Shop
from .serializers import ShopSerializer

# Create your views here.


class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
