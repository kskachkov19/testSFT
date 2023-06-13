from django.urls import path

from credit import views


urlpatterns = [
    path('contracts/', views.list_contracts_view, name='list_contracts'),
    path('contracts/<int:contract_id>/producers', views.list_producer_ids_by_contract_view,
         name='list_producer_ids_by_contract'),
]
