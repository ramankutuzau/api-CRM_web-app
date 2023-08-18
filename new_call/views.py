from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import *
# Create your views here.
from rest_framework import generics, viewsets, mixins

from .serializers import OutGoingCallSerializer
import requests



class OutgoingCallGenericAPIView(generics.GenericAPIView, mixins.CreateModelMixin):

    queryset = OutgoingCalls.objects.all()
    serializer_class = OutGoingCallSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = request.data['phone'].replace('+375', '80')
        num_phone = request.data['number']
        success_message = "Successfully sent the request."
        error_message = "Error occurred while sending the request."
        url = None
        if num_phone == 14:
            url = f'http://admin:reMont2004@192.168.1.229/servlet?key=number={phone}'
        elif num_phone == 15:
            url = f'http://admin:reMont2004@192.168.1.230/servlet?key=number={phone}'

        try:
            response = requests.post(url)
            if response.status_code == 200:
                return Response({"message": success_message})
            else:
                return Response({"message": error_message})
        except requests.exceptions.RequestException:
            return Response({"message": error_message})
