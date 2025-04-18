from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        # 20% discount on the original price
        return "%.2f" % (float(self.price) * 0.8)

    @sale_price.setter
    def sale_price(self, value):
        # If someone sets sale_price, update the real price accordingly
        self.price = float(value) / 0.8

    def get_discount(self):
        # Returns 20% of the original price
        return "%.2f" % (float(self.price) * 0.2)
