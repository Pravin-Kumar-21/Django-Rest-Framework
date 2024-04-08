from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializers
from . import views
from rest_framework import generics, mixins

"""
Now i will Show how routers interact with viewsets
we will now create the url using routers.py then 
from the  routers module of rest framework we will use 
default router to create url for list view of instances 
or detail view for the instances

"""


class productViewSet(
    viewsets.ModelViewSet,
):
    """

    get -> list -> queryset
    get -> retrieve -> lookup_feild ->  Product Instance Detail View
    post -> create -> New Instance
    Put -> Update
    delete -> destroy

    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"


class ProductGenericViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    """
    get-> list-> queryset

    get-> retrieve-> Product Instance Detail View
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"
