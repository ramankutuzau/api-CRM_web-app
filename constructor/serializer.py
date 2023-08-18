from rest_framework import serializers

from miscalculation.models import CommercialOffer
from .models import *
from calculation.models import *

class WindowsCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsCalc
        fields = '__all__'



class WindowsillCalcSerializer(serializers.ModelSerializer):
    windowsill_id = serializers.IntegerField(max_value=None, min_value=None)
    installation_id = serializers.IntegerField(max_value=None, min_value=None)
    color_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    plug = serializers.IntegerField(max_value=None, min_value=None)
    connector = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)
    price_output = serializers.FloatField(max_value=None, min_value=None)

    class Meta:
        model = WindowsillCalc
        fields = 'windowsill_id', 'installation_id', 'color_id', 'width', 'length', 'count', 'plug', 'connector', 'markups_type','price_output'


class LowTidesCalcSerializer(serializers.ModelSerializer):
    low_tides_id = serializers.IntegerField(max_value=None, min_value=None)
    installation_id = serializers.IntegerField(max_value=None, min_value=None)
    color_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    plug = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)

    class Meta:
        model = LowTidesCalc
        fields = 'low_tides_id', 'width', 'installation_id', 'color_id', 'length', 'count', 'plug', 'markups_type'


class FlashingCalcSerializer(serializers.ModelSerializer):
    flashing_id = serializers.IntegerField(max_value=None, min_value=None)
    installation_id = serializers.IntegerField(max_value=None, min_value=None)
    color_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)

    class Meta:
        model = FlashingCalc
        fields = 'flashing_id', 'installation_id', 'color_id',  'width', 'length', 'count', 'markups_type'


class CasingCalcSerializer(serializers.ModelSerializer):
    casing_id = serializers.IntegerField(max_value=None, min_value=None)
    installation_id = serializers.IntegerField(max_value=None, min_value=None)
    color_id = serializers.IntegerField(max_value=None, min_value=None)
    fastening_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)

    class Meta:
        model = SlopesOfMetalCalc
        fields = 'casing_id', 'installation_id','fastening_id', 'color_id',  'width', 'length', 'count', 'markups_type'


class VisorsCalcSerializer(serializers.ModelSerializer):
    visors_id = serializers.IntegerField(max_value=None, min_value=None)
    installation_id = serializers.IntegerField(max_value=None, min_value=None)
    color_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)

    class Meta:
        model = VisorsCalc
        fields = 'visors_id', 'installation_id', 'color_id',  'width', 'length', 'count', 'markups_type'


class SlopesOfMetalCalcSerializer(serializers.ModelSerializer):
    slopes_of_metal_id = serializers.IntegerField(max_value=None, min_value=None)
    installation_id = serializers.IntegerField(max_value=None, min_value=None)
    color_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)

    class Meta:
        model = SlopesOfMetal
        fields = 'slopes_of_metal_id', 'installation_id', 'color_id',  'width', 'length', 'count', 'markups_type'


class InternalSlopeCalcSerializer(serializers.ModelSerializer):
    internal_slope_id = serializers.IntegerField(max_value=None, min_value=None)
    installation_id = serializers.IntegerField(max_value=None, min_value=None)
    color_id = serializers.IntegerField(max_value=None, min_value=None)
    width = serializers.IntegerField(max_value=None, min_value=None)
    length = serializers.IntegerField(max_value=None, min_value=None)
    count = serializers.IntegerField(max_value=None, min_value=None)
    markups_type = serializers.IntegerField(max_value=None, min_value=None)

    class Meta:
        model = InternalSlope
        fields = 'internal_slope_id', 'installation_id', 'color_id',  'width', 'length', 'count', 'markups_type'

class WindowSerializer(serializers.ModelSerializer):
    price_input = serializers.FloatField(max_value=None, min_value=None)
    currency_name = serializers.CharField(max_length=255, read_only=False)
    markups_type = serializers.IntegerField(min_value=0, max_value=4, read_only=False)

    class Meta:
        model = WindowDiscountMarkups
        fields = 'profile_id', 'fittings_id', 'price_input', 'markups_type', 'currency_name',

class WindowCalcSerializer(serializers.ModelSerializer):
    window = WindowSerializer(read_only=False)
    price_input = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    price_output = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    fittings_id = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    profile_id = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    discount = serializers.FloatField(read_only=True)
    currency_name = serializers.IntegerField(max_value=None, min_value=None, read_only=True)
    currency_value = serializers.FloatField(max_value=None, min_value=None, read_only=True)

    markups_value = serializers.FloatField(max_value=None, min_value=None, read_only=True)
    markups_percent = serializers.FloatField(max_value=None, min_value=None, read_only=True)
    markups_name = serializers.CharField(read_only=True)
    markups_type = serializers.IntegerField(read_only=True)

    class Meta:
        model = WindowsCalc
        fields = '__all__'

class MountingMaterialsCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingMaterialsCalc
        fields = '__all__'

class WorksCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name']


class AggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregate
        fields = '__all__'


class FittingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fittings
        fields = ['id', 'name']


class SealOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealOutside
        fields = ['id', 'name']


class SealRebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealRebate
        fields = ['id', 'name']


class SealInternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealInternal
        fields = ['id', 'name']


class SealantColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealantColor
        fields = ['id', 'name']


class SealantInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealantInside
        fields = ['id', 'name']


class SealantOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealantOutside
        fields = ['id', 'name']


class SealantShtapikSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealantShtapik
        fields = ['id', 'name']


class ShprosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shpros
        fields = ['id', 'name']


class ShtapikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shtapik
        fields = ['id', 'name']


class SashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sash
        fields = ['id', 'name']


class LaminationOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaminationOutside
        fields = ['id', 'name']


class LaminationInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaminationInside
        fields = ['id', 'name']


class ProfileWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileWeight
        fields = ['id', 'name']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'name']


class ProductsInstallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsInstall
        fields = ['id', 'name']


class PvcSlopesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PvcSlopes
        fields = ['id', 'name']


class WindowsillColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillColor
        fields = '__all__'


class WindowsillInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillInstallation
        fields = '__all__'


class WindowsillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windowsill
        fields = '__all__'


class WindowsillProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsillProvider
        fields = '__all__'


class LowTidesColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTidesColor
        fields = '__all__'

class LowTidesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTidesType
        fields = '__all__'

class LowTidesProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTidesProvider
        fields = '__all__'


class LowTidesInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTidesInstallation
        fields = '__all__'


class LowTidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowTides
        fields = '__all__'


class VisorsColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisorsColor
        fields = '__all__'


class VisorsProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisorsProvider
        fields = '__all__'


class VisorsInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisorsInstallation
        fields = '__all__'


class VisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visors
        fields = '__all__'


class SlopesOfMetalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlopesOfMetalColor
        fields = '__all__'


class SlopesOfMetalProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlopesOfMetalProvider
        fields = '__all__'


class SlopesOfMetalInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlopesOfMetalInstallation
        fields = '__all__'


class SlopesOfMetalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlopesOfMetal
        fields = '__all__'


class MountingMaterialsProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingMaterialsProvider
        fields = '__all__'


class MountingMaterialsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingMaterialsName
        fields = '__all__'


class MountingMaterialsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountingMaterialsType
        fields = '__all__'


class FlashingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashingProvider
        fields = '__all__'


class FlashingColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashingColor
        fields = '__all__'


class FlashingInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashingInstallation
        fields = '__all__'


class FlashingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashing
        fields = '__all__'


class HandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherComplectation
        fields = ['id', 'name']


class CasingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasingProvider
        fields = '__all__'


class CasingColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasingColor
        fields = '__all__'


class CasingFasteningSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasingFastening
        fields = '__all__'


class CasingInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasingInstallation
        fields = '__all__'


class CasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casing
        fields = '__all__'


class InternalSlopeProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalSlopeProvider
        fields = '__all__'


class InternalSlopeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalSlopeColor
        fields = '__all__'


class InternalSlopeInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalSlopeInstallation
        fields = '__all__'


class InternalSlopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalSlope
        fields = '__all__'


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['id', 'name', 'price']


class GorbylkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gorbylki
        fields = '__all__'


class OtherComplectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherComplectation
        fields = '__all__'


class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opening
        fields = '__all__'


class LockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lock
        fields = '__all__'


class DoorHandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorHandles
        fields = '__all__'


class DoorHingesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorHinges
        fields = '__all__'


class CylinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cylinder
        fields = '__all__'


class DoorCloserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorCloser
        fields = '__all__'


class OpeningLimiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningLimiter
        fields = '__all__'


class TypeLaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLamination
        fields = '__all__'


class TypeLamination1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLamination2
        fields = '__all__'


class SealBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SealBasic
        fields = '__all__'


class ArticleAdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAdditionalProfile
        fields = '__all__'


class ConnectionProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionProfileName
        fields = '__all__'


class ColorInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorInside
        fields = '__all__'


class ColorOutsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorOutside
        fields = '__all__'


class ProviderWindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderWindow
        fields = '__all__'


class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'

class LaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamination
        fields = '__all__'

class ConnectionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionProfile
        fields = '__all__'


class AdditionalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalProfile
        fields = '__all__'

class SealantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sealant
        fields = '__all__'


class ConstructorSerializer(serializers.Serializer):
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




class ConstructorPostSerializer(serializers.Serializer):
    product_type = ProductTypeSerializer(read_only=False)
    class Meta:
        model = Constructor
        fields = '__all__'




