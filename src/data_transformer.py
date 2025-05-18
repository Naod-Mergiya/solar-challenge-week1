import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def convert_timestamp(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert Timestamp column to datetime and extract hour.
    
    Args:
        df (pd.DataFrame): Input DataFrame with Timestamp column.
        
    Returns:
        pd.DataFrame: DataFrame with converted Timestamp and new Hour column.
    """
    try:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df['Hour'] = df['Timestamp'].dt.hour
        logger.info("Converted Timestamp to datetime and extracted Hour")
        return df
    except Exception as e:
        logger.error(f"Error converting timestamp: {str(e)}")
        raise

def cap_wind_speeds(df: pd.DataFrame, max_speed: float = 50) -> pd.DataFrame:
    """
    Cap wind speeds (WS and WSgust) at a maximum value.
    
    Args:
        df (pd.DataFrame): Input DataFrame with WS and WSgust columns.
        max_speed (float): Maximum allowed wind speed (default: 50 m/s).
        
    Returns:
        pd.DataFrame: DataFrame with capped wind speeds.
    """
    try:
        df['WS'] = df['WS'].clip(upper=max_speed)
        df['WSgust'] = df['WSgust'].clip(upper=max_speed)
        logger.info(f"Capped WS and WSgust at {max_speed} m/s")
        return df
    except Exception as e:
        logger.error(f"Error capping wind speeds: {str(e)}")
        raise

def impute_missing_values(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Impute missing values in specified columns with median.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to impute.
        
    Returns:
        pd.DataFrame: DataFrame with imputed values.
    """
    try:
        for col in columns:
            if df[col].isna().sum() > 0:
                median_val = df[col].median()
                df[col].fillna(median_val, inplace=True)
                logger.info(f"Imputed {df[col].isna().sum()} missing values in {col} with median: {median_val}")
        return df
    except Exception as e:
        logger.error(f"Error imputing missing values: {str(e)}")
        raise