import pandas as pd
import numpy as np

def load_dataset(filepath):
    """Loads CSV, prints shape and first 5 rows"""
    df = pd.read_csv(filepath)
    print(f"Dataset loaded from {filepath}")
    print(f"Shape: {df.shape}")
    print("First 5 rows:")
    print(df.head())
    return df

def handle_missing_values(df):
    """Fills missing Marks with mean, missing StudyHours with median"""
    print("\nMissing values before:")
    print(df.isnull().sum())
    
    if 'Marks' in df.columns:
        df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
    if 'StudyHours' in df.columns:
        df['StudyHours'] = df['StudyHours'].fillna(df['StudyHours'].median())
        
    print("Missing values after:")
    print(df.isnull().sum())
    return df

def remove_outliers(df):
    """Removes rows where StudyHours > 15 or Marks > 100"""
    initial_rows = len(df)
    df = df[(df['StudyHours'] <= 15) & (df['Marks'] <= 100)]
    removed = initial_rows - len(df)
    print(f"\nRows removed (outliers): {removed}")
    return df

def feature_engineering(df):
    """Adds Performance and EffortScore columns"""
    def categorize_performance(marks):
        if marks >= 80:
            return "Excellent"
        elif marks >= 60:
            return "Good"
        else:
            return "Needs Improvement"
            
    df['Performance'] = df['Marks'].apply(categorize_performance)
    df['EffortScore'] = df['StudyHours'] * df['Attendance']
    print("\nFeature engineering complete. Added 'Performance' and 'EffortScore'.")
    return df

def preprocess_pipeline(filepath):
    """Main pipeline for preprocessing"""
    df = load_dataset(filepath)
    df = handle_missing_values(df)
    df = remove_outliers(df)
    df = feature_engineering(df)
    return df
