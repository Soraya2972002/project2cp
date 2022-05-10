from django.urls import path
from .views import (
    product_create_view, 
    product_detail_view, 
    product_delete_view,
    product_update_view,
    product_list_view_client,  
    product_list_view_adminwilaya,
    product_filter_hub,
    product_filter_ramassage,
    product_filter_transit,
    product_filter_expedier,
    product_filter_livraison,
    product_filter_suspendus,
    valider_colis
)

app_name = 'products'
urlpatterns = [
    path('hub', product_filter_hub, name='product-list'),
    path('ramassage', product_filter_ramassage, name='product-list'),
    path('transit', product_filter_transit, name='product-list'),
    path('livraison', product_filter_livraison, name='product-list'),
    path('expedier', product_filter_expedier, name='product-list'),
    path('suspendus', product_filter_suspendus, name='product-list'),
    path('client', product_list_view_client, name='product-list-client'),
    path('adminwilaya', product_list_view_adminwilaya, name='product-list-adminwilaya'),
    path('create/', product_create_view, name='product-create'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('<int:id>/validate/', valider_colis, name='validate'),
]