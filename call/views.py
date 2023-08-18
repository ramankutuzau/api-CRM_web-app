from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .serializer import CallWindowSerializer
from config.pagination import CustomPagination
from .models import CallWindow
from .serializer import CallWindowSerializer
from rest_framework import generics, viewsets, mixins
from client.models import Client


class CallGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    queryset = CallWindow.objects.all().values().order_by('-datetime')
    serializer_class = CallWindowSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({'data': self.retrieve(request, pk).data})

        return self.list(request)


class CallAPIView(generics.ListAPIView):  # all requests get,put,patch ...
    queryset = CallWindow.objects.all()
    serializer_class = CallWindowSerializer

    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        w = CallWindow.objects.get(pk=pk)
        return Response({"data": CallWindowSerializer(w).data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PATCH not allowed'})

        try:
            instance = CallWindow.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = CallWindowSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})
