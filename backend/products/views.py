from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    # we should try to to pass something like a pk integer that is read by the url and then
    # we can create urls with unique id followed by a /


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        # serialzer.save (user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = title
        serializer.save(content=content)
        print("\n\n")
        print(serializer.data.get("content"))
        print("\n\n")


class ProductListAPIView(generics.ListAPIView):
    """
    I am Not Gonna Use this Method
    instead i am going to create same API view of Create and list
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
