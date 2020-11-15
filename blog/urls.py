from django.urls import path

from . import views

#Urls inside app Article
urlpatterns = [
    path('', views.index, name = 'index'), #This for find index in views!
    path('auth/', views.auth) 
]