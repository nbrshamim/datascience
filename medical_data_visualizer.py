import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    # Load the dataset
    df = pd.read_csv('medical_examination.csv')

    # Add overweight column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

    # Normalize data
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    # Convert data to long format for catplot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'alco', 'active', 'smoke', 'overweight'])

    # Create catplot
    cat_plot = sns.catplot(
        x='variable',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='count',
        height=5,
        aspect=0.7,
        order=['cholesterol', 'gluc', 'alco', 'active', 'smoke', 'overweight'],
        palette="Set2"
    )

    # Set titles and labels
    cat_plot.set_axis_labels("variable", "total")
    cat_plot.set_titles("{col_name} {col_var}")
    cat_plot.set_xticklabels(['Normal', 'High'])
    plt.show()


def draw_heat_map():
    # Load the dataset
    df = pd.read_csv('medical_examination.csv')

    # Clean the data
    df_clean = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Create a correlation matrix
    corr_matrix = df_clean.corr()

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".1f",
        linewidths=.5,
        square=True,
        cmap="coolwarm",
        cbar_kws={"shrink": 0.8},
        mask=np.triu(corr_matrix)
    )

    plt.show()