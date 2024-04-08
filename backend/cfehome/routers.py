from rest_framework.routers import DefaultRouter
from products.viewsets import productViewSet, ProductGenericViewSet

router = DefaultRouter()
#  to register a router we use to register the app_name then we need to use the viewsets class and then give a basename
router.register("products", ProductGenericViewSet, basename="product")
urlpatterns = router.urls
