from rest_framework import serializers

from .models import OutgoingCalls


class OutGoingCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutgoingCalls
        fields = '__all__'