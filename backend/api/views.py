from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products import models as product_models
from rest_framework.decorators import api_view
from rest_framework.response import responses, Response


# Create your views here.
"""
So what we are trying to do in this function is that
is that we are creating an instance or object of the model
then we are creating a python dictionary then we are 
returning a Jsonresponse(data dictionary) to the client ...
"""


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    client = {}
    try:
        client = json.loads(request.body)
    except:
        pass
    print("\n")
    print(client)
    print("\n")
    model_data = product_models.Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data["id"] = model_data.id
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["Price"] = model_data.price
        """
        instead of writing so much code we just need to use the model_to_method
        """
        data = model_to_dict(
            model_data, fields={"id", "title", "price"}
        )  # this will do the same work as we did manually by creating a dictionary
    return Response(data)
