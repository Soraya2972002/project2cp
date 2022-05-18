from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("contact", views.contact_view),


    path("administrateur", views.admin_view, name = 'administrateur'),
    path("administrateur/list_livreurs", views.afficher_livreurs, name = 'afficher_livreurs'),
    path("administrateur/choisir_livreurs", views.choisir_livreur, name = 'choisir_livreurs'),
    path("administrateur/list_clients", views.afficher_clients, name = 'afficher_clients'),
    path("administrateur/transit", views.transit_admin_view, name = 'transit_admin'),
    path("administrateur/selectionner", views.selectionner_hub, name = 'selectionner_hub'),
    path("administrateur/selectionner_suspendus", views.selectionner_suspendus, name = 'selectionner_suspendus'),
    path("administrateur/selectionner_transit", views.selectionner_transit, name = 'selectionner_transit'),
    path("administrateur/historique", views.historique_admin_view, name = 'historique_admin'),
    path("administrateur/en_hub", views.en_hub_admin_view, name = 'en_hub_admin'),
    path("administrateur/en_livraison", views.en_livraison_admin_view, name = 'en_livraison_admin'),
    path("administrateur/en_ramassage", views.en_ramassage_admin_view, name = 'en_ramassage_admin'),
    path("administrateur/suspendus", views.suspendus_admin_view, name = 'suspendus_admin'),
    path("admin_wilaya", views.admin_wilaya_view, name = 'admin_wilaya'),
    path("retour_livreur_admin", views.retour_livreur_admin, name = 'retour_livreur_admin'),
    #path('administrateur/profile',views.profile_admin,name = 'admin_profile'),
    


    path("livreur", views.livreur_view, name = 'livreur'),
    path("livreur/a_recuperer", views.a_recuperer_livreur_view, name = 'a_recuperer_livreur'),
    path("livreur/en_livraison", views.en_livraison_livreur_view, name = 'en_livraison_livreur'),
    path("livreur/selectionner_ramassage", views.selectionner_livreur_ramassage, name = 'selectionner_livreur_ramassage'),
    path("livreur/selectionner_livraison", views.selectionner_livreur_livraison, name = 'selectionner_livreur_livraison'),
    path("livreur/historique", views.historique_livreur_view, name = 'historique_livreur'),
    path("livreur/non_payés", views.livreur_non_payés, name = 'livreur_non_payés'),
    #path('livreur/profile',views.profile_livreur,name = 'livreur_profile'),

    

    path("client", views.user_view, name = 'client'),
    path("client/hub", views.hub_view, name = 'hub'),
    path("client/ramassage", views.ramassage_view, name = 'ramassage'),
    path("client/transit", views.transit_view, name = 'transit'),
    path("client/livraison", views.livraison_view, name = 'livraison'),
    path("client/pret_a_expedier", views.pret_a_expedier_view, name = 'pret_a_expedier'),
    path("client/historique", views.historique_client_view, name = 'historique_client'),
    path("client/suspendus", views.suspendus_client_view, name = 'suspendus_client'),
    path("client/retour_livreur_client", views.retour_livreur_client, name = 'retour_livreur_client'),
    path("client/payes_client", views.payes_client, name = 'payes_client'),
    path("client/non_payes_client", views.non_payes_client, name = 'non_payes_client'),
    path("client/historique_payements_client", views.historique_payements_client, name = 'historique_payements_client'),
    #path('client/profile',views.profile_client,name = 'client_profile'),
]




