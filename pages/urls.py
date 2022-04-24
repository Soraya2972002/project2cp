from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("contact", views.contact_view),
    path("client", views.user_view, name = 'client'),
    path("administrateur", views.admin_view, name = 'administrateur'),
    path("admin_wilaya", views.admin_wilaya_view, name = 'admin_wilaya'),
    path("livreur", views.livreur_view, name = 'livreur'),
]
