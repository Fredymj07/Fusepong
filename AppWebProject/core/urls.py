from django.urls import path
from . import views

app_name='core'
urlpatterns = [
    path('', views.index, name='index'),
    path('Clients/', views.ClientList, name = 'Clients'),
    path('AddClient/', views.AddClient, name = 'AddClient'),
]
