import requests
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics, viewsets, mixins
from .utils import *
from .serializer import *
from .utils import *
from django.forms import model_to_dict
from config.pagination import CustomPagination
from constructor.models import *


class CalculationWindowAPIView(APIView):
    serializer_class = WindowCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile_id = request.data['window']['profile_id']
        fittings_id = request.data['window']['fittings_id']
        currency = request.data['window']['currency_name']
        price_input = request.data['window']['price_input']
        markup_type = request.data['window']['markups_type']
        window_calc = calc_window_disc(profile_id=profile_id, fittings_id=fittings_id, markup_type=markup_type,
                                       currency=currency,
                                       price=price_input)

        return Response({'data': model_to_dict(window_calc)})
        # return Response({'data': serializer.data})


class CalculationWindowsillAPIView(APIView):
    serializer_class = WindowsillCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        windowsill_id = request.data['windowsill_id']
        print(windowsill_id)
        width = request.data['width']
        length = request.data['length']
        installation_id = request.data['installation_id']
        color_id = request.data['color_id']
        count = request.data['count']
        markups_type = request.data['markups_type']
        windowsill_calc = calc_windowsill(windowsill_id=windowsill_id, width=width,color_id=color_id,installation_id=installation_id,
                                          length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(windowsill_calc)})


class CalculationLowTidesAPIView(APIView):
    serializer_class = LowTidesCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        low_tides_id = request.data['low_tides_id']
        low_tides_type = LowTidesType.objects.get(pk=request.data['low_tides_type'])
        installation_id = request.data['installation_id']
        color_id = request.data['color_id']
        plug = request.data['plug']
        width = request.data['width']
        width_1 = request.data['width_1']
        width_2 = request.data['width_2']
        width_3 = request.data['width_3']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        low_tides_calc = calc_low_tides(low_tides_id=low_tides_id, width=width,width_1=width_1,width_2=width_2,width_3=width_3,plug=plug,color_id=color_id,installation_id=installation_id,low_tides_type=low_tides_type,
                                        length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(low_tides_calc)})


class CalculationFlashingAPIView(APIView):
    serializer_class = FlashingCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        flashing_id = request.data['flashing_id']
        installation_id = request.data['installation_id']
        color_id = request.data['color_id']
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        flashing_calc = calc_flashing(flashing_id=flashing_id, width=width,color_id=color_id,installation_id=installation_id,
                                      length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(flashing_calc)})


class CalculationCasingAPIView(APIView):
    serializer_class = CasingCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        casing_id = request.data['casing_id']
        installation_id = request.data['installation_id']
        fastening_id = request.data['fastening_id']
        color_id = request.data['color_id']
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        casing_calc = calc_casing(casing_id=casing_id, width=width,color_id=color_id,installation_id=installation_id,
                                  fastening_id=fastening_id,length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(casing_calc)})


class CalculationVisorsAPIView(APIView):
    serializer_class = VisorsCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        visors_id = request.data['visors_id']
        installation_id = request.data['installation_id']
        color_id = request.data['color_id']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']
        width_1 = request.data['width_1']
        width_2 = request.data['width_2']
        width_3= request.data['width_3']

        visors_calc = calc_visors(visors_id=visors_id, color_id=color_id,installation_id=installation_id,width_1=width_1,width_2=width_2,width_3=width_3,
                                  length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(visors_calc)})


class CalculationSlopesOfMetalAPIView(APIView):
    serializer_class = SlopesOfMetalCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        slopes_of_metal_id = request.data['slopes_of_metal_id']
        installation_id = request.data['installation_id']
        color_id = request.data['color_id']
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        slopes_of_metal_calc = calc_slopes_of_metal(slopes_of_metal_id=slopes_of_metal_id, width=width,color_id=color_id,installation_id=installation_id,
                                                    length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(slopes_of_metal_calc)})


