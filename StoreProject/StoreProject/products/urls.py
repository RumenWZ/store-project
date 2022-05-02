from django.urls import path

from StoreProject.products.views import AddProductView, EditProductView

urlpatterns = (
    path('add/', AddProductView.as_view(), name='product add'),
    path('edit/<int:pk>', EditProductView.as_view(), name='product edit'),

)