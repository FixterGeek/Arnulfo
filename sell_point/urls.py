from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, SaleOrderViewSet, OrderItemViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('saleorders', SaleOrderViewSet)
router.register('orderitems', OrderItemViewSet)

app_name='sell_point'

urlpatterns=[
	url('^', include(router.urls)),
	# url(r'^animalApi/$',AnimalAPI.as_view() )
]