class CalculationInternalSlopeAPIView(APIView):
    serializer_class = InternalSlopeCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        internal_slope_id = request.data['internal_slope_id']
        installation_id = request.data['installation_id']
        color_id = request.data['color_id']
        width = request.data['width']
        length = request.data['length']
        count = request.data['count']
        markups_type = request.data['markups_type']

        internal_slope = calc_internal_slope(internal_slope_id=internal_slope_id, width=width,color_id=color_id,installation_id=installation_id,
                                             length=length, count=count, markups_type=markups_type)

        return Response({'data': model_to_dict(internal_slope)})


# class ConstructorViewSet(viewsets.ModelViewSet):
#     queryset = Constructor.objects.all()
#     serializer_class = ConstructorSerializer
#     pagination_class = CustomPagination
#     http_method_names = ['get', 'patch', 'post']
#
#     def list(self, request):
#         queryset = Constructor.objects.all()
#         serializer = ConstructorSerializer(queryset, many=True)
#         return Response({"data": serializer.data})
#
#     def retrieve(self, request, pk=None):
#         queryset = Constructor.objects.all()
#         mail = get_object_or_404(queryset, pk=pk)
#         serializer = ConstructorSerializer(mail)
#         return Response({"data": serializer.data})
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         constructor = Constructor.objects.create()
#
#         # product_type = ProductType.objects.get(pk=request.data['product_type']),
#         # constructor.product_type = ProductType.objects.get(id=request.data['product_type'])
#         try:
#             constructor.product_type = ProductType.objects.get(pk=request.data['product_type'])
#         except:
#             pass
#
#         try:
#             constructor.door = Door.objects.get(pk=request.data['door'])
#         except:
#             pass
#
#         try:
#             constructor.aggregate = Aggregate.objects.get(pk=request.data['aggregate'])
#         except:
#             pass
#
#         try:
#             constructor.lamination = Lamination.objects.get(pk=request.data['lamination'])
#         except:
#             pass
#
#         try:
#             constructor.shtapik = Shtapik.objects.get(pk=request.data['shtapik'])
#         except:
#             pass
#
#         try:
#             constructor.sash = Sash.objects.get(pk=request.data['sash'])
#         except:
#             pass
#
#         try:
#             constructor.gorbylki = Gorbylki.objects.get(pk=request.data['gorbylki'])
#         except:
#             pass
#
#         try:
#             constructor.handles = Handles.objects.get(pk=request.data['handles'])
#         except:
#             pass
#
#         try:
#             constructor.connection_profile = ConnectionProfile.objects.get(pk=request.data['connection_profile'])
#         except:
#             pass
#
#         try:
#             constructor.additional_profile = AdditionalProfile.objects.get(pk=request.data['additional_profile'])
#         except:
#             pass
#
#         try:
#             constructor.other_complectation = OtherComplectation.objects.get(pk=request.data['other_complectation'])
#         except:
#             pass
#
#         try:
#             constructor.price_constructor = request.data['price_constructor']
#         except:
#             pass
#
#         # constructor.name = "HUI"
#
#         try:
#             for i in request.data['windowsills_calc']:
#                 constructor.windowsills_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['casing_calc']:
#                 constructor.casing_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['flashing_calc']:
#                 constructor.flashing_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['visors_calc']:
#                 constructor.visors_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['lowtides_calc']:
#                 constructor.lowtides_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['works']:
#                 constructor.works.add(i)
#         except:
#             pass
#         constructor.save()
#         serializer = ConstructorSerializer(constructor)
#         return Response({'data': serializer.data})
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         constructor = Constructor.objects.get(id=instance.pk)
#         try:
#             constructor.product_type = ProductType.objects.get(pk=request.data['product_type'])
#         except:
#             pass
#
#         try:
#             constructor.door = Door.objects.get(pk=request.data['door'])
#         except:
#             pass
#
#         try:
#             constructor.aggregate = Aggregate.objects.get(pk=request.data['aggregate'])
#         except:
#             pass
#
#         try:
#             constructor.lamination = Lamination.objects.get(pk=request.data['lamination'])
#         except:
#             pass
#
#         try:
#             constructor.shtapik = Shtapik.objects.get(pk=request.data['shtapik'])
#         except:
#             pass
#
#         try:
#             constructor.sash = Sash.objects.get(pk=request.data['sash'])
#         except:
#             pass
#
#         try:
#             constructor.gorbylki = Gorbylki.objects.get(pk=request.data['gorbylki'])
#         except:
#             pass
#
#         try:
#             constructor.handles = Handles.objects.get(pk=request.data['handles'])
#         except:
#             pass
#
#         try:
#             constructor.connection_profile = ConnectionProfile.objects.get(pk=request.data['connection_profile'])
#         except:
#             pass
#
#         try:
#             constructor.additional_profile = AdditionalProfile.objects.get(pk=request.data['additional_profile'])
#         except:
#             pass
#
#         try:
#             constructor.other_complectation = OtherComplectation.objects.get(pk=request.data['other_complectation'])
#         except:
#             pass
#
#         try:
#             constructor.price_constructor = request.data['price_constructor']
#         except:
#             pass
#         try:
#             constructor.name = request.data['name']
#         except:
#             pass
#
#         try:
#             for i in request.data['windowsills_calc']:
#                 constructor.windowsills_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['casing_calc']:
#                 constructor.casing_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['flashing_calc']:
#                 constructor.flashing_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['visors_calc']:
#                 constructor.visors_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['lowtides_calc']:
#                 constructor.lowtides_calc.add(i)
#         except:
#             pass
#         try:
#             for i in request.data['works']:
#                 constructor.works.add(i)
#         except:
#             pass
#         constructor.save()
#
#         serializer = ConstructorSerializer(constructor)
#         return Response({"data": serializer.data})


