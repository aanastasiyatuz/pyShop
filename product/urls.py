from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='product-list'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', CreateProductView.as_view(), name='create-product'),
    path('product/update/<int:product_id>/', ProductUpdateView.as_view(), name='update-product'),
    path('product/delete/<int:product_id>/', ProductDeleteView.as_view(), name='delete-product'),
    path('search', SearchListView.as_view(), name='search'),
]
