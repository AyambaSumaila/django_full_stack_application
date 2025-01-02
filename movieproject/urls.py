
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static 
from django.conf import settings

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeapp.urls')),
    path('movies/', include('movieapp.urls')),
    path('accountsapp/', include('accountsapp.urls')),
    path('cart/', include('cart.urls')),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

