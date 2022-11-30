from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [

    path('',views.view_cart,name='view_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkout-confirm/',views.checkout_confirm,name='checkout_confirm'),
    path('<str:id>/cancel/',views.cancel_order,name='cancel_order'),
    path('<str:pro_id>/add/',views.add_to_cart,name='add_to_cart'),
    path('<str:pro_id>/remove/',views.remove_from_cart,name='remove_from_cart'),
]