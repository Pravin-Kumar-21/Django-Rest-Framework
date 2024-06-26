from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products import models as product_models
from rest_framework.decorators import api_view
from rest_framework.response import responses, Response
from products.serializers import ProductSerializers

# Create your views here.
"""
So what we are trying to do in this function is that
is that we are creating an instance or object of the model
then we are creating a python dictionary then we are 
returning a Jsonresponse(data dictionary) to the client ...
"""


"""
Serializer and Views are the most critical
part of DjangoRestframework
"""


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # client = {}
    # try:
    #     client = json.loads(request.body)
    # except:
    #     pass
    # print(client)

    # """Django Rest Framework API View"""
    # instance = product_models.Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     # data["id"] = model_data.id
    #     # data["title"] = model_data.title
    #     # data["content"] = model_data.content
    #     # data["Price"] = model_data.price
    #     """
    #     instead of writing so much code we just need to use the model_to_method
    #     """
    #     data = ProductSerializers(
    #         instance
    #     ).data  # this will do the same work as we did manually by creating a dictionary
    serializer = ProductSerializers(data=request.data)  #
    if serializer.is_valid(raise_exception=True):
        print("\n")
        # in the beow line when we write serializer.save() we just make an instance of class Product
        print(
            serializer.save()
        )  # similar to instance= form.save() in django forms , only thiong we cannot do is (commit = false)
        print(serializer.data)
        print("\n")
        data = serializer.data
        return Response(data)
    # return Response({"invalid": "not good data"}, status=400) {if we want to treat the error according to our needs then we need declare  it like this}
