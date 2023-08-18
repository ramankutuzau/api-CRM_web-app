from rest_framework import serializers

from constructor.serializer import *
from measurer.models import *


class WindowsillCalcSerializer(serializers.ModelSerializer):
    windowsill = WindowsillSerializer(read_only=True)

    class Meta:
        model = WindowsillCalcMob
        fields = '__all__'


class LowTidesCalcSerializer(serializers.ModelSerializer):
    low_tides = LowTidesSerializer(read_only=True)

    class Meta:
        model = LowTidesCalcMob
        fields = '__all__'


class VisorsCalcSerializer(serializers.ModelSerializer):
    visors = VisorsSerializer(read_only=True)

    class Meta:
        model = VisorsCalcMob
        fields = '__all__'


class AdditionalProfileCalcSerializer(serializers.ModelSerializer):
    additional_profile = AdditionalProfileSerializer(read_only=True)

    class Meta:
        model = AdditionalProfileCalcMob
        fields = '__all__'


class ConnectionalProfileCalcSerializer(serializers.ModelSerializer):
    connection_profile = ConnectionProfileSerializer(read_only=True)

    class Meta:
        model = ConnectionProfileCalcMob
        fields = '__all__'


class FlashingCalcSerializer(serializers.ModelSerializer):
    flashing = FlashingSerializer(read_only=True)

    class Meta:
        model = FlashingCalcMob
        fields = '__all__'


class CasingCalcSerializer(serializers.ModelSerializer):
    casing = CasingSerializer(read_only=True)

    class Meta:
        model = CasingCalcMob
        fields = '__all__'


class SlopesOfMetalCalcSerializer(serializers.ModelSerializer):
    slopes_of_metal = SlopesOfMetalSerializer(read_only=True)

    class Meta:
        model = SlopesOfMetalCalcMob
        fields = '__all__'


class InternalSlopesCalcSerializer(serializers.ModelSerializer):
    internal_slopes = InternalSlopeSerializer(read_only=True)

    class Meta:
        model = InternalSlopesCalcMob
        fields = '__all__'


class MountingMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingMaterials
        fields = '__all__'


class MountingMaterialsCalcSerializer(serializers.ModelSerializer):
    mounting_materials = MountingMaterialsSerializer(read_only=True)

    class Meta:
        model = MountingMaterialsCalcMob
        fields = '__all__'


class WorksCalcSerializer(serializers.ModelSerializer):
    works = WorksSerializer(read_only=True)

    class Meta:
        model = WorksCalcMob
        fields = '__all__'


class OtherCalcSerializer(serializers.ModelSerializer):
    other = OtherComplectationSerializer(read_only=True)

    class Meta:
        model = OtherCalcMob
        fields = '__all__'


class Windows1CalcSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    fittings = FittingsSerializer(read_only=True)
    filling = AggregateSerializer(read_only=True)

    class Meta:
        model = Windows1Calc
        fields = '__all__'


class Windows2CalcSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    fittings = FittingsSerializer(read_only=True)
    filling = AggregateSerializer(read_only=True)

    class Meta:
        model = Windows2Calc
        fields = '__all__'


class Windows3CalcSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    fittings = FittingsSerializer(read_only=True)
    filling = AggregateSerializer(read_only=True)

    class Meta:
        model = Windows3Calc
        fields = '__all__'


class Windows4CalcSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    fittings = FittingsSerializer(read_only=True)
    filling = AggregateSerializer(read_only=True)

    class Meta:
        model = Windows4Calc
        fields = '__all__'


class DoorCalcSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    fittings = FittingsSerializer(read_only=True)
    filling = AggregateSerializer(read_only=True)

    class Meta:
        model = DoorCalc
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    windowsill_calc = WindowsillCalcSerializer(read_only=True, many=True)
    low_tides_calc = LowTidesCalcSerializer(read_only=True, many=True)
    visors_calc = VisorsCalcSerializer(read_only=True, many=True)
    additional_profile_calc = AdditionalProfileCalcSerializer(read_only=True, many=True)
    connection_profile_calc = ConnectionalProfileCalcSerializer(read_only=True, many=True)
    flashing_calc = FlashingCalcSerializer(read_only=True, many=True)
    casing_calc = CasingCalcSerializer(read_only=True, many=True)
    slopes_of_metal_calc = SlopesOfMetalCalcSerializer(read_only=True, many=True)
    internal_slopes_calc = InternalSlopesCalcSerializer(read_only=True, many=True)
    mounting_materials_calc = MountingMaterialsCalcSerializer(read_only=True, many=True)
    works_calc = WorksCalcSerializer(read_only=True, many=True)
    other_calc = OtherCalcSerializer(read_only=True, many=True)
    windows_1_calc = Windows1CalcSerializer(read_only=True, many=True)
    windows_2_calc = Windows2CalcSerializer(read_only=True, many=True)
    windows_3_calc = Windows3CalcSerializer(read_only=True, many=True)
    windows_4_calc = Windows3CalcSerializer(read_only=True, many=True)
    door_calc = DoorCalcSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'


class MiscalculationMobSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = MiscalculationMob
        fields = '__all__'
