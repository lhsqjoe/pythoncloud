from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_login, name='show_login'),
    path('login', views.login, name='login'),
    
]
