from django.urls import path, include
from django.urls import path, re_path, register_converter


from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('users/', include('users.urls', namespace="usres")),



]
