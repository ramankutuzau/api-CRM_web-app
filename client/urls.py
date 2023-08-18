from django.urls import path, include

from .views import *
from rest_framework import routers

router_number = routers.SimpleRouter()
router_number.register(r'number', NumberViewSet) # all routers

router_address = routers.SimpleRouter()
router_address.register(r'address', AddressViewSet) # all routers

router_prompter = routers.SimpleRouter()
router_prompter.register(r'prompter', PrompterViewSet) # all routers

router_client = routers.SimpleRouter()
router_client.register(r'', ClientViewSet) # all routers

router_contract = routers.SimpleRouter()
router_contract.register(r'contract', ContractViewSet) # all routers

router_passport = routers.SimpleRouter()
router_passport.register(r'passport', PassportDetailsViewSet) # all routers


urlpatterns = [

    path('', include(router_address.urls)),
    path('', include(router_number.urls)),
    path('', include(router_prompter.urls)),
    path('', include(router_contract.urls)),
    path('', include(router_passport.urls)),
    path('', include(router_client.urls)),


]
