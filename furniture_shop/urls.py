from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from furniture_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)