from django.urls import path

from .views import ShopDetail, ShopList

urlpatterns = [
    path("<int:pk>/", ShopDetail.as_view(), name="shop_detail"),
    path("", ShopList.as_view(), name="shop_list"),
]
