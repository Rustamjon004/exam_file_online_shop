
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.product_list() ,name='product_list'),
]
