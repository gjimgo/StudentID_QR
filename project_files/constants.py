"""
This file will store some values, which will never change during the runtime.
"""

# Path means where does this file located inside the computer
from pathlib import Path
from reportlab.lib.units import mm

# BASE_DIR will give me location of contants.py and then I will call its parent,
# which is project_files and then parent again, which will be our main folder.
BASE_DIR = Path(__file__).resolve().parent.parent

# DATA_DIR will reference to data folder inside BASE_DIR.
DATA_DIR = BASE_DIR / "data"

# It will reference to templates folder inside BASE_DIR.
TEMPLATES_DIR = BASE_DIR / "templates"

IMAGES_DIR = BASE_DIR / "images"
ID_CARDS_DIR = BASE_DIR / "id_cards"

# Constant which will reference to data file.
DATA_FILE = DATA_DIR / "student_data.xlsx"

# This constant will reference to template file.
# TEMPLATE_FRONT = TEMPLATES_DIR / "student_card_front.pdf"  # "student_card.pdf"
# TEMPLATE_BACK = TEMPLATES_DIR / "student_card_back.pdf"
TEMPLATE_FILE = TEMPLATES_DIR / "student_card.pdf"
QR_CODE_FILE = IMAGES_DIR / 'qr_code.png'

PAGE_WIDTH = 54 * mm
PAGE_HEIGHT = 85 * mm
PAGE_SIZE = PAGE_WIDTH, PAGE_HEIGHT

FONT = "Calibri"
FONT_SIZE = 6
FONT_COLOR = (0, 0, 0)  # Tuple with RGB colors, black consist of three zeros.
# print(DATA_DIR)