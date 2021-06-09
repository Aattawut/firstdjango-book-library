from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name='index'),
    path('detail<slug:slug>/', views.detail, name='detail'),
    re_path(r'add/$',views.book_add, name='book_add'),
    re_path(r'cart/add/(?P<slug>[\w-]+)/$', views.cart_add, name='cart_add'),
    re_path(r'cart/reduce/(?P<slug>[\w-]+)/$', views.cart_reduce, name='cart_reduce'),
    re_path(r'cart/delete/(?P<slug>[\w-]+)/$', views.cart_delete, name='cart_delete'),
    
    re_path(r'cart/list/$',views.cart_list, name='cart_list'),
]