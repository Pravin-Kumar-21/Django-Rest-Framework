# One more thing is that we can as many serializers according to our need , and multiple serializers can be of the
# of the same model class and we can create it as per our needs
from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import unique_product_title, no_samsung_title
from rest_framework import generics, mixins, authentication

# from api.serializers import UserPublicSerializer

"""See now i have created a Product inline Serializer now i will jus have to create a new feild
    in the Product Serializer class that will display mmy all of my ProductInlineSerializer Class 
    Attribute now 
# """


# class ProductInlineSerializer(serializers.Serializer):
#     url = serializers.HyperlinkedIdentityField(
#         view_name="product-detail", lookup_field="pk", read_only=True
#     )
#     title = serializers.CharField(read_only=True)


class ProductSerializers(serializers.ModelSerializer):
    # owner = UserPublicSerializer(source="user", read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(source="user", read_only=True)
    # related_products = ProductInlineSerializer(
    #     source="product_set.all()", read_only=True, many=True
    # )
    """this is not working for a while we will see to it later |^|^|^"""
    # obj = Product.objects.all().order_by("?").first()
    url = serializers.HyperlinkedIdentityField(
        view_name="Product-detail", lookup_field="pk"
    )
    # # Suppose we want to send one email when a instance is created so you see how we are going to do it
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[unique_product_title, no_samsung_title]
    )  # this will do the same stuff as that of validating_title

    class Meta:
        model = Product
        fields = [
            # "owner",
            "user",
            "email",
            "url",
            "edit_url",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            # "discount",
            # "related_products",
        ]

    # def get_discount(self, obj):
    #     try:
    #         if discount:
    #             return obj.get_discount()
    #     except:
    #         pass

    def get_user(self, obj):
        return obj.user.username

    #  Now this function defination is
    def get_edit_url(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("Product-edit", kwargs={"pk": obj.pk}, request=request)

    def create(self, validated_data):
        obj = super().create(validated_data)
        return obj

    def update(self, instance, validated_data):
        email = validated_data.pop("email")
        instance.title = validated_data.get("title")
        return super().update(instance, validated_data)

    """"
    Now it will become very tedious if we use the validate each and 
    every atrribute of the seralizers and models.py so what we can do is 
    we can create validators.py file in the app so that whenever we want to validate
    some attribute we can just import the validator classess and then we can 
    just use these accordingly 
    

    """

    def validate_title(self, value):
        request = self.context.get("request")
        user = request.user
        query = Product.objects.filter(user=user, title__iexact=value)
        if query.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value
