from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('<str:pk>/',views.single_product,name='single_product'),
]