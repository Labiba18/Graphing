"""
Program Name: Lab16_labalam_data1.py
Author: Labiba Alam
Description: Reads and plots U.S. unemployment data from FRED (UNRATE).
Date: 2025-05-02
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'unemployment.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)