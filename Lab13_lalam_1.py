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

# Plot the graph
plt.plot(x, y)
plt.show()