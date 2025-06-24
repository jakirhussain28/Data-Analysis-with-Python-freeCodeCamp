import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    res1 = linregress(x, y)
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = res1.slope * x_pred1 + res1.intercept
    plt.plot(x_pred1, y_pred1, 'b', label='Best Fit: 1880-2050')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, 'g', label='Best Fit: 2000-2050')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()