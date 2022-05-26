from django.urls import path

from StoreProject.products.views import AddProductView, EditProductView, ProductDeleteView, product_details

urlpatterns = (
    path('add/', AddProductView.as_view(), name='product add'),
    path('edit/<int:pk>', EditProductView.as_view(), name='product edit'),
    path('details/<int:pk>', product_details, name='product details'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product delete')
)