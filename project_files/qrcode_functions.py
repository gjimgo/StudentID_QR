import pyqrcode

from .constants import  QR_CODE_FILE

def code_generator(student):
    info = f"{student['School ID']} - {student['Name']} - {student['Surname']} - {student['Gender']} - {student['Date of Birth']}"
    qr_image = pyqrcode.create(info)
    qr_image.png(str(QR_CODE_FILE), module_color=(0, 0, 0, 255), background=(255, 255, 255, 255), scale=1, quiet_zone=1)
    return QR_CODE_FILE
