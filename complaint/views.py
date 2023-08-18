import coreschema as coreschema
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema, coreapi, AutoSchema
from rest_framework.viewsets import GenericViewSet
from .serializer import ComplaintSerializer
from .models import *

from config.pagination import CustomPagination


class ComplaintViewSet(mixins.CreateModelMixin,  # viewsets.ModelViewSet
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Complaint.objects.all()
        serializer = ComplaintSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Complaint.objects.all()
        mail = get_object_or_404(queryset, pk=pk)
        serializer = ComplaintSerializer(mail)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     complaint = Complaint.objects.get(id=instance.pk)
    #     complaint.author = request.data['author']
    #     complaint.executor = request.data['executor']
    #     complaint.content = request.data['content']
    #     complaint.status = request.data['status']
    #     complaint.time_create = request.data['time_create']
    #     complaint.time_update = request.data['time_update']
    #     complaint.time_deadline = request.data['time_deadline']
    #     complaint.overdue = request.data['overdue']
    #     complaint.is_active = request.data['is_active']
    #
    #     complaint.save()
    #
    #     serializer = ComplaintSerializer(complaint)
    #     return Response({"data": serializer.data})
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data})
