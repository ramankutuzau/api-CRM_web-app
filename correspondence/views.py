from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from .models import *
from .serializer import *
from config.pagination import CustomPagination
from rest_framework.response import Response


class IncomingMailViewSet(viewsets.ModelViewSet):
    queryset = IncomingMail.objects.all()
    serializer_class = IncomingMailSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = IncomingMail.objects.all()
        serializer = IncomingMailSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = IncomingMail.objects.all()
        mail = get_object_or_404(queryset, pk=pk)
        serializer = IncomingMailSerializer(mail)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class OutgoingMailViewSet(viewsets.ModelViewSet):
    queryset = OutgoingMail.objects.all()
    serializer_class = OutgoingMailSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = OutgoingMail.objects.all()
        serializer = OutgoingMailSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = OutgoingMail.objects.all()
        mail = get_object_or_404(queryset, pk=pk)
        serializer = OutgoingMailSerializer(mail)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})
