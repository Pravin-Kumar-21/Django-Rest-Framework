from django.contrib import admin

from . import models as Productmodels

# Register your models here.
admin.site.register(Productmodels.Product)
