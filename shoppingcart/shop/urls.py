from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('produse/', views.product_list, name="product-list"),
    path('produse/<int:idtip>', views.product_list_tip, name="product-list-tip"),
    path('produse/<str:num>', views.product_list_nume, name="product-list-nume"),
    path('produse/produs/<int:idp>', views.product_detalii, name="product-detalii"),
    path('produse/select/<int:idp>', views.product_select, name="product-select"),
    path('produse/select/del/<int:ids>', views.stergeselectie, name="sterge-selectie"),



]



