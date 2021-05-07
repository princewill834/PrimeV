from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    
]