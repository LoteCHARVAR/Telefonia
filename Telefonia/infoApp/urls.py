from django.contrib import admin
from django.urls import path
from infoApp.views import informacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', informacion),
]
