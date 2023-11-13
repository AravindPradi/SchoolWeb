
from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.demo,name='demo'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('submit/',views.submit,name='submit'),
    path('success/',views.success,name='success')

]







