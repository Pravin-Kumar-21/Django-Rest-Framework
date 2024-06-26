from django.urls import path
from . import views
from . import viewsets

"""
we can also use viewsets to make get -> list view 
get -> detail view  by using the given method now 

or the other thing we can do is we can create a variable that is in the viewsets.py file and 
then we can import that viewset file into the urls. py file 

let say

retrive_instance = ProductGenericViewSet.as_view({"get": "retrieve"})
list_instance = ProductGenericViewSet.as_view({"get": "list"})

"""

urlpatterns = [
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="Product-detail"),
    path("", views.ProductListCreateAPIView.as_view(), name="Product-list"),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view(), name="Product-edit"),
    path("<int:pk>/delete/", views.ProductDestroyAPIView.as_view()),
]
"""

# path(
#     "<int:pk>/",
#     viewsets.ProductGenericViewSet.as_view({"get": "retrieve"}),
# ),
# path(
#     "",
#     viewsets.ProductGenericViewSet.as_view({"get": "list"}),
# )

We declare this when we are using the viewsets file to create urls for the products and all
"""
