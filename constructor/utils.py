import os

from PyPDF2 import PdfReader, PdfWriter

from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont



from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from calculation.models import Constructor


def generate_offer():
    constructor = Constructor.objects.get(pk=1)

    buffer = BytesIO()

    # Создание документа PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter, bottomPadding=0)

    # Создание списка элементов для добавления в документ
    elements = []

    # Стили для текста
    styles = getSampleStyleSheet()
    # PRODUCTION
    # pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    # pdfmetrics.registerFont(TTFont('Arial-bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Arial', 'D:\dejavu\DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-bold', 'D:\dejavu\DejaVuSans-bold.ttf'))

    # Установка шрифта для стилей
    styles['Heading1'].fontName = 'Arial-bold'
    styles['Normal'].fontName = 'Arial'
    # PRODUCTION

    full_page_style = ParagraphStyle(name='FullPage', parent=styles['Normal'], fontSize=36, leading=32)
    styles.add(full_page_style)

    # Стиль для заголовка
    heading_style = styles['Heading1']
    heading_style.fontSize = 24  # Увеличение размера шрифта
    heading_style.textColor = colors.black  # Черный цвет текста
    heading_style.alignment = 1

    # Добавление изображения
    elements.append(Spacer(1, -72))
    elements.append(image)

    # Получение пути к файлу изображения из директории static
    image_path = f"{MEDIA_ROOT}/../../apps/static/assets/{sticker.cert_sign}.png"  #

    # Создание объекта Image с указанным путем к файлу
    image_cert = Image(image_path, width=100, height=60)


    data = [
        [
            Paragraph(
                f"<font name='Arial' size='32'> Цвет: </font> <font name='Arial-Bold' size='36'>{sticker.color}</font>",
                styles['FullPage']
            ),
            image_cert
        ]
    ]
    table = Table(data, colWidths=[370, 100])

    # Установка стилей для таблицы и ячеек
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Выравнивание содержимого ячеек по верхней границе
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),  # Выравнивание содержимого второй ячейки по правой границе
    ]))

    # Добавление текста
    elements.append(Paragraph(sticker.datamatrix_code, heading_style))
    elements.append(Spacer(1, 12))

    elements.extend([
        Paragraph(
            f"<font name='Arial' size='32'>Бренд: </font> <font name='Arial-Bold' size='36'>{sticker.brand}</font>",
            styles['FullPage'])
    ])
    elements.extend([
        Paragraph(
            f"<font name='Arial' size='32'>Артикул: </font> <font name='Arial-Bold' size='36'>{sticker.number}</font>",
            styles['FullPage'])
    ])
    elements.extend([
        Paragraph(
            f"<font name='Arial' size='32'>Артикул поставщика: </font>",
            styles['FullPage'])
    ])
    elements.extend([
        Paragraph(
            f"<font name='Arial-Bold' size='36'>{sticker.producer_number}</font>",
            styles['FullPage'])
    ])
    elements.extend([
        Paragraph(
            f"<font name='Arial' size='32'>Р-р: </font> <font name='Arial-Bold' size='36'>{sticker.size}</font>",
            styles['FullPage'])
    ])
    elements.append(Spacer(1, 4))

    elements.append(table)
    elements.append(Spacer(1, 26))

    # Добавление изображения
    elements.append(image)

    heading_style_barcode = styles['Heading1']
    heading_style_barcode.fontSize = 30  # Увеличение размера шрифта
    heading_style_barcode.textColor = colors.black  # Черный цвет текста
    heading_style_barcode.alignment = 1


    # Генерация документа
    doc.build(elements)

    # Получение содержимого PDF из буфера
    pdf_content = buffer.getvalue()
    buffer.close()

    # Сохранение PDF-файла


    with open(os.path.join(), "wb") as file:
        file.write(pdf_content)

