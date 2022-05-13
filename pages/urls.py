from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("contact", views.contact_view),
    path("client", views.user_view, name = 'client'),
    path("administrateur", views.admin_view, name = 'administrateur'),
    path("administrateur/list_livreurs", views.afficher_livreurs, name = 'afficher_livreurs'),
    path("administrateur/choisir_livreurs", views.choisir_livreur, name = 'choisir_livreurs'),
    path("administrateur/list_clients", views.afficher_clients, name = 'afficher_clients'),
    path("administrateur/pret_a_expedier", views.pret_a_expedier_admin_view, name = 'expedier_admin'),
    path("administrateur/selectionner", views.selectionner, name = 'selectionner'),
    path("admin_wilaya", views.admin_wilaya_view, name = 'admin_wilaya'),
    path("livreur", views.livreur_view, name = 'livreur'),
    path("client/hub", views.hub_view, name = 'hub'),
    path("client/ramassage", views.ramassage_view, name = 'ramassage'),
    path("client/transit", views.transit_view, name = 'transit'),
    path("client/livraison", views.livraison_view, name = 'livraison'),
    path("client/non_encaisse", views.non_encaisse_view, name = 'non_encaisse'),
    path("client/pret_a_expedier", views.pret_a_expedier_view, name = 'pret_a_expedier'),
    path("client/suspendus", views.suspendus_view, name = 'suspendus'),
]




