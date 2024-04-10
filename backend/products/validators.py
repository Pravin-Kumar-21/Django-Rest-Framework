from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator


# def validate_title(value):
#     qs = Product.objects.filter(title__iexact=value)
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} already exists ")
#     return value

# let this be for some time


def no_samsung_title(value):
    query = "samsung"
    if query in value.lower():
        raise serializers.ValidationError(f"{query} not allowed")
    return value


"""
there are mutliple ways of creating serializer file ->

first -> we can declare it exactly in the model.py files only when we are creating the feilds

second -> we can create it inside the serializers.py file (inline)

third -> one we can create validators feild as external file as validators.py and then import them in 
the serializer file according to our needs

"""
#  the below line of code is similar to the function that i have created in the above file
unique_product_title = UniqueValidator(Product.objects.all(), lookup="iexact")
# the above line state that all the product that is being created irrespective of different user must hold a unique product
#  suppose if User1 has


# we can do custom validation purely upon our need just like in the above section i
# created a custom validators that will no accept any title with the name of samsung.
