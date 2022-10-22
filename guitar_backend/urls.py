
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, re_path, include
from apps.guitar_server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.guitar_server.urls')),
]