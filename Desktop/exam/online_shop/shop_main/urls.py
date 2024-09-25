from django.urls import path
from .views import home_page,detail_view

urlpatterns = [
    path('', home_page, name='home'),
    path('detail/<int:_id>/', detail_view, name='detail'),


]
