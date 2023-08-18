import coreschema as coreschema
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema, coreapi, AutoSchema
from rest_framework.viewsets import GenericViewSet
from .serializer import TaskSerializer
from .models import Task
from config.pagination import CustomPagination


class TaskAPIList(generics.ListCreateAPIView): # GET and POST requests
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomPagination

class TaskViewSet(mixins.CreateModelMixin, # viewsets.ModelViewSet
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet): # get, post , get<id>, put<id>, path<id>

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        if self.request.query_params == {}:
            queryset = Task.objects.all()
        else:
            overdue = self.request.query_params.get('overdue')
            author = self.request.query_params.get('author')
            queryset = Task.objects.filter(overdue=overdue, author=author).order_by('time_create')

        return queryset