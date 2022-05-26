from django.urls import path

from StoreProject.main.views import HomeView, ItemDetailsView, CartView, CheckoutView, ContactView, shop_view, \
    review_view, ReviewView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('details/', ItemDetailsView.as_view(), name='details'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('shop/', ShopView.as_view(), name='shop'),
    path('shop/', shop_view, name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('review/<int:pk>/', review_view, name='review'),
    path('review1/', ReviewView.as_view(), name='review1'),
)