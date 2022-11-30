from django.urls import path
from django.http.response import HttpResponse
from . import views



app_name = 'superadmin'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('manage/users/',views.manage_users,name='users'),
    path('manage/inventory/',views.dashboard,name='inventory'),
    path('manage/orders/',views.dashboard,name='orders'),
    path('user/<str:pk>/',views.view_user_profile,name='view_user_profile'),
    path('cart/<str:id>/',views.fetch_cart,name='fetch_cart'),
]