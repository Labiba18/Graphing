"""
Program Name: Lab16_lalam_1.py
Author: Labiba Alam
Description: This program reads and visualizes U.S. unemployment rate data from the FRED dataset (UNRATE) using matplotlib.
Date: 5/2/25
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

def read_csv_header(filename):
    """Read and print the CSV header using enumerate."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            print(index, column_header)

def load_unemployment_data(filename):
    """Extracts dates and unemployment rates from CSV."""
    dates, rates = [], []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                rate = float(row[1])
            except ValueError:
                continue
            else:
                dates.append(current_date)
                rates.append(rate)
    return dates, rates

def plot_unemployment(dates, rates):
    """Plots unemployment rate data using matplotlib."""
    plt.style.use('seaborn-v0_8-dark-palette')
    fig, ax = plt.subplots()
    ax.plot(dates, rates, linewidth=2)

    ax.set_title("Unemployment Rate in the U.S.", fontsize=20)
    ax.set_xlabel("Date", fontsize=14)
    ax.set_ylabel("Unemployment Rate (%)", fontsize=14)
    ax.tick_params(labelsize=12)

    plt.savefig('us_unemployment_plot.png', bbox_inches='tight')
    plt.show()

def main():
    filename = 'unemployment.csv'
    read_csv_header(filename)
    dates, rates = load_unemployment_data(filename)
    plot_unemployment(dates, rates)

if __name__ == "__main__":
    main()