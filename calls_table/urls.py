from django.urls import path, include

from .views import *

from rest_framework import routers



urlpatterns = [
    path('', CallsTableGenericAPIView.as_view()),
    path('parse-all-calls', ParseCallsTableGenericAPIView.as_view()),
]
