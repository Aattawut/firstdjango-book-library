from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    # path('signin/', views.signin2, name='signin'),
    #ส่ง พารามิเตอร์ผ่าน url ไปยัง views
    path('hello/<int:id>', views.hello, name='hello'),
    re_path(r'article/$', views.article),

    #ส่ง พารามิเตอร์เเบบ regular expression
    re_path(r'article/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$', views.article, name='article'),


]