from django.urls import path

from StoreProject.products.views import AddProductView, EditProductView, ProductDetailsView, ProductDeleteView

urlpatterns = (
    path('add/', AddProductView.as_view(), name='product add'),
    path('edit/<int:pk>', EditProductView.as_view(), name='product edit'),
    path('details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product delete')
)