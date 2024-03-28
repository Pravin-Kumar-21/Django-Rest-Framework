from django.shortcuts import render
from django.http import JsonResponse
import json
from products import models as product_models


# Create your views here.
"""
So what we are trying to do in this function is that
is that we are creating an instance or object of the model
then we are creating a python dictionary then we are 
returning a Jsonresponse(data dictionary) to the client ...
"""


def api_home(request, *args, **kwargs):
    model_data = product_models.Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["Price"] = model_data.price
    return JsonResponse(data)
