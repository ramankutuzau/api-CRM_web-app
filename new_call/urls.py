from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
from django.urls import path,include

urlpatterns = [
    path('', OutgoingCallGenericAPIView.as_view()),
]
