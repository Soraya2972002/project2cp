from django.urls import path
from .views import (
    product_create_view, 
    product_detail_view, 
    product_delete_view,
    product_update_view,
    product_list_view_client,  
    product_list_view_adminwilaya,
    valider_colis_pret_a_expedier,
    product_list_view,
    colis_non_payé,
    colis_payé,
    retour_chez_livreur,
    retour_hub,
    retour_suspendre,
    all_suspendre,
    non_payés
)

app_name = 'products'
urlpatterns = [
    path('client', product_list_view_client, name='product-list-client'),
    path('adminwilaya', product_list_view_adminwilaya, name='product-list-adminwilaya'),
    path('create/', product_create_view, name='product-create'),
    path('list', product_list_view, name='product_list'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('<int:id>/validate_expedier/', valider_colis_pret_a_expedier, name='validate_expedier'),
    path('<int:id>/payé/', colis_payé, name='colis_payé'),
    path('<int:id>/non_payé/', colis_non_payé, name='colis_non_payé'),
    path('<int:id>/non_payés/', non_payés, name='non_payés'),
    path('<int:id>/retour_livreur/', retour_chez_livreur, name='retour_chez_livreur'),
    path('<int:id>/retour_hub/', retour_hub, name='retour_hub'),
    path('<int:id>/retour_suspendre/', retour_suspendre, name='retour_suspendre'),
    path('<int:id>/all_suspendre/', all_suspendre, name='all_suspendre'),
]