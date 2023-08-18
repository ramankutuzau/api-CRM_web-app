from calculation.models import WindowDiscountMarkups, ExchangeRates
from .models import *
import pandas as pd
from config.settings import BASE_DIR

def add_windowsill_calc(windowsill_calc, windowsill, windowsill_color, windowsill_width, windowsill_count, length):
    try:
        sum_windowsill_byn = round((windowsill.price_input * (
                (float(windowsill_width.name) * length) / 1000000)) * windowsill_count, 2)
        # sum_windowsill_currency = round((windowsill.price_in_currency * (
        #         (float(windowsill_width.name) * length) / 1000000)) * windowsill_count, 2)
        square_meter = ((float(windowsill_width.name) * length) / 1000000) * windowsill_count
        linear_meter = (length / 1000) * windowsill_count

        if windowsill_count > 0:
            sum_windowsill_byn = sum_windowsill_byn * windowsill_count
            # sum_windowsill_currency = sum_windowsill_currency * windowsill_count
        windowsill_calc.sum_windowsill_byn = round(sum_windowsill_byn, 2)
        # windowsill_calc.sum_windowsill_currency = round(sum_windowsill_currency, 2)
        windowsill_calc.square_meter = round(square_meter, 2)
        windowsill_calc.linear_meter = round(linear_meter, 2)

        windowsill_calc.windowsill_color = windowsill_color
        windowsill_calc.windowsill = windowsill
        windowsill_calc.windowsill_width = windowsill_width
        windowsill_calc.windowsill_count = windowsill_count
        windowsill_calc.length = length
    except:
        windowsill_calc.sum_windowsill_byn = 0.0
        windowsill_calc.square_meter = 0.0
        windowsill_calc.linear_meter = 0.0
        windowsill_calc.windowsill_color = None
        windowsill_calc.windowsill = None




def add_plug_calc(windowsill_calc, windowsill_plug, windowsill_plug_count):
    try:
        windowsill_calc.sum_plug_byn = windowsill_plug.price_input * windowsill_plug_count
        windowsill_calc.windowsill_plug = windowsill_plug
        windowsill_calc.windowsill_plug_count = windowsill_plug_count
    except:
        windowsill_calc.sum_plug_byn = 0.0


def add_connection_calc(windowsill_calc, windowsill_connection, windowsill_connection_count):
    try:
        windowsill_calc.sum_connection_byn = windowsill_connection.price_input * windowsill_connection_count
        # windowsill_calc.sum_connection_currency = windowsill_connection.price_in_currency * windowsill_connection_count
        windowsill_calc.windowsill_connection = windowsill_connection
        windowsill_calc.windowsill_connection_count = windowsill_connection_count
    except:
        windowsill_calc.sum_connection_byn = 0.0
        # windowsill_calc.sum_connection_currency = 0.0


def calc_windowsill_sum(windowsill_calc):
    windowsill_calc.sum_in_byn = round(windowsill_calc.sum_windowsill_byn + windowsill_calc.sum_plug_byn + windowsill_calc.sum_connection_byn,2)
    # windowsill_calc.sum_in_currency = windowsill_calc.sum_windowsill_currency + windowsill_calc.sum_plug_currency + windowsill_calc.sum_connection_currency


def calc_windowsill(order_id, windowsill, windowsill_color, windowsill_width, windowsill_count, windowsill_plug,
                    windowsill_plug_count,
                    windowsill_connection, windowsill_connection_count, length):
    windowsill_calc = WindowsillCalcMob.objects.create(order_id=order_id)

    add_windowsill_calc(windowsill_calc, windowsill, windowsill_color, windowsill_width, windowsill_count, length)
    add_plug_calc(windowsill_calc, windowsill_plug, windowsill_plug_count)
    add_connection_calc(windowsill_calc, windowsill_connection, windowsill_connection_count)

    calc_windowsill_sum(windowsill_calc=windowsill_calc)
    windowsill_calc.save()


