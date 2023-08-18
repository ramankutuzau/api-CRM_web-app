import base64
import datetime
import os

from PyPDF2 import PdfReader, PdfWriter
from django.http import HttpResponse

from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont



from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from calculation.models import Constructor
from config.settings import MEDIA_ROOT
from constructor.models import Profile, Fittings, Windowsill, WindowsillColor
from miscalculation.models import Miscalculation


def generate_offer(pk):
    constructor = Constructor.objects.get(pk=1)
    # miscalculation = Miscalculation.objects.get(pk=pk)

    buffer = BytesIO()

    # Создание документа PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter, bottomPadding=0, topMargin=30)  # Задайте нужное значение отступа сверху (например, 30)

    # Создание списка элементов для добавления в документ
    elements = []

    # Стили для текста
    styles = getSampleStyleSheet()
    # PRODUCTION
    # pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    # pdfmetrics.registerFont(TTFont('Arial-bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Arial', 'D:\\fonts\SF-Pro-Display-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-bold', 'D:\\fonts\SF-Pro-Display-Bold.ttf'))

    # Установка шрифта для стилей
    styles['Heading1'].fontName = 'Arial-bold'
    styles['Normal'].fontName = 'Arial'

    phone_style = ParagraphStyle(name='Phone', parent=styles['Normal'], fontName='Arial', fontSize=14)
    styles.add(phone_style)


    header_style = styles["Heading1"]
    header_style.fontSize = 16
    header_style.textColor = colors.black
    header_style.alignment = 1

    style_head_table = ParagraphStyle(name='Phone', parent=styles['Heading4'], fontName='Arial', fontSize=14)

    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    # Добавление изображения
    header_text = f"Коммерческое предложение №{constructor.pk} от {current_date}"
    data = [
        [
            Image(f"{MEDIA_ROOT}/logo_red.png", width=100, height=70),
            Paragraph(header_text, header_style)
        ]
    ]
    table = Table(data, colWidths=[letter[0] * 0.1, letter[0] * 0.9])
    # Установка стилей для таблицы и ячеек
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.white),  # Белый фон для левой колонки
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),  # Выравнивание текста в правой колонке по правому краю
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Выравнивание содержимого по центру вертикали
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),  # Шрифт Arial для всей таблицы
        ("FONTSIZE", (0, 0), (-1, -1), 12),  # Размер шрифта 14 для всей таблицы
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),  # Отступ снизу для всех ячеек
    ]))


    # Добавление таблицы в список элементов
    elements.append(table)


    # Получение изображения из base64-строки
    base64_image = constructor.final_image
    base64_data = base64_image.replace("data:image/png;base64,", "")
    image_data = base64.b64decode(base64_data)

    image_width = letter[0] * 0.9
    image_height = letter[1] * 0.35
    image_x = 0
    image_y = 0

    # Create a new canvas
    c = canvas.Canvas(f"{MEDIA_ROOT}/offers/template.png")

    c.saveState()

    image = Image(BytesIO(image_data), width=image_width, height=image_height)
    image.drawOn(c, image_x, image_y)

    # Restore the previously saved state of the canvas
    c.restoreState()

    # Save the canvas to a PDF file
    c.save()
    style_head = ParagraphStyle(name='Phone', parent=styles['Heading1'], fontName='Arial', fontSize=14)

    caption = Paragraph("Позиция №", style=style_head)
    elements.append(caption)

    elements.append(image)
    # elements.append(image)
    profile = Profile.objects.get(pk=constructor.window_calc.profile_id)
    fittings = Fittings.objects.get(pk=constructor.window_calc.fittings_id)
    data = [
        ["Тип изделия: ", f"{constructor.product_type.name}"],
        ["Профиль: ", f"{profile.name}"],
        ["Фурнитура: ", f"{fittings.name}"],
        ["Заполнение: ", f"{constructor.aggregate.name}"],
        ["Цена: ", f"{constructor.window_calc.price_output} BYN"],
    ]

    # Создание таблицы
    table = Table(data, colWidths=[130,300], rowHeights=20, hAlign="LEFT")

    # Установка стилей для таблицы и ячеек
    table.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, colors.black),  # Рамка для всей таблицы
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.black),  # Внутренняя сетка
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),  # Белый фон для ячеек
        ("LEFTPADDING", (0, 0), (-1, -1), 10),  # Отступ слева для содержимого ячеек
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Выравнивание текста по левому краю
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Выравнивание содержимого по центру вертикали
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),  # Шрифт Arial для всей таблицы
        ("FONTSIZE", (0, 0), (-1, -1), 12)  # Размер шрифта 12 для всей таблицы
    ]))

    # Добавление подписи "Изделие №" сверху таблицы

    elements.append(Spacer(1, 24))
    caption = Paragraph("Конфигурация окна", style=style_head_table)
    elements.append(caption)
    elements.append(Spacer(1, 4))
    elements.append(table)

    data = [
        ["Штапик: ", f"{constructor.shtapik.name}"],
        ["Створка: ", f"{constructor.sash.name}"],
        ["Горбыльки: ", f"{constructor.gorbylki.name}"],
        ["Ручки: ", f"{constructor.handles.name}"],
    ]
    if constructor.lamination:
        data += [
            ["Ламинация: ", f""],
            ["Тип ламинации: ", f"{constructor.lamination.type_lamination.name}"],
            ["Вид ламинации: ", f"{constructor.lamination.type_lamination1.name}"],
            ["Исполнение внутри: ", f"{constructor.lamination.seal_internal.name}"],
            ["Исполнение снаружи: ", f"{constructor.lamination.seal_outside.name}"],
            ["Исполнение основы детали: ", f"{constructor.lamination.seal_outside.name}"],
        ]
    if constructor.sealant:
        data += [
            ["Уплотнитель: ", f""],
            ["Цвет уплотнитель: ", f"{constructor.sealant.sealant_color.name}"],
            ["Исполнение снаружи: ", f"{constructor.sealant.sealant_inside.name}"],
            ["Исполнение внутри: ", f"{constructor.sealant.sealant_outside.name}"],
            ["Штапик: ", f"{constructor.sealant.sealant_outside.name}"],
        ]


    table = Table(data, colWidths=[160, 320], rowHeights=20, hAlign="LEFT")

    table.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, colors.black),  # Рамка для всей таблицы
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.black),  # Внутренняя сетка
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),  # Белый фон для ячеек
        ("LEFTPADDING", (0, 0), (-1, -1), 10),  # Отступ слева для содержимого ячеек
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Выравнивание текста по левому краю
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Выравнивание содержимого по центру вертикали
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),  # Шрифт Arial для всей таблицы
        ("FONTSIZE", (0, 0), (-1, -1), 12)  # Размер шрифта 12 для всей таблицы
    ]))



    elements.append(Spacer(1, 24))
    caption = Paragraph("Дополнительная конфигурация окна", style=style_head_table)
    elements.append(caption)
    elements.append(Spacer(1, 4))
    elements.append(table)

    style_head = ParagraphStyle(name='Phone', parent=styles['Heading1'], fontName='Arial', fontSize=14)

    if constructor.windowsills_calc.exists():
        data = [
            ["Название", "Цвет", "Заглушки", "Соед.", "Кол-во", "Цена"],
        ]
        windowsill_sum = 0
        for el in constructor.windowsills_calc.all():
            windowsill = Windowsill.objects.get(pk=el.windowsill_id)
            windowsill_color = WindowsillColor.objects.get(pk=el.color_id)
            data += [
                [windowsill.name, windowsill_color.name, el.plug, el.connector, el.count, f"{el.price_output} BYN"],
            ]
            windowsill_sum += el.price_output
        data += [
            ["Итог: ", "", "", "", "", f"{windowsill_sum} BYN"],
        ]

        table = Table(data, colWidths=[160, 120,70,60,60], rowHeights=20, hAlign="LEFT")

        table.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 1, colors.black),  # Рамка для всей таблицы
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.black),  # Внутренняя сетка
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),  # Белый фон для ячеек
            ("LEFTPADDING", (0, 0), (-1, -1), 10),  # Отступ слева для содержимого ячеек
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Выравнивание текста по левому краю
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Выравнивание содержимого по центру вертикали
            ("FONTNAME", (0, 0), (-1, -1), "Arial"),  # Шрифт Arial для всей таблицы
            ("FONTSIZE", (0, 0), (-1, -1), 12)  # Размер шрифта 12 для всей таблицы
        ]))

        elements.append(Spacer(1, 24))
        caption = Paragraph("Подоконники", style=style_head_table)
        elements.append(caption)
        elements.append(Spacer(1, 4))
        elements.append(table)

    # Генерация документа
    doc.build(elements)

    # Получение содержимого PDF из буфера
    pdf_content = buffer.getvalue()
    buffer.close()

    # Сохранение PDF-файла
    datetime_save = datetime.datetime.now()
    datetime_save = datetime_save.strftime("%Y-%m-%d_%H-%M-%S")

    # with open(f"{MEDIA_ROOT}/offers/offer_{pk}_{datetime_save}.pdf", "wb") as file:
    #     file.write(pdf_content)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ззз.pdf"'

    response.write(pdf_content)

    return response


