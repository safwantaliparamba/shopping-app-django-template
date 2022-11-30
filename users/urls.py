from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('order/<str:id>/',views.order_item,name='order_item'),
    
    path('<str:pk>/',views.profile,name='profile'),
    path('<str:pk>/orders/',views.orders,name='orders'),
]