def add_low_tides_calc(low_tides_calc, low_tides, low_tides_type, low_tides_color, low_tides_width, low_tides_count,
                       low_tides_length):
    try:
        if (low_tides_width > 0) and (low_tides_length > 0):
            low_tides_width = low_tides_width + 55
            sum_low_tides_byn = round((low_tides.price_input * (
                    (float(low_tides_width) * low_tides_length) / 1000000)) * low_tides_count, 2)
            # sum_low_tides_currency = round((low_tides.price_in_currency * (
            #         (float(low_tides_width) * low_tides_length) / 1000000)) * low_tides_count, 2)
            square_meter = ((float(low_tides_width) * low_tides_length) / 1000000) * low_tides_count
            linear_meter = (low_tides_length / 1000) * low_tides_count

            if low_tides_count > 0:
                sum_low_tides_byn = sum_low_tides_byn * low_tides_count
                # sum_low_tides_currency = sum_low_tides_currency * low_tides_count
            low_tides_calc.sum_low_tides_byn = round(sum_low_tides_byn,2)
            # low_tides_calc.sum_low_tides_currency = sum_low_tides_currency
            low_tides_calc.square_meter = round(square_meter, 2)
            low_tides_calc.linear_meter = round(linear_meter, 2)

            low_tides_calc.low_tides_color = low_tides_color
            low_tides_calc.low_tides_type = low_tides_type
            low_tides_calc.low_tides = low_tides
            low_tides_calc.low_tides_width = low_tides_width
            low_tides_calc.low_tides_count = low_tides_count
            low_tides_calc.length = low_tides_length
    except:
        low_tides_calc.sum_low_tides_byn = 0.0
        # low_tides_calc.sum_low_tides_currency = 0.0
        low_tides_calc.square_meter = 0.0
        low_tides_calc.linear_meter = 0.0
        low_tides_calc.low_tides_color = None
        low_tides_calc.low_tides_type = None


def add_plug_low_tides_calc(low_tides_calc, low_tides_plug, low_tides_plug_count):
    try:
        low_tides_calc.sum_plug_byn = low_tides_plug.price_input * low_tides_plug_count
        # low_tides_calc.sum_plug_currency = low_tides_plug.price_in_currency * low_tides_plug_count
        low_tides_calc.low_tides_plug = low_tides_plug
        low_tides_calc.low_tides_plug_count = low_tides_plug_count
    except:
        low_tides_calc.sum_plug_byn = 0.0
        # low_tides_calc.sum_plug_currency = 0.0


def add_connection_low_tides_calc(low_tides_calc, low_tides_connection, low_tides_connection_count):
    try:
        low_tides_calc.sum_connection_byn = low_tides_connection.price_input * low_tides_connection_count
        # low_tides_calc.sum_connection_currency = low_tides_connection.price_in_currency * low_tides_connection_count
        low_tides_calc.low_tides_connection = low_tides_connection
        low_tides_calc.low_tides_connection_count = low_tides_connection_count
    except:
        low_tides_calc.sum_connection_byn = 0.0
        # low_tides_calc.sum_connection_currency = 0.0


def calc_low_tides_sum(low_tides_calc):
    low_tides_calc.sum_in_byn = round(low_tides_calc.sum_low_tides_byn + low_tides_calc.sum_plug_byn + low_tides_calc.sum_connection_byn,2)
    # low_tides_calc.sum_in_currency = low_tides_calc.sum_low_tides_currency + low_tides_calc.sum_plug_currency + low_tides_calc.sum_connection_currency


def calc_low_tides(order_id, low_tides, low_tides_color, low_tides_width, low_tides_count, low_tides_plug,
                   low_tides_plug_count, low_tides_type,
                   low_tides_connection, low_tides_connection_count, length):
    low_tides_calc = LowTidesCalcMob.objects.create(order_id=order_id)

    add_low_tides_calc(low_tides_calc=low_tides_calc, low_tides=low_tides, low_tides_type=low_tides_type,
                       low_tides_color=low_tides_color, low_tides_width=low_tides_width,
                       low_tides_count=low_tides_count, low_tides_length=length)
    add_plug_low_tides_calc(low_tides_calc=low_tides_calc, low_tides_plug=low_tides_plug,
                            low_tides_plug_count=low_tides_plug_count)
    add_connection_low_tides_calc(low_tides_calc=low_tides_calc, low_tides_connection=low_tides_connection,
                                  low_tides_connection_count=low_tides_connection_count)
    calc_low_tides_sum(low_tides_calc=low_tides_calc)
    low_tides_calc.save()


