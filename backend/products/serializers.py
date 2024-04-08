from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse


class ProductSerializers(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    # obj = Product.objects.all().order_by("?").first()
    url = serializers.HyperlinkedIdentityField(
        view_name="Product-detail", lookup_field="pk"
    )

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    def get_discount(self, obj):
        try:
            if discount:
                return obj.get_discount()
        except:
            pass

    #  Now this function defination is
    def get_edit_url(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("Product-edit", kwargs={"pk": obj.pk}, request=request)


# One more thing is that we can as many serializers according to our need , and multiple serializers can be of the
# of the same model class and we can create it as per our needs
