from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404


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


"""
            This is a Function based View For Get and Post Requests
            this is how i have also done in my previous project for 
            Get and Post Requests 
"""


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    # so you see get method can be of more than type either it is List View or DetailView
    if method == "GET":
        if (
            pk is not None
        ):  # See this {{if condition}} == True then itself says that it is a detail view request
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializers(obj, many=False).data
            return Response(data)
        """
        url args ??
        get request -> detail view
        list view
        """
        queryset = Product.objects.all()
        data = ProductSerializers(queryset, many=True).data
        return Response(data)
    if method == "POST":
        """
        create an item
        """
        serialzier = ProductSerializers(data=request.data)
        if serialzier.is_valid(raise_exception=True):
            title = serialzier.validated_data.get("title")
            content = serialzier.validated_data.get("content")
            if content is None:
                content = title
            serialzier.save(content=content)
            return Response(serialzier.data)
        return Response({"invalid": "Please provide Valid data"})