def calc_visors(order_id, visors, visors_color, width_1,width_2,width_3, length, count):
    width = width_1 + width_2 + width_3 + 50
    if (width > 0) and (length > 0):
        price_in_byn = visors.price_input
        # price_in_currency = visors.price_in_currency

        # width = width + 55.0  # + 55 мм

        sum_byn = price_in_byn * ((width * length) / 1000000)
        # sum_currency = price_in_currency * ((width * length) / 1000000)
        square_meter = (width * length) / 1000000
        linear_meter = length / 1000

        if count > 0:
            sum_byn = sum_byn * count
            # sum_currency = sum_currency * count
            square_meter = square_meter * count
            linear_meter = linear_meter * count

        sum_byn = round(sum_byn, 2)
        # sum_currency = round(sum_currency, 2)

        square_meter = round(square_meter, 2)
        linear_meter = round(linear_meter, 2)
        visors_calc = VisorsCalcMob.objects.create(order_id=order_id,
                                                visors=visors,
                                                visors_color=visors_color,
                                                width=width,
                                                width_1=width_1, width_2=width_2, width_3=width_3,
                                                length=length,
                                                count=count,
                                                price_in_byn=sum_byn,
                                                # price_in_currency=sum_currency,
                                                square_meter=square_meter,
                                                linear_meter=linear_meter)

        return visors_calc


def calc_additional_profile(order_id, additional_profile, lamination, count):
    if (count > 0):
        price_in_byn = additional_profile.price_in_byn
        # price_in_currency = additional_profile.price_in_currency
        sum_byn = price_in_byn * count
        # sum_currency = price_in_currency * count

        sum_byn = round(sum_byn, 2)
        # sum_currency = round(sum_currency, 2)
        additional_profile = AdditionalProfileCalcMob.objects.create(order_id=order_id,
                                                                  additional_profile=additional_profile,
                                                                  lamination=lamination,
                                                                  count=count,
                                                                  price_in_byn=sum_byn,
                                                                  )
        # price_in_currency=sum_currency)

        return additional_profile


def calc_connection_profile(order_id, connection_profile, count):
    if count > 0:
        price_in_byn = connection_profile.price_in_byn
        # price_in_currency = connection_profile.price_in_currency
        sum_byn = price_in_byn * count
        # sum_currency = price_in_currency * count

        sum_byn = round(sum_byn, 2)
        # sum_currency = round(sum_currency, 2)
        connection_profile = ConnectionProfileCalcMob.objects.create(order_id=order_id,
                                                                  connection_profile=connection_profile,
                                                                  count=count,
                                                                  price_in_byn=sum_byn,
                                                                  )
        # price_in_currency=sum_currency)

        return connection_profile


def calc_flashing(order_id, flashing, flashing_color, width, length, count):

    if (width > 0) and (length > 0):

        price_in_byn = flashing.price_input
        # price_in_currency = flashing.price_in_currency

        width = width + 55.0  # + 55 мм
        sum = 0
        if flashing.type == 0:  # metal -> m2
            sum = price_in_byn * ((width * length) / 1000000)
        elif flashing.type == 1:
            sum = price_in_byn * (length / 1000000)

        square_meter = (width * length) / 1000000
        linear_meter = length / 1000

        if count > 0:
            sum = sum * count
            # sum_currency = sum_currency * count
            square_meter = square_meter * count
            linear_meter = linear_meter * count

        sum = round(sum, 2)
        # sum_currency = round(sum_currency, 2)

        square_meter = round(square_meter, 2)
        linear_meter = round(linear_meter, 2)
        flashing_calc = FlashingCalcMob.objects.create(order_id=order_id,
                                                    flashing=flashing,
                                                    flashing_color=flashing_color,
                                                    width=width,
                                                    length=length,
                                                    count=count,
                                                    price_in_byn=sum,
                                                    # price_in_currency=sum_currency,
                                                    square_meter=square_meter,
                                                    linear_meter=linear_meter)

        return flashing_calc


def calc_casing(order_id, casing, casing_color, width, length, count):

    casing_price = CasingPrice.objects.get(casing=casing, width_1__lte=width, width_2__gte=width)
    price_input_casing = casing_price.price_input

    if (width > 0) and (length > 0):

        price_in_byn = price_input_casing
        # price_in_currency = casing.price_in_currency

        sum_byn = price_in_byn * ((width * length) / 1000000)
        # sum_currency = price_in_currency * ((width * length) / 1000000)

        square_meter = (width * length) / 1000000
        linear_meter = length / 1000

        if count > 0:
            sum_byn = sum_byn * count
            # sum_currency = sum_currency * count
            square_meter = square_meter * count
            linear_meter = linear_meter * count

        sum_byn = round(sum_byn, 2)
        # sum_currency = round(sum_currency, 2)

        square_meter = round(square_meter, 2)
        linear_meter = round(linear_meter, 2)
        casing_calc = CasingCalcMob.objects.create(order_id=order_id,
                                                casing=casing,
                                                casing_color=casing_color,
                                                width=width,
                                                length=length,
                                                count=count,
                                                price_in_byn=sum_byn,
                                                # price_in_currency=sum_currency,
                                                square_meter=square_meter,
                                                linear_meter=linear_meter)

        return casing_calc


