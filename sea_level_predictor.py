import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope_all, intercept_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = np.arange(df['Year'].min(), 2051)
    y_all = intercept_all + slope_all * x_all
    plt.plot(x_all, y_all, label='Best fit (all years)', linewidth=2)

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()