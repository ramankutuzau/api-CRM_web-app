from rest_framework import serializers, status

from calculation.serializer import CasingCalcSerializer, VisorsCalcSerializer, FlashingCalcSerializer, \
    LowTidesCalcSerializer, WindowsillCalcSerializer, WindowsCalcSerializer, SlopesOfMetalCalcSerializer, \
    InternalSlopeCalcSerializer, MountingMaterialsCalcSerializer, WorksCalcSerializer, LaminationSerializer, \
    DoorSerializer, ProductTypeSerializer, ConnectionProfileSerializer, AdditionalProfileSerializer, SealantSerializer
from constructor.serializer import AggregateSerializer, ShtapikSerializer, SashSerializer, GorbylkiSerializer, \
    HandlesSerializer, OtherComplectationSerializer
from .models import *


class MiscalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miscalculation
        fields = ['id', 'author', 'constructors', 'sum', 'status',
                  'created_time', 'last_update_time','hidden_cost']


class CommercialOfferSerializer(serializers.Serializer):

    class Meta:
        model = CommercialOffer
        fields = '__all__'


class ConstructorOfferSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    configuration = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    context = serializers.CharField(read_only=True)
    product_type = ProductTypeSerializer(read_only=True)
    door = DoorSerializer(read_only=True)
    aggregate = AggregateSerializer(read_only=True)
    lamination = LaminationSerializer(read_only=True)

    shtapik = ShtapikSerializer(read_only=True)
    sash = SashSerializer(read_only=True)
    gorbylki = GorbylkiSerializer(read_only=True)
    handles = HandlesSerializer(read_only=True)
    connection_profile = ConnectionProfileSerializer(read_only=True)
    additional_profile = AdditionalProfileSerializer(read_only=True)
    sealant = SealantSerializer(read_only=True)
    other_complectation = OtherComplectationSerializer(read_only=True)

    price_constructor = serializers.FloatField(read_only=True)
    # MATERIALS END
    window_calc = WindowsCalcSerializer(read_only=True,)
    windowsills_calc = WindowsillCalcSerializer(read_only=True,many=True)
    lowtides_calc = LowTidesCalcSerializer(read_only=True,many=True)
    flashing_calc = FlashingCalcSerializer(read_only=True,many=True)
    visors_calc =  VisorsCalcSerializer(read_only=True,many=True)
    casing_calc = CasingCalcSerializer(read_only=True,many=True)
    slopes_of_metal_calc = SlopesOfMetalCalcSerializer(read_only=True,many=True)
    internal_slope_calc = InternalSlopeCalcSerializer(read_only=True,many=True)
    mounting_materials_calc = MountingMaterialsCalcSerializer(read_only=True,many=True)
    works = WorksCalcSerializer(read_only=True,many=True)
    final_image = serializers.CharField(read_only=False,max_length=10000000)

    class Meta:
        model = Constructor
        fields = '__all__'



class HideCostSerializer(serializers.ModelSerializer):
    cost = serializers.FloatField()
    class Meta:
        model = Miscalculation
        fields = 'pk', 'cost'