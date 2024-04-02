from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # we should try to to pass something like a pk integer that is read by the url and then
    # we can create urls
