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

# Now extract the data and plot
dates, rates = [], []

with open(filename) as f:
    reader = csv.reader(f)
    next(reader)  # skip header again

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rate = float(row[1])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            rates.append(rate)

plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()
ax.plot(dates, rates, linewidth=2)

ax.set_title("Unemployment Rate in the U.S.", fontsize=20)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Unemployment Rate (%)", fontsize=14)
ax.tick_params(labelsize=12)

plt.savefig('us_unemployment_plot.png', bbox_inches='tight')
plt.show()