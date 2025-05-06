from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('index/', views.index, name="index"),
    path('length/', views.length, name="length"),
    path('weight/', views.weight, name="weight"),
    path('temp/', views.temp, name="temp"),
    path('convert-l/', views.convert_L, name="convert_L"),
    path('convert-w/', views.convert_W, name="convert_W"),
    path('convert-t/', views.convert_T, name="convert_T"),
    path('length_out/', views.length_out, name="length_out"),
    path('weight_out/', views.weight_out, name="weight_out"),
    path('temp_out/', views.temp_out, name="temp_out"),
]
