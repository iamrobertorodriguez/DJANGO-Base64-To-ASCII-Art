from rest_framework import routers
from product.views import ConversionViewSet

router = routers.SimpleRouter()
router.register(r'conversion', ConversionViewSet, basename='conversion')
product_patterns = router.urls