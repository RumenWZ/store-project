from django.urls import path

from StoreProject.products.views import AddProductView

urlpatterns = (
    path('add/', AddProductView.as_view(), name='product add'),

)