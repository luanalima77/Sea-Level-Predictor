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
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all, intercept_all = result.slope, result.intercept
    x_all = np.arange(df['Year'].min(), 2051)
    y_all = intercept_all + slope_all * x_all
    plt.plot(x_all, y_all, label='Best fit (all years)', linewidth=2)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    result_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    slope_2000, intercept_2000 = result_2000.slope, result_2000.intercept
    x_2000 = np.arange(2000, 2051)
    y_2000 = intercept_2000 + slope_2000 * x_2000
    plt.plot(x_2000, y_2000, label='Best fit (2000 onwards)', linewidth=2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.tight_layout()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()