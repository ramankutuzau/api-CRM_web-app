from django.urls import include, path

from rest_framework.routers import SimpleRouter
from .views import *


router_incoming = SimpleRouter()
router_incoming.register(r'Incoming', IncomingMailViewSet, basename='incoming')
router_outgoing = SimpleRouter()
router_outgoing.register(r'Outgoing', OutgoingMailViewSet, basename='outgoing')

urlpatterns = [
    path('', include(router_incoming.urls)),
    path('', include(router_outgoing.urls)),
]