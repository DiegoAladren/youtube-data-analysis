import pandas as pd

def map_category(df, category_map, id_col='category_id', name_col='category_name'):
    """
    Map category IDs to category names.
    """
    df[name_col] = df[id_col].map(category_map)
    return df

def convert_to_datetime(df, column, format=None):
    """
    Convert a column to datetime.
    """
    df[column] = pd.to_datetime(df[column], format=format, errors='coerce')
    return df

def calculate_ratios(df):
    """
    Add like_ratio and comment_ratio columns.
    """
    df['like_ratio'] = df['likes'] / df['views']
    df['comment_ratio'] = df['comment_count'] / df['views']
    return df
