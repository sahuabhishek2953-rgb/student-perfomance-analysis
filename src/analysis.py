import pandas as pd
import numpy as np

def basic_statistics(df):
    """Prints df.describe() and mean, median, std for specific columns"""
    print("\n=== Basic Statistics ===")
    print(df.describe())
    cols = ['Marks', 'StudyHours', 'Attendance']
    for col in cols:
        if col in df.columns:
            print(f"\n{col} - Mean: {df[col].mean():.2f}, Median: {df[col].median():.2f}, Std: {df[col].std():.2f}")

def top_students(df, n=5):
    """Prints top n students by Marks descending"""
    print(f"\n=== Top {n} Students ===")
    top = df.sort_values(by='Marks', ascending=False).head(n)
    print(top[['Name', 'Marks']])

def low_performers(df, threshold=50):
    """Prints students with Marks < threshold"""
    print(f"\n=== Low Performers (Marks < {threshold}) ===")
    low = df[df['Marks'] < threshold]
    print(low[['Name', 'Marks']])

def studyhours_vs_marks(df):
    """Correlation and grouping by StudyHours"""
    print("\n=== StudyHours vs Marks ===")
    correlation = df['StudyHours'].corr(df['Marks'])
    print(f"Correlation: {correlation:.4f}")
    
    bins = [0, 4, 8, float('inf')]
    labels = ['Low (<4)', 'Medium (4-8)', 'High (>8)']
    df['StudyGroup'] = pd.cut(df['StudyHours'], bins=bins, labels=labels)
    avg_marks = df.groupby('StudyGroup', observed=True)['Marks'].mean()
    print("Avg Marks per StudyHours Group:")
    print(avg_marks)

def attendance_vs_marks(df):
    """Correlation and grouping by Attendance"""
    print("\n=== Attendance vs Marks ===")
    correlation = df['Attendance'].corr(df['Marks'])
    print(f"Correlation: {correlation:.4f}")
    
    bins = [0, 60, 80, float('inf')]
    labels = ['Low (<60)', 'Medium (60-80)', 'High (>80)']
    df['AttendanceGroup'] = pd.cut(df['Attendance'], bins=bins, labels=labels)
    avg_marks = df.groupby('AttendanceGroup', observed=True)['Marks'].mean()
    print("Avg Marks per Attendance Group:")
    print(avg_marks)

def group_by_performance(df):
    """Groups by Performance and prints avg Marks and EffortScore"""
    print("\n=== Performance Group Analysis ===")
    performance_stats = df.groupby('Performance', observed=True).agg({
        'Marks': 'mean',
        'EffortScore': 'mean'
    })
    print(performance_stats)

def extract_insights(df):
    """Prints exactly 5 insights as numbered full sentences"""
    print("\n=== Key Insights ===")
    
    # Calculate some metrics for insights
    avg_marks = df['Marks'].mean()
    correlation_study = df['StudyHours'].corr(df['Marks'])
    top_performer = df.iloc[df['Marks'].idxmax()]['Name']
    needs_improvement_pct = (len(df[df['Performance'] == 'Needs Improvement']) / len(df)) * 100
    avg_effort_excellent = df[df['Performance'] == 'Excellent']['EffortScore'].mean()
    
    insights = [
        f"1. The average marks across all students in the dataset is {avg_marks:.2f}.",
        f"2. There is a correlation of {correlation_study:.4f} between study hours and marks obtained.",
        f"3. {top_performer} is the top performing student with the highest marks recorded.",
        f"4. Approximately {needs_improvement_pct:.2f}% of students fall into the 'Needs Improvement' category.",
        f"5. Students categorized as 'Excellent' have an average EffortScore of {avg_effort_excellent:.2f}."
    ]
    for insight in insights:
        print(insight)
