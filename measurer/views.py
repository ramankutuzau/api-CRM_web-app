import datetime

from django.db.models import Sum
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from client.models import Number
from .forms import *
from .models import *
from .serializer import MiscalculationMobSerializer
from .utils import *
from num2words import num2words


# Create your views here.

class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order"


def order(request, miscalc_pk, order_pk, form):
    user = User.objects.get(username=request.user.username)

    if request.method == "GET":
        pass

    if request.method == 'POST':
        try:
            WindowsillCalcMob.objects.get(pk=request.POST.get(f'id_windowsill_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='windowsill')
        except:
            pass
        try:
            LowTidesCalcMob.objects.get(pk=request.POST.get(f'id_low_tides_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='low-tides')
        except:
            pass
        try:
            AdditionalProfileCalcMob.objects.get(pk=request.POST.get(f'id_additional_profile_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='additional-profile')
        except:
            pass
        try:
            ConnectionProfileCalcMob.objects.get(pk=request.POST.get(f'id_connection_profile_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='connection-profile')
        except:
            pass
        try:
            VisorsCalcMob.objects.get(pk=request.POST.get(f'id_visors_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='visors')
        except:
            pass
        try:
            FlashingCalcMob.objects.get(pk=request.POST.get(f'id_flashing_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='flashing')
        except:
            pass
        try:
            CasingCalcMob.objects.get(pk=request.POST.get(f'id_casing_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='casing')
        except:
            pass
        try:
            SlopesOfMetalCalcMob.objects.get(pk=request.POST.get(f'id_slopes_of_metal_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='slopes-of-metal')
        except:
            pass
        try:
            InternalSlopesCalcMob.objects.get(pk=request.POST.get(f'id_internal_slopes_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='internal-slopes')
        except:
            pass
        try:
            MountingMaterialsCalcMob.objects.get(pk=request.POST.get(f'id_mounting_materials_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='mounting-materials')
        except:
            pass
        try:
            WorksCalcMob.objects.get(pk=request.POST.get(f'id_works_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='works')
        except:
            pass
        try:
            OtherCalcMob.objects.get(pk=request.POST.get(f'id_other_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='works')
        except:
            pass
        try:
            Windows1Calc.objects.get(pk=request.POST.get(f'id_windows_1_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            pass
        try:
            Windows2Calc.objects.get(pk=request.POST.get(f'id_windows_2_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            pass
        try:
            Windows3Calc.objects.get(pk=request.POST.get(f'id_windows_3_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            pass
        try:
            Windows4Calc.objects.get(pk=request.POST.get(f'id_windows_4_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            pass
        try:
            DoorCalc.objects.get(pk=request.POST.get(f'id_door_calc')).delete()
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            pass

        one_sash_width = request.POST.get('one-sash-width')
        one_sash_length = request.POST.get('one-sash-length')

        try:
            if one_sash_width and one_sash_length and int(one_sash_width) > 0 and int(one_sash_length) > 0:
                profile = request.POST.get('one-sash-profile-select')
                fittings = request.POST.get('one-sash-fitting-select')
                filling = request.POST.get('one-sash-filling-select')
                window = request.POST.get('one-sash-select')
                calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=window,
                             width=one_sash_width, length=one_sash_length, sash=1)
                return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            pass

        two_sash_width = request.POST.get('two-sash-width')
        two_sash_length = request.POST.get('two-sash-length')
        try:
            if two_sash_width and two_sash_length and int(two_sash_width) > 0 and int(two_sash_length) > 0:
                profile = request.POST.get('two-sash-profile-select')
                fittings = request.POST.get('two-sash-fitting-select')
                filling = request.POST.get('two-sash-filling-select')
                window_1 = request.POST.get('two-sash-select-1')
                window_2 = request.POST.get('two-sash-select-2')
                window = f'{window_1}_{window_2}'
                print(window)
                calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=window,
                             width=two_sash_width, length=two_sash_length, sash=2)
                return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            form = 'products'

        three_sash_width = request.POST.get('three-sash-width')
        three_sash_length = request.POST.get('three-sash-length')
        try:
            if three_sash_width and three_sash_length and int(three_sash_width) > 0 and int(three_sash_length) > 0:
                profile = request.POST.get('three-sash-profile-select')
                fittings = request.POST.get('three-sash-fitting-select')
                filling = request.POST.get('three-sash-filling-select')
                window_1 = request.POST.get('three-sash-select-1')
                window_2 = request.POST.get('three-sash-select-2')
                window_3 = request.POST.get('three-sash-select-3')
                print(f' {profile} {fittings} {filling} {window_1} {window_2}')
                print(f' {three_sash_width} {three_sash_length}')
                window = f'{window_1}_{window_2}_{window_3}'
                calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=window,
                             width=three_sash_width, length=three_sash_length, sash=3)
                return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            form = 'products'

        four_sash_width = request.POST.get('four-sash-width')
        four_sash_length = request.POST.get('four-sash-length')

        try:
            if four_sash_width and four_sash_length and int(four_sash_width) > 0 and int(four_sash_length) > 0:
                profile = request.POST.get('four-sash-profile-select')
                fittings = request.POST.get('four-sash-fitting-select')
                filling = request.POST.get('four-sash-filling-select')
                window_1 = request.POST.get('four-sash-select-1')
                window_2 = request.POST.get('four-sash-select-2')
                window_3 = request.POST.get('four-sash-select-3')
                window_4 = request.POST.get('four-sash-select-4')
                print(f' {profile} {fittings} {filling} {window_1} {window_2} {window_3} {window_4}''')
                print(f' {four_sash_width} {four_sash_length}')
                window = f'{window_1}_{window_2}_{window_3}_{window_4}'
                calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=window,
                             width=four_sash_width, length=four_sash_length, sash=4)
                return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            form = 'products'

        door_width = request.POST.get('door-width')
        door_length = request.POST.get('door-length')

        try:
            if door_width and door_length and int(door_width) > 0 and int(door_length) > 0:
                profile = request.POST.get('door-profile-select')
                fittings = request.POST.get('door-fitting-select')
                filling = request.POST.get('door-filling-select')
                door = request.POST.get('door-select')
                door = f'{door}'
                calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=door,
                             width=door_width, length=door_length, sash=0)
                return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')
        except:
            form = 'products'

        form_windowsill_calc = WindowsillCalcForm(request.POST)
        if form_windowsill_calc.is_valid():
            cleaned_data = form_windowsill_calc.cleaned_data
            calc_windowsill(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='windowsill')

        form_low_tides_calc = LowTidesCalcForm(request.POST)
        if form_low_tides_calc.is_valid():
            cleaned_data = form_low_tides_calc.cleaned_data
            calc_low_tides(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='low-tides')

        form_additional_profile_calc = AdditionalProfileCalcForm(request.POST)
        if form_additional_profile_calc.is_valid():
            cleaned_data = form_additional_profile_calc.cleaned_data
            calc_additional_profile(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='additional-profile')

        form_connection_profile_calc = ConnectionProfileCalcForm(request.POST)
        if form_connection_profile_calc.is_valid():
            cleaned_data = form_connection_profile_calc.cleaned_data
            calc_connection_profile(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='connection-profile')

        form_visors_calc = VisorsCalcForm(request.POST)
        if form_visors_calc.is_valid():
            cleaned_data = form_visors_calc.cleaned_data
            calc_visors(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='visors')

        form_flashing_calc = FlashingCalcForm(request.POST)
        if form_flashing_calc.is_valid():
            cleaned_data = form_flashing_calc.cleaned_data
            calc_flashing(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='flashing')

        form_casing_calc = CasingCalcForm(request.POST)
        if form_casing_calc.is_valid():
            cleaned_data = form_casing_calc.cleaned_data
            calc_casing(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='casing')

        form_slopes_of_metal_calc = SlopesOfMetalCalcForm(request.POST)
        if form_slopes_of_metal_calc.is_valid():
            cleaned_data = form_slopes_of_metal_calc.cleaned_data
            calc_slopes_of_metal(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='slopes-of-metal')

        form_internal_slopes_calc = InternalSlopesCalcForm(request.POST)
        if form_internal_slopes_calc.is_valid():
            cleaned_data = form_internal_slopes_calc.cleaned_data
            calc_internal_slopes(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='internal-slopes')

        form_mounting_materials_calc = MountingMaterialsCalcForm(request.POST)
        if form_mounting_materials_calc.is_valid():
            cleaned_data = form_mounting_materials_calc.cleaned_data
            calc_mounting_materials(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='mounting-materials')

        form_works_calc = WorksCalcForm(request.POST)
        if form_works_calc.is_valid():
            cleaned_data = form_works_calc.cleaned_data
            calc_works(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='works')

        form_other_calc = OtherCalcForm(request.POST)
        if form_other_calc.is_valid():
            cleaned_data = form_other_calc.cleaned_data
            calc_other(order_id=order_pk, **cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='works')

        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            cleaned_data = form_order.cleaned_data
            cleaned_data['user'] = user
            Order.objects.filter(pk=order_pk).update(**cleaned_data)
            return redirect('order', order_pk=order_pk, miscalc_pk=miscalc_pk, form='None')
    try:
        calc_order(miscalc_pk=miscalc_pk)
    except:
        pass
    order = Order.objects.get(pk=order_pk)

    windowsill_calc = WindowsillCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    low_tides_calc = LowTidesCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    additional_profile_calc = AdditionalProfileCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    connection_profile_calc = ConnectionProfileCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    visors_calc = VisorsCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    flashing_calc = FlashingCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    casing_calc = CasingCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    slopes_of_metal_calc = SlopesOfMetalCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    internal_slopes_calc = InternalSlopesCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    mounting_materials_calc = MountingMaterialsCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    works_calc = WorksCalcMob.objects.filter(order_id=order_pk).order_by('-id')
    other_calc = OtherCalcMob.objects.filter(order_id=order_pk).order_by('-id')

    windows_1_calc = Windows1Calc.objects.filter(order_id=order_pk).order_by('-id')
    windows_2_calc = Windows2Calc.objects.filter(order_id=order_pk).order_by('-id')
    windows_3_calc = Windows3Calc.objects.filter(order_id=order_pk).order_by('-id')
    windows_4_calc = Windows4Calc.objects.filter(order_id=order_pk).order_by('-id')
    door_calc = DoorCalc.objects.filter(order_id=order_pk).order_by('-id')

    check_windows = any([windows_1_calc, windows_2_calc, windows_3_calc, windows_4_calc, door_calc])
    check_works = any([works_calc, other_calc])

    works_other_sum = order.sum_other_byn + order.sum_works_byn

    form_windowsill_calc = WindowsillCalcForm(
        initial={'windowsill_count': 1, 'windowsill': 1, 'windowsill_color': 1, 'windowsill_plug': 1,
                 'windowsill_plug_count': 1, })

    form_low_tides_calc = LowTidesCalcForm(
        initial={'low_tides_count': 1, 'low_tides': 1, 'low_tides_type': 1, 'low_tides_color': 1, 'low_tides_plug': 1,
                 'low_tides_plug_count': 1, })

    form_additional_profile_calc = AdditionalProfileCalcForm(initial={'count': 1})

    form_connection_profile_calc = ConnectionProfileCalcForm(initial={'count': 1})

    form_visors_calc = VisorsCalcForm(initial={'count': 1, 'visors_color': 1})

    form_flashing_calc = FlashingCalcForm(initial={'count': 1, 'flashing_color': 1})

    form_casing_calc = CasingCalcForm(initial={'count': 1, 'casing_color': 1})

    form_slopes_of_metal_calc = SlopesOfMetalCalcForm(initial={'count': 1, 'slopes_of_metal_color': 1})

    form_internal_slopes_calc = InternalSlopesCalcForm(initial={'count': 1, 'internal_slopes_color': 1})

    form_mounting_materials_calc = MountingMaterialsCalcForm(initial={'count': 1})

    form_works_calc = WorksCalcForm(initial={'count': 1})

    form_other_calc = OtherCalcForm(initial={'count': 1})

    profiles = Profile.objects.all()
    fittings = Fittings.objects.all()
    filling = Aggregate.objects.all()
    context = {
        'profiles': profiles,
        'fittings': fittings,
        'filling': filling,

        'form': form,
        'order': order,

        'miscalc_pk': miscalc_pk,
        'order_pk': order_pk,

        'form_windowsill_calc': form_windowsill_calc,
        'windowsill_calc': windowsill_calc,

        'form_low_tides_calc': form_low_tides_calc,
        'low_tides_calc': low_tides_calc,

        'form_additional_profile_calc': form_additional_profile_calc,
        'additional_profile_calc': additional_profile_calc,

        'form_connection_profile_calc': form_connection_profile_calc,
        'connection_profile_calc': connection_profile_calc,

        'form_visors_calc': form_visors_calc,
        'visors_calc': visors_calc,

        'form_flashing_calc': form_flashing_calc,
        'flashing_calc': flashing_calc,

        'form_casing_calc': form_casing_calc,
        'casing_calc': casing_calc,

        'form_slopes_of_metal_calc': form_slopes_of_metal_calc,
        'slopes_of_metal_calc': slopes_of_metal_calc,

        'form_internal_slopes_calc': form_internal_slopes_calc,
        'internal_slopes_calc': internal_slopes_calc,

        'form_mounting_materials_calc': form_mounting_materials_calc,
        'mounting_materials_calc': mounting_materials_calc,

        'form_works_calc': form_works_calc,
        'works_calc': works_calc,

        'form_other_calc': form_other_calc,
        'other_calc': other_calc,

        'windows_1_calc': windows_1_calc,
        'windows_2_calc': windows_2_calc,
        'windows_3_calc': windows_3_calc,
        'windows_4_calc': windows_4_calc,
        'door_calc': door_calc,

        'check_windows': check_windows,
        'check_works': check_works,
        'works_other_sum': works_other_sum,
    }
    return render(request, 'order_detail.html', context)


def order_list(request, pk):
    calc_order(miscalc_pk=pk)

    miscalculation = MiscalculationMob.objects.get(pk=pk)
    if miscalculation.status == 'запланирован' or miscalculation.status == 'выполнен':
        miscalculation.status = 'активный'
        miscalculation.save()
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('accounts/login/')

    if request.method == "GET":
        id_order = request.GET.get('id_order')
        if id_order:
            Order.objects.filter(pk=id_order, user=user, active=True).delete()


    if request.method == 'POST':


        try:
            Order.objects.get(pk=request.POST.get(f'id_order')).delete()
            return redirect('order_list', pk=pk)
        except:
            pass
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            order = form_order.save(commit=False)
            order.user = user
            order.save()
            miscalculation.orders.add(order)

            return redirect('order', order_pk=order.pk, miscalc_pk=pk, form=None)






    form_order = OrderForm()

    total_sum_byn = 0
    for order in miscalculation.orders.all():
        total_sum_byn += order.sum_byn
    miscalculation.total_cost = total_sum_byn

    miscalculation.save()

    try:
        orders_id = MiscalculationMob.objects.filter(pk=pk).values_list('orders', flat=True)
        orders = []
        for el in orders_id:
            orders.append(Order.objects.get(pk=el))
        total_cost = miscalculation.total_cost
    except:
        pass
    passport_details = miscalculation.client.passport_details
    passport_form = PassportDetailsForm(instance=passport_details)

    contract = miscalculation.contract
    contract_form = ContractForm(instance=contract)


    context = {
        'form_order': form_order,
        'orders': orders,
        'miscalc_pk': pk,
        'passport': passport_form,
        'contract_form': contract_form,
        'contract': contract,
        'miscalculation': miscalculation,

    }
    return render(request, 'miscalculations_detail.html', context)


def miscalculation(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('accounts/login/')
    if request.method == 'POST':
        form_miscalculation = MiscalculationForm(request.POST)
        if form_miscalculation.is_valid():
            miscalculation = form_miscalculation.save()
            miscalculation.user = request.user
            phone = form_miscalculation.cleaned_data['phone']
            name = form_miscalculation.cleaned_data['name']
            number, created = Number.objects.get_or_create(number=phone)
            client, created = Client.objects.get_or_create(author=request.user.username, name=name)
            client.numbers.add(number)
            passport = PassportDetails.objects.create(name=name)
            client.passport_details = passport
            client.save()
            last_contract = Contract.objects.order_by('-id').first()
            last_number = int(last_contract.number) if last_contract else 0
            new_number = last_number + 1
            contract = Contract.objects.create(number=str(new_number),phone=phone,date=datetime.datetime.now(),passport_details=passport)
            miscalculation.contract = contract
            miscalculation.client = client

            miscalculation.save()
            return redirect('order_list', pk=miscalculation.pk)
    date = datetime.datetime.now()

    if request.method == 'GET':
        date_now = request.GET.get('date-now')
        if date_now:
            date = datetime.datetime.strptime(date_now, '%Y-%m-%d').date()
        date_now = request.GET.get('date-now')

        if 'back' in request.GET:
            date = datetime.datetime.strptime(date_now, '%Y-%m-%d').date() - datetime.timedelta(days=1)

        if 'plus' in request.GET:
            date = datetime.datetime.strptime(date_now, '%Y-%m-%d').date() + datetime.timedelta(days=1)

    print(date)
    miscalculation = MiscalculationMob.objects.filter(user=user, active=True, date=date).order_by('-pk')

    form_miscalculation = MiscalculationForm(initial={
        'status': 1,
        'date': datetime.datetime.now(),
    })
    context = {
        'date': date.strftime('%Y-%m-%d'),
        'miscalculation': miscalculation,
        'form_miscalculation': form_miscalculation,
    }
    return render(request, 'miscalculation.html', context)


def miscalculation_history(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('accounts/login/')
    if request.method == 'POST':
        form_miscalculation = MiscalculationForm(request.POST)
        if form_miscalculation.is_valid():
            miscalculation = form_miscalculation.save()
            miscalculation.user = request.user
            miscalculation.save()
            return redirect('order_list', pk=miscalculation.pk)
    miscalculation = MiscalculationMob.objects.filter(user=user, active=False).order_by('-pk')
    form_miscalculation = MiscalculationForm(initial={
        'status': 1,
        'date': datetime.datetime.now(),
    })
    context = {
        'miscalculation': miscalculation,
        'form_miscalculation': form_miscalculation,
    }
    return render(request, 'miscalculation_history.html', context)


def welcome_page(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('login', )

    if request.method == 'POST':
        order = Order.objects.create(active=False)
        order.user = user
        order.date = datetime.datetime.now()
        order.save()
        miscalculation = MiscalculationMob.objects.create(active=False)
        miscalculation.user = user
        miscalculation.date = datetime.datetime.now()
        miscalculation.orders.add(order)
        miscalculation.save()
        return redirect('order', order_pk=order.pk, miscalc_pk=miscalculation.pk, form='None')
    return render(request, 'welcome_page.html')


def calculation_form(request):
    if request.method == 'POST':
        order_pk = request.POST.get('order_pk')
        miscalc_pk = request.POST.get('miscalc_pk')

        profile = Profile.objects.get(pk=request.POST.get('profile'))
        fittings = Fittings.objects.get(pk=request.POST.get('fitting'))
        filling = Aggregate.objects.get(pk=request.POST.get('filling'))

        one_sash_width = request.POST.get('one-sash-width')
        one_sash_length = request.POST.get('one-sash-length')
        if one_sash_width and one_sash_length and int(one_sash_width) > 0 and int(one_sash_length) > 0:
            window = request.POST.get('one-sash-select')
            calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=window,
                         width=one_sash_width, length=one_sash_length, sash=1)

            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')

        two_sash_width = request.POST.get('two-sash-width')
        two_sash_length = request.POST.get('two-sash-length')
        if two_sash_width and two_sash_length and int(two_sash_width) > 0 and int(two_sash_length) > 0:
            window_1 = request.POST.get('two-sash-select-1')
            window_2 = request.POST.get('two-sash-select-2')
            window = f'{window_1}_{window_2}'
            calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=window,
                         width=two_sash_width, length=two_sash_length, sash=2)
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')

        three_sash_width = request.POST.get('three-sash-width')
        three_sash_length = request.POST.get('three-sash-length')
        if three_sash_width and three_sash_length and int(three_sash_width) > 0 and int(three_sash_length) > 0:
            window_1 = request.POST.get('three-sash-select-1')
            window_2 = request.POST.get('three-sash-select-2')
            window_3 = request.POST.get('three-sash-select-3')
            window = f'{window_1}_{window_2}_{window_3}'
            calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=window,
                         width=three_sash_width, length=three_sash_length, sash=3)
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')

        four_sash_width = request.POST.get('four-sash-width')
        four_sash_length = request.POST.get('four-sash-length')
        if four_sash_width and four_sash_length and int(four_sash_width) > 0 and int(four_sash_length) > 0:
            window_1 = request.POST.get('four-sash-select-1')
            window_2 = request.POST.get('four-sash-select-2')
            window_3 = request.POST.get('four-sash-select-3')
            window_4 = request.POST.get('four-sash-select-4')
            window = f'{window_1}_{window_2}_{window_3}_{window_4}'
            calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=window,
                         width=four_sash_width, length=four_sash_length, sash=4)
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')

        door_width = request.POST.get('door-width')
        door_length = request.POST.get('door-length')
        if door_width and door_length and int(door_width) > 0 and int(door_length) > 0:
            door = request.POST.get('door-select')
            door = f'{door}'
            calc_windows(order_id=order_pk, profile=profile, fittings=fittings, filling=filling, window_type=door,
                         width=door_width, length=door_length, sash=0)
            return redirect('order', miscalc_pk=miscalc_pk, order_pk=order_pk, form='products')



    else:
        return HttpResponse('Invalid request method')


def add_cost_miscalculation(request):
    if request.method == 'GET':
        miscalc_pk = request.GET.get('miscalc_pk')
        cost = request.GET.get('add-cost-input')
        add_hidden_cost(miscalc_pk, cost)
        response_data = {'status': 'success', 'message': 'Cost added successfully.'}
        return JsonResponse(response_data, status=200)


def reset_hidden_cost_miscalculation(request, pk):
    if request.method == 'GET':
        miscalculation = MiscalculationMob.objects.get(pk=pk)
        miscalculation.hidden_cost = 0
        miscalculation.save()
        return redirect('order_list', pk)


def commercial_offer(request, pk):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('login', )

    miscalculation = MiscalculationMob.objects.get(pk=pk)
    orders = miscalculation.orders.all()
    context = {
        'miscalculation': miscalculation,
        'orders': orders,
    }
    return render(request, 'commercial_offer.html', context)

def contract(request, pk):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('login', )

    # miscalculation = MiscalculationMob.objects.get(pk=pk)
    contract = Contract.objects.get(pk=pk)
    # client = miscalculation.client

    context = {
        # 'miscalculation': miscalculation,
        # 'client': client,
        'contract': contract,
    }
    return render(request, 'contract.html', context)

def contract_offer(request, pk):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return redirect('login', )

    miscalculation = MiscalculationMob.objects.get(pk=pk)
    orders = miscalculation.orders.all()
    client = miscalculation.client
    contract = miscalculation.contract

    contract.cost = miscalculation.total_cost
    try:
        contract.finish_cost = contract.cost - contract.deposit
    except:
        contract.finish_cost = miscalculation.total_cost

    contract.cost = round(contract.cost, 2)
    contract.finish_cost = round(contract.finish_cost, 2)
    contract.save()
    miscalculation.save()

    try:
        amount = num2words(contract.finish_cost, lang='ru', to='currency', currency='RUB')
    except:
        amount = "ноль"


    context = {
        'miscalculation': miscalculation,
        'orders': orders,
        'client': client,
        'contract': contract,
        'amount': amount,
    }
    return render(request, 'contract_offer.html', context)


def send_to_manager(request, pk):
    miscalculation = MiscalculationMob.objects.get(pk=pk)
    miscalculation.status = "отправить на просчёт"
    miscalculation.save()
    return redirect('miscalculation')

def save_passport(request, pk, passport_pk):
    passport = PassportDetails.objects.get(pk=passport_pk)
    passport_form = PassportDetailsForm(request.POST, instance=passport)
    if passport_form.is_valid():
        # Сохраняем форму, вызывая метод save()
        passport = passport_form.save()
        passport.save()
        miscalculation = MiscalculationMob.objects.get(pk=pk)

        miscalculation.client.passport_details = passport
        miscalculation.client.save()
        # Теперь объект PassportDetails сохранен в базе данных
        # Вы можете добавить дополнительные действия или перенаправить пользователя на другую страницу
        return redirect('order_list', pk=pk)

def save_contract(request, pk,contract_pk):
    contract = Contract.objects.get(pk=contract_pk)
    contract_form = ContractForm(request.POST, instance=contract)
    if contract_form.is_valid():
        # Сохраняем форму, вызывая метод save()
        contract = contract_form.save()
        contract.date = datetime.datetime.now()
        contract.save()
        miscalculation = MiscalculationMob.objects.get(pk=pk)
        miscalculation.contract = contract
        miscalculation.contract.passport_details = miscalculation.client.passport_details
        miscalculation.contract.save()
        miscalculation.save()
        return redirect('order_list',pk=pk)

def confirm_order(request, pk):
    miscalculation = MiscalculationMob.objects.get(pk=pk)
    miscalculation.status = "выполнен"
    miscalculation.save()
    return redirect('miscalculation')


class MiscalculationViewSet(viewsets.ModelViewSet):
    queryset = MiscalculationMob.objects.all().order_by('-id')
    serializer_class = MiscalculationMobSerializer
    http_method_names = ['get', 'patch', 'post']

    def list(self, request):
        queryset = MiscalculationMob.objects.all().order_by('-id')
        serializer = MiscalculationMobSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = MiscalculationMob.objects.all().order_by('-id')
        lamination = get_object_or_404(queryset, pk=pk)
        serializer = MiscalculationMobSerializer(lamination)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"data": serializer.data})
