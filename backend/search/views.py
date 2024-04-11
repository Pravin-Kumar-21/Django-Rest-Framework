from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from product.serializers import ProductSerializers

# Create your views here.


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return super().get_queryset(*args, **kwargs)
