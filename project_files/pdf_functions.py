from io import BytesIO


from .data_functions import get_data

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

from reportlab.pdfgen import canvas             # It will enable me to write information on a PDF canvas.
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm

from .constants import PAGE_SIZE
from .constants import FONT, FONT_SIZE, FONT_COLOR
from .constants import TEMPLATE_FILE, ID_CARDS_DIR, IMAGES_DIR

from .qrcode_functions import code_generator


def create_info_canvas(student):
    packet = BytesIO()                      # Instead of a PDF file, I will use Python's Byte IO object -BytesIO()-, which will enable me to write student information on a memory instead of a file
    can = canvas.Canvas(packet, PAGE_SIZE)  # I will create a packet named BytesIO and use it instead of file name inside canvas class.

    can.setFont(FONT, FONT_SIZE)            # It will define font of the text which will be used on me canvas.
    can.setFillColor(FONT_COLOR)

    school_id = student['School ID']
    name = student['Name']
    surname = student['Surname']
    gender = student['Gender']
    dob = student['Date of Birth']

    # First two parameters are the positions of the text on the canvas.
    can.drawString(20.7*mm, 3.5*mm, school_id)
    can.drawString(23*mm, 29*mm, name)
    can.drawString(20*mm, 25.5*mm, surname)
    can.drawString(23*mm, 22.5*mm, gender)
    can.drawString(20*mm, 19.5*mm, dob)

    # I define code_generator(student) in a qrcode_functions.py
    qr_code = code_generator(student)
    can.drawImage(str(qr_code), 3*mm, 17*mm)

    image_path = IMAGES_DIR / f"{school_id}.png"

    if image_path.exists():
        can.drawImage(str(image_path), 13*mm, 35*mm, width=27*mm, height=30*mm)

    can.save()  # It will save me canvas
    packet.seek(0)  # To merge this packet with me template, I need to go its initial position.

    return PdfFileReader(packet)


# It will read our student_card.pdf, to read a pdf file.
def get_template(template=TEMPLATE_FILE):
    return PdfFileReader(str(template))     # It will convert its template into string.


def create_pdf_file(student, canvas_info, template):
    page = template.getPage(0)
    page.mergePage(canvas_info.getPage(0))

    output = PdfFileWriter()
    output.addPage(page)

    page = template.getPage(1)
    output.addPage(page)

    file_name = ID_CARDS_DIR / f"{student['School ID']}.pdf"

    with open(file_name, "wb") as file:
        output.write(file)


def create_an_id_card(student):
    # Create a canvas with student info
    # This canvas will be created with the information related to our student.
    canvas_info = create_info_canvas(student)

    # Get pdf template
    template = get_template()

    # Merge canvas with template
    create_pdf_file(student, canvas_info, template)


def create_student_cards():
    # Read data from an Excel file
    data = get_data()  # Import get_data, call it and store this in a variable name data.
    print(data)

    """
    Iterate over each student in the file.
    During each iteration, data.iterrows return a tuple of two objects:
    First one is the index of this row and second one -student- is the row itself.
    So instead of typing index after for, I will use underscore (_) which is used to name variables
    which will not be used in me code later.
    If the loop have not .head(number), it will iterate for all rows in Excel file.
    """
    for _, student in data.head(3).iterrows():  # In this project I want to iterate only over three rows.
        create_an_id_card(student)

    # Create an id card for each student

pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))  # Register the font file