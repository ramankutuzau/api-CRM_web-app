from rest_framework import serializers, status

from call.models import CallWindow
from .models import Client, Number, Address, Prompter, Contract, PassportDetails
from call.serializer import CallWindowSerializer
from miscalculation.serializer import MiscalculationSerializer
from complaint.serializer import ComplaintSerializer
from constructor.serializer import ConstructorSerializer

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ['id', 'number', 'name']

class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'

class PassportDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportDetails
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name']


class PrompterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompter
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=False)
    is_active = serializers.BooleanField(read_only=True)
    numbers = NumberSerializer(many=True, read_only=False)
    addresses = AddressSerializer(many=True, read_only=False)
    prompter = PrompterSerializer(many=True, read_only=False)
    calls = CallWindowSerializer(many=True, read_only=False)
    passport_details = PassportDetailsSerializer(read_only=False)
    contract = ContractSerializer(many=True, read_only=False)
    miscalculation = MiscalculationSerializer(many=True, read_only=False)
    complaints = ComplaintSerializer(many=True, read_only=False)
    category_select = serializers.IntegerField(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class ClientPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientPostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=False)
    is_active = serializers.BooleanField(read_only=True)
    author = serializers.CharField(read_only=True)
    calls = CallWindowSerializer(many=True, read_only=True)
    numbers = NumberSerializer(many=True, read_only=True)
    addresses = AddressSerializer(many=True, read_only=True)
    prompter = PrompterSerializer(many=True, read_only=True)
    constructor = ConstructorSerializer(many=True, read_only=True)
    contract = ContractSerializer(many=True, read_only=True)
    passport_details = PassportDetailsSerializer(read_only=True)
    miscalculation = MiscalculationSerializer(many=True, read_only=True)
    complaints = ComplaintSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