class ConstructorCategorySerializer(serializers.Serializer):
    profile = ProfileSerializer(read_only=True, many=True)
    product_type = ProductTypeSerializer(read_only=True, many=True)
    aggregate = AggregateSerializer(read_only=True, many=True)
    fittings = FittingsSerializer(read_only=True, many=True)
    seal_outside = SealOutsideSerializer(read_only=True, many=True)
    seal_rebate = SealRebateSerializer(read_only=True, many=True)
    seal_internal = SealInternalSerializer(read_only=True, many=True)
    shpros = ShprosSerializer(read_only=True, many=True)
    shtapik = ShtapikSerializer(read_only=True, many=True)
    sash = SashSerializer(read_only=True, many=True)
    lamination_outside = LaminationOutsideSerializer(read_only=True, many=True)
    lamination_inside = LaminationInsideSerializer(read_only=True, many=True)
    profile_weight = ProfileWeightSerializer(read_only=True, many=True)
    note = NoteSerializer(read_only=True, many=True)
    products_install = ProductsInstallSerializer(read_only=True, many=True)
    pvc_slopes = PvcSlopesSerializer(read_only=True, many=True)
    handles = HandlesSerializer(read_only=True, many=True)
    supply_valve = CasingSerializer(read_only=True, many=True)
    works = WorksSerializer(read_only=True, many=True)
    other_complectation = OtherComplectationSerializer(read_only=True, many=True)
    gorbylki = GorbylkiSerializer(read_only=True, many=True)
    opening = OpeningSerializer(read_only=True, many=True)
    lock = LockSerializer(read_only=True, many=True)
    handle = DoorHandleSerializer(read_only=True, many=True)
    door_hinges = DoorHingesSerializer(read_only=True, many=True)
    cylinder = CylinderSerializer(read_only=True, many=True)
    door_closer = DoorCloserSerializer(read_only=True, many=True)
    opening_limiter = OpeningLimiterSerializer(read_only=True, many=True)
    type_lamination = TypeLaminationSerializer(read_only=True, many=True)
    type_lamination1 = TypeLamination1Serializer(read_only=True, many=True)
    seal_basic = SealBasicSerializer(read_only=True, many=True)
    article = ArticleAdditionalSerializer(read_only=True, many=True)
    connection_profile_name = ConnectionProfileNameSerializer(read_only=True, many=True)
    color_inside = ColorInsideSerializer(read_only=True, many=True)
    color_outside = ColorOutsideSerializer(read_only=True, many=True)
    sealant_color = SealantColorSerializer(read_only=True, many=True)
    sealant_inside = SealantInsideSerializer(read_only=True, many=True)
    sealant_outside = SealantOutsideSerializer(read_only=True, many=True)
    sealant_shtapik = SealantShtapikSerializer(read_only=True, many=True)

    windowsill_color = WindowsillColorSerializer(read_only=True, many=True)
    windowsill_installation = WindowsillInstallationSerializer(read_only=True, many=True)
    windowsill = WindowsillSerializer(read_only=True, many=True)
    windowsill_provider = WindowsillProviderSerializer(read_only=True, many=True)

    casing_fastening = CasingFasteningSerializer(read_only=True, many=True)
    casing_color = CasingColorSerializer(read_only=True, many=True)
    casing_installation = CasingInstallationSerializer(read_only=True, many=True)
    casing = CasingSerializer(read_only=True, many=True)

    flashing_color = FlashingColorSerializer(read_only=True, many=True)
    flashing_installation = FlashingInstallationSerializer(read_only=True, many=True)
    flashing = FlashingSerializer(read_only=True, many=True)

    internal_slope_color = InternalSlopeColorSerializer(read_only=True, many=True)
    internal_slope_installation = InternalSlopeInstallationSerializer(read_only=True, many=True)
    internal_slope = InternalSlopeSerializer(read_only=True, many=True)

    low_tides_color = LowTidesColorSerializer(read_only=True, many=True)
    low_tides_installation = LowTidesInstallationSerializer(read_only=True, many=True)
    low_tides_type = LowTidesTypeSerializer(read_only=True, many=True)
    low_tides = LowTidesSerializer(read_only=True, many=True)


    visors_color = VisorsColorSerializer(read_only=True, many=True)
    visors_installation = VisorsInstallationSerializer(read_only=True, many=True)
    visors = VisorsSerializer(read_only=True, many=True)
    slopes_of_metal_color = SlopesOfMetalColorSerializer(read_only=True, many=True)
    slopes_of_metal_installation = SlopesOfMetalInstallationSerializer(read_only=True, many=True)
    slopes_of_metal = SlopesOfMetalSerializer(read_only=True, many=True)
    mounting_materials_type = MountingMaterialsTypeSerializer(read_only=True, many=True)
    mounting_materials_name = MountingMaterialsNameSerializer(read_only=True, many=True)
    provider_window = ProviderWindowSerializer(read_only=True, many=True)
    low_tides_provider = LowTidesProviderSerializer(read_only=True, many=True)
    visors_provider = VisorsProviderSerializer(read_only=True, many=True)
    casing_provider = CasingProviderSerializer(read_only=True, many=True)
    flashing_provider = FlashingProviderSerializer(read_only=True, many=True)
    slopes_of_metal_provider = SlopesOfMetalProviderSerializer(read_only=True, many=True)
    internal_slope_provider = InternalSlopeProviderSerializer(read_only=True, many=True)
    mounting_materials_provider = MountingMaterialsProviderSerializer(read_only=True, many=True)
