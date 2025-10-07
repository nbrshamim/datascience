import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import the data
    df = pd.read_csv('epa-sea-level.csv')

    # Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Linear regression for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = list(range(1880, 2051))
    y_pred = [slope * x + intercept for x in x_pred]
    plt.plot(x_pred, y_pred, label=f'Original Fit (R-squared: {round(r_value**2, 2)})')

    # Linear regression for data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    y_pred_recent = [slope_recent * x + intercept_recent for x in x_pred]
    plt.plot(x_pred, y_pred_recent, label='Recent Fit')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and show the plot
    plt.savefig('sea_level_plot.png')
    plt.show()