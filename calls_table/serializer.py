from rest_framework import serializers
from .models import *
from call.serializer import CallWindowSerializer
from client.serializer import ClientSerializer


class CallsTableSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False, read_only=False)
    call = CallWindowSerializer(many=False, read_only=False)

    class Meta:
        model = CallsTable
        fields = '__all__'


