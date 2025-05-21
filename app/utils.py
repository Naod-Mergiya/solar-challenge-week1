import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    benin_df = pd.read_csv('data/benin_clean.csv')
    sierraleone_df = pd.read_csv('data/sierraleone_clean.csv')
    togo_df = pd.read_csv('data/togo_clean.csv')

    combined_df = pd.concat([
        benin_df.assign(Country='Benin'),
        sierraleone_df.assign(Country='Sierra Leone'),
        togo_df.assign(Country='Togo')
    ])
    return combined_df

def filter_data(df, selected_countries):
    return df[df['Country'].isin(selected_countries)]

def plot_boxplots(df, metrics):
    cols = len(metrics)
    fig, axes = plt.subplots(1, cols, figsize=(5 * cols, 5))
    if cols == 1:
        axes = [axes]
    for ax, metric in zip(axes, metrics):
        sns.boxplot(data=df, x='Country', y=metric, ax=ax)
        ax.set_title(metric)
    return fig

def calculate_average_metrics(df, metrics):
    return df.groupby('Country')[metrics].mean().reset_index()


def get_top_regions_by_ghi(avg_df):
    return avg_df.sort_values(by='GHI', ascending=False)
