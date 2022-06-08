from django.urls import path

from StoreProject.main.views import ItemDetailsView, CheckoutView, ContactView, shop_view, \
    review_view, ReviewView, cart_view, CartDeleteView, updateCart, home_view

urlpatterns = (
    path('', home_view, name='index'),
    path('details/', ItemDetailsView.as_view(), name='details'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop/', shop_view, name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('review/<int:pk>/', review_view, name='review'),
    path('review1/', ReviewView.as_view(), name='review1'),
    path('delete/<int:pk>', CartDeleteView.as_view(), name='cart delete'),
    path('delete_cart/', updateCart, name='delete cart item'),

)