from rest_framework import generics, mixins, authentication
from rest_framework import permissions as DjangoPermissions
from .models import Product
from .serializers import ProductSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404, request
from api.authentication import TokenAuthentication

# from api.permissions import IsStaffEditorPermission we can remove this and
from api.mixins import StaffEditorPermissionsMixin, UserQuerySetmixin

# from django.views.generic import


class ProductDetailAPIView(
    UserQuerySetmixin,
    generics.RetrieveAPIView,
    StaffEditorPermissionsMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # allow_staff_view = False
    lookup_feild = "pk"
    # we should try to to pass something like a pk integer that is read by the url and then
    # we can create urls with unique id followed by a /


# --------------------------------------------------------------------------------------------------------------------
class ProductListCreateAPIView(
    UserQuerySetmixin,
    generics.ListCreateAPIView,
    StaffEditorPermissionsMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # allow_staff_view = False
    # now we are moving to session and authentication

    def perform_create(self, serializer):
        # serialzer.save (user=self.request.user)
        print(serializer.validated_data)
        email = serializer.validated_data.pop("email")
        print(email)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        print("\n\n")
        print(serializer.data.get("content"))
        print("\n\n")

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        # print(dir(request))
        user = request.user
        print(request.user)
        if not user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user=user)


"""
You need to understand this very carefully that create an update work 
conjuctionally while updation create method also work ...
updation -> value Updated -> creation of new object
"""


class ProductListAPIView(
    UserQuerySetmixin,
    generics.ListAPIView,
    StaffEditorPermissionsMixin,
):
    """
    I am Not Gonna Use this Method
    instead i am going to create same API view of Create and list ^|^|^|^|
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # allow_staff_view = False


# -----------------------------------------------------------------------------------------------------------------
#  class Based view for Product Update Api View
class ProductUpdateAPIView(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_feild = "pk"

    """This function is created by me i have used the concept of validated_data that is given by the serializer
    and then i just grab the object using the filter command and then i just change the value and just saved it
    """

    def Perform_Update(self, serializer):
        instance = Product.objects.filter(self.lookup_feild)
        try:
            email = serializer.validated_data.get("email")
            if email is not None:
                instance.email = serializer.validated_data.get("email")
        except:
            raise ValueError
        if serializer.validated_data:
            instance.title = serializer.validated_data.get("title")
            instance.content = serializer.validated_data.get("content")
        instance.save()
        return Response(data=instance)

    """
    This is the function to perform update that is done by the documentation way

    "
        class ProductUpdateAPIView(generics.UpdateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializers
        lookup_feild = "pk"

        def Perform_Update(self, serializer):
            instance = serializer.save()
            if not instance.content:
                instance.content = instance.title
            return Response(data=instance)
    
    "


    """


"""
            This is a Function based View For Get and Post Requests
            this is how i have also done in my previous project for 
            Get and Post Requests , Similiarly we can Update Details of an 
            object by using the PUT method and also we can Destroy an object using the
            Destroy Method
"""
# ----------------------------------------------------------------------------------------------------------------


# Now we are going to create destroy method
class ProductDestroyAPIView(
    generics.DestroyAPIView,
    StaffEditorPermissionsMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def Perform_destroy(self, instance):
        # instance
        data = instance
        super().perform_destroy(instance)
        return Response(data)


# -------------------------------------------------------------------------------------------------
# Mixins and GenericAPI View
# Complete Crud Operation using ProductMixinView
class ProductMixinView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    StaffEditorPermissionsMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):  # http:// --> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        print(args, kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


#   def post(): http:// -->post

#  in the view it is request = self.request
#


# ---------------------------------------------------------------------------------------------------
# we can perform a complete crud operation using the logic method
# But good developer does not advises to use this type of method because of its hazy logic
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
