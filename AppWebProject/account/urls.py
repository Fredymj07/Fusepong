from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('UserRegister/', views.UserRegister, name='UserRegister'),
]