def calc_slopes_of_metal(order_id, slopes_of_metal, slopes_of_metal_color, width, length, count):
    if (width > 0) and (length > 0):

        price_in_byn = slopes_of_metal.price_in_byn
        # price_in_currency = slopes_of_metal.price_in_currency

        sum_byn = price_in_byn * ((width * length) / 1000000)
        # sum_currency = price_in_currency * ((width * length) / 1000000)
        square_meter = (width * length) / 1000000
        linear_meter = length / 1000

        if count > 0:
            sum_byn = sum_byn * count
            # sum_currency = sum_currency * count
            square_meter = square_meter * count
            linear_meter = linear_meter * count

        sum_byn = round(sum_byn, 2)
        # sum_currency = round(sum_currency, 2)

        square_meter = round(square_meter, 2)
        linear_meter = round(linear_meter, 2)
        slopes_of_metal_calc = SlopesOfMetalCalcMob.objects.create(order_id=order_id,
                                                                slopes_of_metal=slopes_of_metal,
                                                                slopes_of_metal_color=slopes_of_metal_color,
                                                                width=width,
                                                                length=length,
                                                                count=count,
                                                                price_in_byn=sum_byn,
                                                                # price_in_currency=sum_currency,
                                                                square_meter=square_meter,
                                                                linear_meter=linear_meter)

        return slopes_of_metal_calc


def calc_internal_slopes(order_id, internal_slopes, internal_slopes_color, width, length, count):
    if (width > 0) and (length > 0):

        price_in_byn = internal_slopes.price_in_byn
        # price_in_currency = internal_slopes.price_in_currency

        sum_byn = price_in_byn * ((width * length) / 1000000)
        # sum_currency = price_in_currency * ((width * length) / 1000000)
        square_meter = (width * length) / 1000000
        linear_meter = length / 1000

        if count > 0:
            sum_byn = sum_byn * count
            # sum_currency = sum_currency * count
            square_meter = square_meter * count
            linear_meter = linear_meter * count

        sum_byn = round(sum_byn, 2)
        # sum_currency = round(sum_currency, 2)

        square_meter = round(square_meter, 2)
        linear_meter = round(linear_meter, 2)
        internal_slopes_calc = InternalSlopesCalcMob.objects.create(order_id=order_id,
                                                                 internal_slopes=internal_slopes,
                                                                 internal_slopes_color=internal_slopes_color,
                                                                 width=width,
                                                                 length=length,
                                                                 count=count,
                                                                 price_in_byn=sum_byn,
                                                                 # price_in_currency=sum_currency,
                                                                 square_meter=square_meter,
                                                                 linear_meter=linear_meter)

        return internal_slopes_calc


def calc_mounting_materials(order_id, mounting_materials, count):
    if count > 0:
        price_in_byn = mounting_materials.price_in_byn
        # price_in_currency = mounting_materials.price_in_currency

        sum_byn = price_in_byn
        # sum_currency = price_in_currency

        sum_byn = sum_byn * count
        # sum_currency = sum_currency * count

        sum_byn = round(sum_byn, 2)
        # sum_currency = round(sum_currency, 2)

        mounting_materials_calc = MountingMaterialsCalcMob.objects.create(order_id=order_id,
                                                                       mounting_materials=mounting_materials,
                                                                       count=count,
                                                                       price_in_byn=sum_byn,
                                                                       )
        # price_in_currency=sum_currency)

        return mounting_materials_calc


def calc_works(order_id, works, count):
    if count > 0:
        price_in_byn = works.price_in_byn
        # price_in_currency = works.price_in_currency

        sum_byn = price_in_byn
        # sum_currency = price_in_currency

        sum_byn = sum_byn * count
        # sum_currency = sum_currency * count

        sum_byn = round(sum_byn, 2)
        # sum_currency = round(sum_currency, 2)

        works_calc = WorksCalcMob.objects.create(order_id=order_id,
                                              works=works,
                                              count=count,
                                              price_in_byn=sum_byn,
                                              )
        # price_in_currency=sum_currency)

    return works_calc


