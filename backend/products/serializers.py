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
    # Suppose we want to send one email when a instance is created so you see how we are going to do it
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "email",
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

    def create(self, validated_data):
        obj = super().create(validated_data)
        return obj

    def update(self, instance, validated_data):
        email = validated_data.pop("email")
        instance.title = validated_data.get("title")
        return super().update(instance, validated_data)


# One more thing is that we can as many serializers according to our need , and multiple serializers can be of the
# of the same model class and we can create it as per our needs
