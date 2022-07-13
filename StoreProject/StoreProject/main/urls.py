from django.urls import path

from StoreProject.main.views import ItemDetailsView, ContactView, shop_view, \
    review_view, cart_view, CartDeleteView, updateCart, home_view, cart_add_quantity, cart_remove_quantity, \
    cart_remove_item, checkout_view, thank_you_for_shopping_view, my_purchases_view

urlpatterns = (
    path('', home_view, name='index'),
    path('details/', ItemDetailsView.as_view(), name='details'),
    path('checkout/', checkout_view, name='checkout'),
    path('shop/', shop_view, name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('review/<int:pk>/', review_view, name='review'),
    path('delete/<int:pk>', CartDeleteView.as_view(), name='cart delete'),
    path('delete_cart/', updateCart, name='delete cart item'),
    path('purchases/', my_purchases_view, name='my purchases'),
    path('thank_you_for_shopping/', thank_you_for_shopping_view, name='thank you for shopping'),

    path('cart/', cart_view, name='cart'),
    path('cart/quantity/add/<int:pk>/', cart_add_quantity, name='cart add quantity'),
    path('cart/quantity/remove/<int:pk>/', cart_remove_quantity, name='cart remove quantity'),
    path('cart/remove/<int:pk>/', cart_remove_item, name='cart remove item'),

    # path('error_403', )

)