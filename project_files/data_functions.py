import pandas as pd
from .constants import DATA_FILE

def get_data():
    return pd.read_excel(DATA_FILE)  # Name of this Excel file is stored inside contants.py