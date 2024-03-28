from django.shortcuts import render
from django.http import JsonResponse
import json


# Create your views here.
def api_home(request, *args, **kwargs):
    data = {}
    body = request.body  # byte string of json data
    # we are doing try and except so that if there is no json data provided we will simply pass
    try:
        data = json.loads(
            body
        )  # this line of code converts JSON data -> python dictionary
    except:
        pass
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    print("--------------------------------------------------------------------------")
    print(dict(request.GET))
    data["params"] = dict(request.GET)
    print("--------------------------------------------------------------------------")
    print(data)
    return JsonResponse({"Message": "You are Currently working on Linux 23.10 Mantic "})
