from django.db import models
from django.conf import settings
from django.db.models import Q

# Create your models here.
User = settings.AUTH_USER_MODEL
"""
So now we are going to implement product search Functionality in Django Rest Framework
"""


class ProductQueryset(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQueryset(self.model, using=self.db)

    def search(self, query, user=None):
        return self.get_queryset.is_public.filter(lookup, user=user)


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    objects = ProductManager()

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"
