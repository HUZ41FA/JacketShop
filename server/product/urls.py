from django.urls import path
from .views import CategoryList, LastestProduct, ProductDetail


app_name = 'product'

urlpatterns = [
    path('latest-products/', LastestProduct.as_view(), name='latest_products'),
    path('product/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view(), name='product_detail'),
    path('product/<slug:category_slug>', CategoryList.as_view(), name="category_list"),
]