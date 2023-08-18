from rest_framework import serializers
from .models import CallWindow

# from client.serializer import ClientSerializer


class CallWindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallWindow
        fields = '__all__'
