from django.contrib import admin
from django.urls import path, include
import firstpractice.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',firstpractice.views.home, name = 'home'),
    path('firstpractice/',include('firstpractice.urls', namespace = 'firstpractice')),
]