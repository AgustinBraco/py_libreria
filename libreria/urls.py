from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('apps.libros.urls')),
    path('autores/', include('apps.autores.urls')),
]