from django.contrib import admin
from django.urls import path
from menuApp.views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu),
]
