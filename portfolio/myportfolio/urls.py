from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('projects/', views.about, name="projects"),
    path('stats/', views.about, name="stats"),
    path('contact/', views.about, name="contact"),
]