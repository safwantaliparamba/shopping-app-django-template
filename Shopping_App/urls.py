
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('', include('web.urls', namespace='web')),
    path('users/',include('users.urls', namespace='users')),
    path('cart/',include('cart.urls', namespace='cart')),
    path('products/',include('products.urls', namespace='products')),
    path('admin/',include('superadmin.urls', namespace='superadmin')),

]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
        static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