def calc_other(order_id, other, price):
    price = round(price, 2)
    other_calc = OtherCalcMob.objects.create(order_id=order_id,
                                          other=other,
                                          price=price, )

    return other_calc


def calc_materials(order):
    sum_byn = 0.0

    windowsill_calc = WindowsillCalcMob.objects.filter(order_id=order.pk)
    for el in windowsill_calc:
        sum_byn = sum_byn + el.sum_in_byn
        order.windowsill_calc.add(el)
        # sum_currency = sum_currency + el.sum_in_currency

    low_tides_calc = LowTidesCalcMob.objects.filter(order_id=order.pk)
    for el in low_tides_calc:
        sum_byn = sum_byn + el.sum_in_byn
        order.low_tides_calc.add(el)
        # sum_currency = sum_currency + el.sum_in_currency

    visors_calc = VisorsCalcMob.objects.filter(order_id=order.pk)
    for el in visors_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.visors_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    additional_profile_calc = AdditionalProfileCalcMob.objects.filter(order_id=order.pk)
    for el in additional_profile_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.additional_profile_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    connection_profile_calc = ConnectionProfileCalcMob.objects.filter(order_id=order.pk)
    for el in connection_profile_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.additional_profile_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    flashing_calc = FlashingCalcMob.objects.filter(order_id=order.pk)
    for el in flashing_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.flashing_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    casing_calc = CasingCalcMob.objects.filter(order_id=order.pk)
    for el in casing_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.casing_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    slopes_of_metal_calc = SlopesOfMetalCalcMob.objects.filter(order_id=order.pk)
    for el in slopes_of_metal_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.slopes_of_metal_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    internal_slopes_calc = InternalSlopesCalcMob.objects.filter(order_id=order.pk)
    for el in internal_slopes_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.internal_slopes_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    mounting_materials_calc = MountingMaterialsCalcMob.objects.filter(order_id=order.pk)
    for el in mounting_materials_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.mounting_materials_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    order.sum_materials_byn = round(sum_byn, 2)
    # order.sum_materials_currency = round(sum_currency, 2)


def calc_order_works(order):
    sum_byn = 0.0
    # sum_currency = 0.0

    works_calc = WorksCalcMob.objects.filter(order_id=order.pk)
    for el in works_calc:
        sum_byn = sum_byn + el.price_in_byn
        order.works_calc.add(el)
        # sum_currency = sum_currency + el.price_in_currency

    order.sum_works_byn = round(sum_byn, 2)
    # order.sum_works_currency = round(sum_currency, 2)
    order.save()


def calc_order_other(order):
    sum_byn = 0.0

    other_calc = OtherCalcMob.objects.filter(order_id=order.pk)
    for el in other_calc:
        sum_byn = sum_byn + el.price
        order.other_calc.add(el)

    order.sum_other_byn = round(sum_byn, 2)
    order.save()


def calc_order_windows(order):
    sum_byn = 0.0
    # sum_currency = 0.0

    windows_1_calc = Windows1Calc.objects.filter(order_id=order.pk)
    for el in windows_1_calc:
        try:
            sum_byn = sum_byn + el.price_in_byn
            order.windows_1_calc.add(el)
        except:
            sum_byn = 0
        # sum_currency = sum_currency + el.price_in_currency

    windows_2_calc = Windows2Calc.objects.filter(order_id=order.pk)
    for el in windows_2_calc:
        try:
            sum_byn = sum_byn + el.price_in_byn
            order.windows_2_calc.add(el)

        except:
            sum_byn = 0
        # sum_currency = sum_currency + el.price_in_currency

    windows_3_calc = Windows3Calc.objects.filter(order_id=order.pk)
    for el in windows_3_calc:
        try:
            sum_byn = sum_byn + el.price_in_byn
            order.windows_3_calc.add(el)

        except:
            sum_byn = 0
        # sum_currency = sum_currency + el.price_in_currency

    windows_4_calc = Windows4Calc.objects.filter(order_id=order.pk)
    for el in windows_4_calc:
        try:
            sum_byn = sum_byn + el.price_in_byn
            order.windows_4_calc.add(el)

        except:
            sum_byn = 0
        # sum_currency = sum_currency + el.price_in_currency

    door_calc = DoorCalc.objects.filter(order_id=order.pk)
    for el in door_calc:
        try:
            sum_byn = sum_byn + el.price_in_byn
            order.door_calc.add(el)
        except:
            sum_byn = 0
        # sum_currency = sum_currency + el.price_in_currency

    order.sum_windows_byn = round(sum_byn, 2)
    # order.sum_windows_currency = round(sum_currency, 2)
    order.save()


