from django.urls import path

from StoreProject.main.views import HomeView, ItemDetailsView, CartView, CheckoutView, ShopView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('details/', ItemDetailsView.as_view(), name='details'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop/', ShopView.as_view(), name='shop'),
)