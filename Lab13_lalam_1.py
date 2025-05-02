"""
Program Name: Lab13_labalam_graph1.py
Author: Labiba Alam
Description: Plotting sin(x)/x for Lab 13 graph assignment
Date: 4/30/25
"""

import matplotlib.pyplot as plt
import numpy as np

# Create x and y values
x = np.linspace(-20, 20, 1000)
y = np.sinc(x / np.pi)  # sinc(x) = sin(x)/x

# Create the figure and plot
plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2)

# Add title and labels
ax.set_title("Plot of sin(x)/x", fontsize=20)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("sin(x)/x", fontsize=14)

# Add grid and tick size
ax.grid(True)
ax.tick_params(labelsize=12)

# Show the plot
plt.show()