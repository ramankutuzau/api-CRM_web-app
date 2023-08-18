from django.urls import path, include

from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet) # all routers


urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', TaskAPIList.as_view()),
]
