from rest_framework.serializers import ModelSerializer
from .models import *


class IncomingMailSerializer(ModelSerializer):
    class Meta:
        model = IncomingMail
        fields = '__all__'


class OutgoingMailSerializer(ModelSerializer):
    class Meta:
        model = OutgoingMail
        fields = '__all__'
