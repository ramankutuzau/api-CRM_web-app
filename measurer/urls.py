from django.urls import path, include
from rest_framework import routers

from .views import *





urlpatterns = [

    path('welcome-page/', welcome_page),
    path('', welcome_page),
    path('miscalculation/', miscalculation, name="miscalculation"),
    path('miscalculation-history/', miscalculation_history),
    path('miscalculation/<int:client>/<int:miscalc_pk>/<int:order_pk>/<slug:form>/', order, name='order'),
    path('miscalculation/<int:miscalc_pk>/<int:order_pk>/<slug:form>/', order, name='order'),
    # path('miscalculation/<int:client>/<int:pk>/', order_list, name='order_list'),
    path('miscalculation/<int:pk>/', order_list, name='order_list'),
    path('/accounts/', include('django.contrib.auth.urls')),
    path('calculation-form/', calculation_form, name='calculation-form'),
    path('add-cost-miscalculation/', add_cost_miscalculation, name='add_cost_miscalculation'),
    path('reset-hidden-cost-miscalculation/<int:pk>/', reset_hidden_cost_miscalculation, name='reset_hidden_cost_miscalculation'),
    path('miscalculation/<int:pk>/commercial_offer/', commercial_offer, name='commercial_offer'),
    path('miscalculation/<int:pk>/contract/', contract, name='contract'),
    path('miscalculation/<int:pk>/contract-offer/', contract_offer, name='contract_offer'),
    path('miscalculation/<int:pk>/send-to-manager/', send_to_manager, name='send_to_manager'),
    path('miscalculation/<int:pk>/confirm-order/', confirm_order, name='confirm_order'),
    path('miscalculation/<int:pk>/save-contract/<int:contract_pk>', save_contract, name='save_contract'),
    path('miscalculation/<int:pk>/save-passport/<int:passport_pk>', save_passport, name='save_passport'),

]
