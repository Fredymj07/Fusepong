from django.urls import path
from . import views

app_name='core'
urlpatterns = [
    path('', views.index, name='index'),
    path('ClientList/', views.ClientList, name = 'ClientList'),
    path('AddClient/', views.AddClient, name = 'AddClient'),
]
