from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def api_home(request, *args, **kwargs):
    return JsonResponse({"Message": "You are Currently working on Linux 23.10 Mantic "})
