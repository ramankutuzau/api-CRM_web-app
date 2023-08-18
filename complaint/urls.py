from django.urls import path, include

from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'', ComplaintViewSet) # all routers


urlpatterns = [
    path('', include(router.urls)),
]
