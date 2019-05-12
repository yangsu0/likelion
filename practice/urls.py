from django.contrib import admin
from django.urls import path, include
import firstpractice.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('firstpractice.urls', namespace = 'firstpractice')),
]