from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
from django.urls import path,include

urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', register),
    # path('login', LoginView.as_view()),
    # path('logout', LogoutView.as_view()),
    path('user', AuthenticatedUser.as_view()),
    # path('permissions', PermissionAPIView.as_view()),
    # path('roles', RoleViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # path('roles/<str:pk>', RoleViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'delete'
    # })),
    path('users', UserGenericAPIView.as_view()),
    path('users/<str:pk>', UserGenericAPIView.as_view()),

    path('', home, name="home"), # django
    path("signup/", SignUp.as_view(), name="signup"),
]
