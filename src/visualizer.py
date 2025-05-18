import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def plot_distributions(df: pd.DataFrame, columns: list, output_dir: str = 'plots') -> None:
    """
    Plot histograms for specified columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to plot.
        output_dir (str): Directory to save plots (default: 'plots').
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        plt.figure(figsize=(12, 8))
        for i, column in enumerate(columns, 1):
            plt.subplot(3, 3, i)
            sns.histplot(df[column], bins=50, kde=True, color='skyblue')
            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
        plt.tight_layout()
        output_path = os.path.join(output_dir, 'distributions.png')
        plt.savefig(output_path)
        plt.close()
        logger.info(f"Saved distributions plot to {output_path}")
    except Exception as e:
        logger.error(f"Error plotting distributions: {str(e)}")
        raise

def plot_boxplots(df: pd.DataFrame, columns: list, output_dir: str = 'plots') -> None:
    """
    Plot boxplots for specified columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to plot.
        output_dir (str): Directory to save plots (default: 'plots').
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        plt.figure(figsize=(12, 8))
        for i, column in enumerate(columns, 1):
            plt.subplot(2, 3, i)
            sns.boxplot(y=df[column], color='lightcoral')
            plt.title(f'Boxplot of {column}')
            plt.xlabel(column)
        plt.tight_layout()
        output_path = os.path.join(output_dir, 'boxplots.png')
        plt.savefig(output_path)
        plt.close()
        logger.info(f"Saved boxplots to {output_path}")
    except Exception as e:
        logger.error(f"Error plotting boxplots: {str(e)}")
        raise

def plot_combined_visuals(df: pd.DataFrame, columns: list, output_dir: str = 'plots') -> None:
    """
    Plot combined histograms and boxplots for each column.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to plot.
        output_dir (str): Directory to save plots (default: 'plots').
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        for col in columns:
            fig, axes = plt.subplots(1, 2, figsize=(12, 4))
            
            # Histogram
            sns.histplot(df[col], kde=True, ax=axes[0], bins=50, color='skyblue')
            axes[0].set_title(f'Distribution of {col}')
            axes[0].set_xlabel(col)
            axes[0].set_ylabel("Frequency")
            
            # Boxplot
            sns.boxplot(x=df[col], ax=axes[1], color='lightcoral')
            axes[1].set_title(f'Boxplot of {col}')
            axes[1].set_xlabel(col)
            
            plt.tight_layout()
            output_path = os.path.join(output_dir, f'{col}_combined_plot_benin.png')
            plt.savefig(output_path)
            plt.close()
            logger.info(f"Saved combined plot for {col} to {output_path}")
    except Exception as e:
        logger.error(f"Error plotting combined visuals: {str(e)}")
        raise