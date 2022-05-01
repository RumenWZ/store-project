from django.urls import path

from StoreProject.main.views import HomeView, ItemDetailsView, CartView, CheckoutView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('details/', ItemDetailsView.as_view(), name='details'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
)