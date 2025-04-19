from django.contrib import admin

from products.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "sale_price_display", "discount_display")

    def sale_price_display(self, obj):
        return obj.sale_price

    sale_price_display.short_description = "Sale Price"

    def discount_display(self, obj):
        return obj.get_discount()

    discount_display.short_description = "Discount"