def calc_order(miscalc_pk):
    try:
        orders_id = MiscalculationMob.objects.filter(pk=miscalc_pk).values_list('orders', flat=True)
        for el in orders_id:
            order = Order.objects.get(pk=el)
            calc_order_windows(order)
            calc_materials(order)
            calc_order_works(order)
            calc_order_other(order)

            order.sum_byn = round(order.sum_materials_byn + order.sum_works_byn + order.sum_windows_byn + order.sum_other_byn,
                                  2)
            order.save()

        miscalculation = MiscalculationMob.objects.get(pk=miscalc_pk)
        orders_id = MiscalculationMob.objects.filter(pk=miscalc_pk).values_list('orders', flat=True)
        orders = []
        for el in orders_id:
            orders.append(Order.objects.get(pk=el))
        sum = 0
        for el in orders:
            sum = round(sum + el.sum_byn, 2)
        miscalculation.total_cost = sum
        miscalculation.save()
    except Order.DoesNotExist:
        pass

def calc_window_disc(order_id, profile, fittings, filling, window_type, price, sash):
    if profile.name == "Start 60":
        exchange_rates = ExchangeRates.objects.get(name='RUB')
    # elif profile.name == "Brusbox 60-3":
    #     exchange_rates = ExchangeRates.objects.get(name='USD')

    try:
        window_disc_markup = WindowDiscountMarkups.objects.get(profile_id=profile, fittings_id=fittings)

        discount = window_disc_markup.discount

        markup = window_disc_markup.markups_diler

        in_percent = window_disc_markup.markups_diler_in_percent

        disc_window = (float(price) / 100) * discount  # discount window

        window_input_price = (float(price) - disc_window)  # price - discount

        if in_percent:
            window_price_with_markup = window_input_price + (window_input_price / 100 * markup)  # + MARKUP
        else:
            window_price_with_markup = window_input_price + markup  # + MARKUP

        price_in_byn = round(window_price_with_markup, 2)  # round output price

    except WindowDiscountMarkups.DoesNotExist:
        price_in_byn = round(price, 2)
    try:
        price_in_byn = round(exchange_rates.value * float(price_in_byn), 2)  # price in BYN
    except:
        pass


    if sash == 0:  # is DOOR
        window_calc = DoorCalc.objects.create(order_id=order_id,
                                              profile=profile,
                                              fittings=fittings,
                                              filling=filling,
                                              type=window_type,
                                              price_in_byn=price_in_byn, )

    if sash == 1:
        window_calc = Windows1Calc.objects.create(order_id=order_id,
                                                  profile=profile,
                                                  fittings=fittings,
                                                  filling=filling,
                                                  type=window_type,
                                                  price_in_byn=price_in_byn, )
    elif sash == 2:
        types = window_type.split("_")
        window_calc = Windows2Calc.objects.create(order_id=order_id,
                                                  profile=profile,
                                                  fittings=fittings,
                                                  filling=filling,
                                                  type_1=types[0],
                                                  type_2=types[1],
                                                  price_in_byn=price_in_byn, )
    elif sash == 3:
        types = window_type.split("_")
        window_calc = Windows3Calc.objects.create(order_id=order_id,
                                                  profile=profile,
                                                  fittings=fittings,
                                                  filling=filling,
                                                  type_1=types[0],
                                                  type_2=types[1],
                                                  type_3=types[2],
                                                  price_in_byn=price_in_byn, )

    elif sash == 4:
        types = window_type.split("_")
        window_calc = Windows4Calc.objects.create(order_id=order_id,
                                                  profile=profile,
                                                  fittings=fittings,
                                                  filling=filling,
                                                  type_1=types[0],
                                                  type_2=types[1],
                                                  type_3=types[2],
                                                  type_4=types[3],
                                                  price_in_byn=price_in_byn, )

    return window_calc


def sorted_windows_str(window):
    windows_str_output = []
    for el in window.split("_"):
        if (el == 'turning-left') or (el == 'turning-right'):
            el = 'turning'
        windows_str_output.append(el)
    return sorted(windows_str_output)


