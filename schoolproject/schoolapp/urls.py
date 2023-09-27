from . import views
from django.urls import path

app_name = 'schoolapp'
urlpatterns = [

    path('', views.demo, name='demo'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('logout', views.logout, name='logout'),
    path('page', views.page, name='page'),




]
