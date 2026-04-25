from src.preprocess import preprocess_pipeline
from src.analysis import (
    basic_statistics,
    top_students,
    low_performers,
    studyhours_vs_marks,
    attendance_vs_marks,
    group_by_performance,
    extract_insights
)

def main():
    # Define dataset path
    dataset_path = 'data/student_dataset.csv'
    
    print("=== STEP 1: DATA LOADING AND PREPROCESSING ===")
    df = preprocess_pipeline(dataset_path)
    
    print("\n=== STEP 2: BASIC STATISTICS ===")
    basic_statistics(df)
    
    print("\n=== STEP 3: TOP PERFORMERS ===")
    top_students(df)
    
    print("\n=== STEP 4: LOW PERFORMERS ===")
    low_performers(df)
    
    print("\n=== STEP 5: STUDY HOURS VS MARKS ===")
    studyhours_vs_marks(df)
    
    print("\n=== STEP 6: ATTENDANCE VS MARKS ===")
    attendance_vs_marks(df)
    
    print("\n=== STEP 7: GROUP-BASED ANALYSIS ===")
    group_by_performance(df)
    
    print("\n=== STEP 8: INSIGHTS EXTRACTION ===")
    extract_insights(df)
    
    print("\nAnalysis complete. All tasks executed successfully.")

if __name__ == "__main__":
    main()
