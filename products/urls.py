from django.urls import path
from .views import (
    product_create_view, 
    product_detail_view, 
    product_delete_view,
    product_update_view,
    product_list_view_client,  
    product_list_view_adminwilaya,
    valider_colis,
    product_list_view
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
    path('<int:id>/validate/', valider_colis, name='validate'),
]