class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Door.objects.all()
        serializer = DoorSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Door.objects.all()
        door = get_object_or_404(queryset, pk=pk)
        serializer = DoorSerializer(door)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class LaminationViewSet(viewsets.ModelViewSet):
    queryset = Lamination.objects.all()
    serializer_class = LaminationSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Lamination.objects.all()
        serializer = LaminationSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Lamination.objects.all()
        lamination = get_object_or_404(queryset, pk=pk)
        serializer = LaminationSerializer(lamination)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class ConnectionProfileViewSet(viewsets.ModelViewSet):
    queryset = ConnectionProfile.objects.all()
    serializer_class = ConnectionProfileSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = ConnectionProfile.objects.all()
        serializer = ConnectionProfileSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = ConnectionProfile.objects.all()
        connection_profile = get_object_or_404(queryset, pk=pk)
        serializer = ConnectionProfileSerializer(connection_profile)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class AdditionalProfileViewSet(viewsets.ModelViewSet):
    queryset = AdditionalProfile.objects.all()
    serializer_class = AdditionalProfileSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = AdditionalProfile.objects.all()
        serializer = AdditionalProfileSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = AdditionalProfile.objects.all()
        additional_profile = get_object_or_404(queryset, pk=pk)
        serializer = AdditionalProfileSerializer(additional_profile)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})


class SealantViewSet(viewsets.ModelViewSet):
    queryset = Sealant.objects.all()
    serializer_class = SealantSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = Sealant.objects.all()
        serializer = SealantSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Sealant.objects.all()
        sealant = get_object_or_404(queryset, pk=pk)
        serializer = SealantSerializer(sealant)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})

class CalculationWindowsillAPIView(APIView):
    serializer_class = WindowsillCalcSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        windowsill_id = request.data['windowsill_id']
        print(windowsill_id)
        width = request.data['width']
        length = request.data['length']
        installation_id = request.data['installation_id']
        color_id = request.data['color_id']
        count = request.data['count']
        markups_type = request.data['markups_type']
        plug = request.data['plug']
        connector = request.data['connector']
        windowsill_calc = calc_windowsill(windowsill_id=windowsill_id, width=width,color_id=color_id,installation_id=installation_id,
                                          length=length, count=count, markups_type=markups_type, connector=connector,plug=plug)

        return Response({'data': model_to_dict(windowsill_calc)})

