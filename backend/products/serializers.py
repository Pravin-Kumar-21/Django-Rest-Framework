from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    # obj = Product.objects.all().order_by("?").first()

    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    def get_discount(self, obj):
        return obj.get_discount()


# One more thing is that we can as many serializers according to our need , and multiple serializers can be of the
# of the same model class and we can create it as per our needs
