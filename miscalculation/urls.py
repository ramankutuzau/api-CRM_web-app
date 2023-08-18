from django.urls import path, include


from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'', MiscalculationViewSet) # all routers

router_offer = routers.SimpleRouter()
router_offer.register(r'', CommercialOfferViewSet) # all routers

urlpatterns = [
    path('add-hide-cost/', MiscalculationAddHideCostAPIView.as_view()),
    path('minus-hide-cost/', MiscalculationMinusHideCostAPIView.as_view()),
    path('', include(router.urls)),
    path('offer/', include(router_offer.urls)),
    path('offer/files/<str:file_name>/', FileView.as_view(), name='file-view'),

]
