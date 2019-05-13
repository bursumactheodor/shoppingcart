from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.adauga, name="adauga"),
    path('mod/<int:ids>', views.modifica, name="modifica"),
    path('del/<int:ids>', views.sterge, name="sterge"),



]



