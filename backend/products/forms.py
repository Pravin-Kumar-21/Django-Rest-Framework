from django import forms
from . import models as Product_model


class ProductForm(forms.ModelForm):
    class Meta:
        models = Product_model.Product
        fields = [
            "title",
            "content",
            "price",
        ]
