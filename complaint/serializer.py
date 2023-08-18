from rest_framework import serializers, status

from .models import *
from users.serializers import UserSerializer


class ComplaintSerializer(serializers.ModelSerializer):
    time_create = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Complaint
        fields = '__all__'