def add_hide_cost_miscalculation(pk, cost):
    try:
        miscalculation = Miscalculation.objects.get(pk=pk)

        constructors = miscalculation.constructors.all()
        count = 0  # Начальное значение для подсчета

        for el in constructors:
            if el.window_calc:  # Проверка наличия связанного объекта window_calc
                count += 1

        if count > 0:
            add_cost = float(cost) / count

            for el in constructors:
                if el.window_calc:
                    window_calc = el.window_calc
                    window_calc.price_output += add_cost
                    window_calc.save()
                    constructor = Constructor.objects.get(pk=el.pk)
                    constructor.price_constructor += add_cost
                    constructor.save()

            miscalculation.hidden_cost += float(cost)
            miscalculation.sum += add_cost
            miscalculation.save()

    except Miscalculation.DoesNotExist:
        # Обработка случая, когда Miscalculation с данным pk не найдена
        pass


def minus_hide_cost_miscalculation(pk, cost):
    try:
        if cost > 0:
            miscalculation = Miscalculation.objects.get(pk=pk)

            constructors = miscalculation.constructors.all()
            count = 0  # Начальное значение для подсчета

            for el in constructors:
                if el.window_calc:  # Проверка наличия связанного объекта window_calc
                    count += 1

            if count > 0:
                add_cost = float(cost) / count

                for el in constructors:
                    if el.window_calc:
                        window_calc = el.window_calc
                        window_calc.price_output -= add_cost
                        window_calc.save()
                        constructor = Constructor.objects.get(pk=el.pk)
                        constructor.price_constructor -= add_cost
                        constructor.save()

                miscalculation.hidden_cost -= float(cost)
                miscalculation.sum -= add_cost
                miscalculation.save()

    except Miscalculation.DoesNotExist:
        # Обработка случая, когда Miscalculation с данным pk не найдена
        pass