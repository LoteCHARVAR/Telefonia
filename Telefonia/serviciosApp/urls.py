from django.contrib import admin
from django.urls import path
from serviciosApp.views import servicios
from serviciosApp.views import precios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', servicios),
    path('precios/', precios)
]