def get_price_door(profile, filling, fittings, folder, width, length):

    file_path = f"{BASE_DIR}/windows_tables/{folder}/{profile.name}_{fittings.name}_door_{filling.name}.xlsx"
    try:
        df = pd.DataFrame(pd.read_excel(file_path))
        return df.loc[length][width]
    except:
        return 0.0

def get_price_window_1_sash(profile, filling, fittings,folder, window, width, length):
    sorted_windows = sorted_windows_str(window)
    file_path = f"{BASE_DIR}/windows_tables/{folder}/{profile.name}_{fittings.name}_{sorted_windows[0]}_{filling.name}.xlsx"
    print(file_path)
    try:
        df = pd.DataFrame(pd.read_excel(file_path))
        return df.loc[length][width]
    except:
        return 0.0


def get_price_window_2_sash(profile, filling, fittings,folder, window, width, length):
    sorted_windows = sorted_windows_str(window)
    file_path = f"{BASE_DIR}/windows_tables/{folder}/{profile.name}_{fittings.name}_{sorted_windows[0]}_{sorted_windows[1]}_{filling.name}.xlsx"
    print(file_path)

    try:
        df = pd.DataFrame(pd.read_excel(file_path))
        return df.loc[length][width]
    except:
        return 0.0


def get_price_window_3_sash(profile, filling, fittings,folder, window, width, length):
    sorted_windows = sorted_windows_str(window)
    file_path = f"{BASE_DIR}/windows_tables/{folder}/{profile.name}_{fittings.name}_{sorted_windows[0]}_{sorted_windows[1]}_{sorted_windows[2]}_{filling.name}.xlsx"

    try:
        df = pd.DataFrame(pd.read_excel(file_path))
        return df.loc[length][width]
    except:
        return 0.0


def get_price_window_4_sash(profile, filling, fittings,folder, window, width, length):
    sorted_windows = sorted_windows_str(window)
    file_path = f"{BASE_DIR}/windows_tables/{folder}/{profile.name}_{fittings.name}_{sorted_windows[0]}_{sorted_windows[1]}_{sorted_windows[2]}_{sorted_windows[3]}_{filling.name}.xlsx"
    try:
        df = pd.DataFrame(pd.read_excel(file_path))
        return df.loc[length][width]
    except:
        return 0.0


def calc_width_length(profile,width, length, start):
    if profile.name == 'Brusbox 60-3':
        step = 100
    elif profile.name == 'Start 60':
        step = 50
    width = int(width)
    length = int(length)
    if width % step > 0:
        width_calc = width + (step - (width % step))
    else:
        width_calc = int(width)
    if length % step > 0:
        length_calc = length + (step - (length % step))
    else:
        length_calc = int(length)

    length_row = ((length_calc - start) / step)
    return {'width_calc': width_calc, 'length_calc': length_calc, 'length_row': length_row}


