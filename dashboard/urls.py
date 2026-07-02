from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/temperatura/', views.api_temperatura, name='api_temperatura'),
]