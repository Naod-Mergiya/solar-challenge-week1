import pandas as pd
import numpy as np
from scipy.stats import zscore
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute summary statistics for the DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        
    Returns:
        pd.DataFrame: Summary statistics.
    """
    try:
        stats = df.describe()
        logger.info("Computed summary statistics")
        return stats
    except Exception as e:
        logger.error(f"Error computing summary statistics: {str(e)}")
        raise

def detect_negative_values(df: pd.DataFrame, columns: list) -> pd.Series:
    """
    Detect negative values in specified columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to check.
        
    Returns:
        pd.Series: Count of negative values per column.
    """
    try:
        negative_counts = (df[columns] < 0).sum()
        logger.info("Detected negative values")
        return negative_counts
    except Exception as e:
        logger.error(f"Error detecting negative values: {str(e)}")
        raise

def detect_missing_values(df: pd.DataFrame) -> tuple:
    """
    Detect missing values and their percentages.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        
    Returns:
        tuple: (missing_counts, missing_percentages)
    """
    try:
        missing_counts = df.isna().sum()
        missing_percentages = (missing_counts / len(df)) * 100
        logger.info("Detected missing values")
        return missing_counts, missing_percentages
    except Exception as e:
        logger.error(f"Error detecting missing values: {str(e)}")
        raise

def detect_outliers(df: pd.DataFrame, columns: list, threshold: float = 3) -> pd.DataFrame:
    """
    Detect outliers using Z-scores.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to check.
        threshold (float): Z-score threshold for outliers (default: 3).
        
    Returns:
        pd.DataFrame: DataFrame containing outlier rows.
    """
    try:
        z_scores = df[columns].apply(zscore, nan_policy='omit')
        outliers = (z_scores.abs() > threshold).any(axis=1)
        outlier_df = df[outliers][columns]
        logger.info(f"Detected {outlier_df.shape[0]} outlier rows with |Z|>{threshold}")
        return outlier_df
    except Exception as e:
        logger.error(f"Error detecting outliers: {str(e)}")
        raise

def check_unrealistic_wind_speeds(df: pd.DataFrame, max_speed: float = 50) -> pd.DataFrame:
    """
    Check for unrealistic wind speeds.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        max_speed (float): Maximum realistic wind speed (default: 50 m/s).
        
    Returns:
        pd.DataFrame: DataFrame with rows exceeding max_speed.
    """
    try:
        high_wind = df[(df['WS'] > max_speed) | (df['WSgust'] > max_speed)]
        logger.info(f"Found {len(high_wind)} rows with unrealistic wind speeds (> {max_speed} m/s)")
        return high_wind
    except Exception as e:
        logger.error(f"Error checking unrealistic wind speeds: {str(e)}")
        raise