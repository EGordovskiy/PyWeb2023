from django.urls import path
from rest_framework import routers
from .views import ProductView, CartView, ShopView, CartViewSet

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

app_name = 'store'


urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
]