def calc_windows(order_id, profile, fittings, filling, window_type, width, length, sash):
    folder = f'{profile.name}_{fittings.name}_{filling.name}'
    price = None
    result = None
    try:
        if sash == 0:  # door - id 0
            if profile.name == 'Start 60':
                start = 1000
            elif profile.name == 'Brusbox 60-3':
                start = 1800
            result = calc_width_length(profile=profile, width=width, length=length, start=start)

            price = get_price_door(profile=profile, length=result['length_row'], filling=filling,
                                   fittings=fittings,folder=folder,
                                   width=result['width_calc'])
        if sash == 1:
            start = 0
            if window_type == 'no-opening':
                start = 300
            elif (window_type == 'turning-right') or (window_type == 'turning-left'):
                start = 600
            elif window_type == 'transom':
                start = 400

            if profile.name == 'Brusbox 60-3':
                if window_type == 'no-opening':
                    start = 400
                elif (window_type == 'turning-right') or (window_type == 'turning-left'):
                    start = 700

            result = calc_width_length(profile=profile, width=width, length=length, start=start)

            price = get_price_window_1_sash(profile=profile, length=result['length_row'], filling=filling,
                                            fittings=fittings,folder=folder,
                                            window=window_type,
                                            width=result['width_calc'])
        elif sash == 2:
            if profile.name == 'Start 60':
                start = 600
            elif profile.name == 'Brusbox 60-3':
                start = 800
            result = calc_width_length(profile=profile, width=width, length=length, start=start)
            price = get_price_window_2_sash(profile=profile, length=result['length_row'], filling=filling,
                                            fittings=fittings,folder=folder,
                                            window=window_type,
                                            width=result['width_calc'])
        elif sash == 3:
            if profile.name == 'Start 60':
                start = 600
            elif profile.name == 'Brusbox 60-3':
                start = 800
            result = calc_width_length(profile=profile, width=width, length=length, start=start)
            price = get_price_window_3_sash(profile=profile, length=result['length_row'], filling=filling,
                                            fittings=fittings,folder=folder,
                                            window=window_type,
                                            width=result['width_calc'])
        elif sash == 4:
            if profile.name == 'Start 60':
                start = 600
            elif profile.name == 'Brusbox 60-3':
                start = 1100
            result = calc_width_length(profile=profile, width=width, length=length, start=start)
            price = get_price_window_4_sash(profile=profile, length=result['length_row'], filling=filling,
                                            fittings=fittings,folder=folder,
                                            window=window_type,
                                            width=result['width_calc'])
    except:
        price = 0
        result = {'width_calc': 0, 'length_calc': 0 }
    try:
        window_calc = calc_window_disc(order_id=order_id, profile=profile, fittings=fittings, window_type=window_type,
                               filling=filling, sash=sash, price=price)
    except:
        if sash == 1:
            window_calc = Windows1Calc.objects.create(filling=filling,profile=profile, fittings=fittings,order_id=order_id,type=window_type)
        elif sash == 2:
            types = window_type.split("_")
            window_calc = Windows2Calc.objects.create(filling=filling, profile=profile, fittings=fittings,order_id=order_id,type_1=types[0],type_2=types[1] )
        elif sash == 3:
            types = window_type.split("_")
            window_calc = Windows3Calc.objects.create(filling=filling, profile=profile, fittings=fittings,order_id=order_id,type_1=types[0],type_2=types[1],type_3=types[2] )
        elif sash == 4:
            types = window_type.split("_")

            window_calc = Windows4Calc.objects.create(filling=filling, profile=profile, fittings=fittings,order_id=order_id,type_1=types[0],type_2=types[1],type_3=types[2],type_4=types[3] )
        elif sash == 0:
            window_calc = DoorCalc.objects.create(filling=filling, profile=profile, fittings=fittings,order_id=order_id,type=window_type )

    window_calc.width = width
    window_calc.length = length
    window_calc.width_calc = result['width_calc']
    window_calc.length_calc = result['length_calc']

    window_calc.save()


def calc_total_cost(miscalculation, orders):
    sum = 0
    for el in orders:
        sum = round(sum + el.sum_byn, 2)
    miscalculation.total_cost = sum


def add_hidden_cost(miscalc_pk, cost):
    miscalculation = MiscalculationMob.objects.get(pk=miscalc_pk)

    orders = miscalculation.orders.all()
    count = 0
    for order in orders:
        count = count + order.windows_4_calc.count()
        count = count + order.windows_3_calc.count()
        count = count + order.windows_2_calc.count()
        count = count + order.windows_1_calc.count()
        count = count + order.door_calc.count()
    add_cost = float(cost) / count
    for el in orders:

        count = el.windows_4_calc.count()
        if count > 0:
            windows_4_calc = Windows4Calc.objects.get(order_id=el.pk)
            windows_4_calc.price_in_byn = windows_4_calc.price_in_byn + add_cost
            windows_4_calc.save()

        count = el.windows_3_calc.count()
        if count > 0:
            windows_3_calc = Windows3Calc.objects.get(order_id=el.pk)
            windows_3_calc.price_in_byn = windows_3_calc.price_in_byn + add_cost
            windows_3_calc.save()

        count = el.windows_2_calc.count()
        if count > 0:
            windows_2_calc = Windows2Calc.objects.get(order_id=el.pk)
            windows_2_calc.price_in_byn = windows_2_calc.price_in_byn + add_cost
            windows_2_calc.save()


        count = el.windows_1_calc.count()
        if count > 0:
            windows_1_calc = Windows1Calc.objects.get(order_id=el.pk)
            windows_1_calc.price_in_byn = windows_1_calc.price_in_byn + add_cost
            windows_1_calc.save()

        count = el.door_calc.count()
        if count > 0:
            door_calc = DoorCalc.objects.get(order_id=el.pk)
            door_calc.price_in_byn = door_calc.price_in_byn + add_cost
            door_calc.save()
    if add_cost > 0:
        miscalculation.hidden_cost = miscalculation.hidden_cost + float(cost)
        miscalculation.save()
