# Student Performance Analysis System

## Objective
This project aims to analyze student performance by examining the relationship between study habits, attendance, and academic outcomes. It provides a comprehensive pipeline for cleaning raw data, engineering relevant features, and extracting statistical insights. The system identifies top performers and areas for improvement, helping educators understand key drivers of success.

## Dataset Description
- **StudyHours**: Number of hours spent studying by the student.
- **Attendance**: Percentage of classes attended.
- **Marks**: Academic score obtained by the student.

## Project Structure
```
student-performance-analysis/
├── data/
│   └── student_dataset.csv
├── src/
│   ├── preprocess.py
│   └── analysis.py
├── main.py
├── requirements.txt
└── README.md
```

## Steps Performed
1. **Data Loading and Inspection**: Loading the CSV and checking initial structure.
2. **Data Cleaning**: Handling missing values by filling Marks with mean and StudyHours with median, and removing outliers.
3. **Feature Engineering**: Adding 'Performance' categories and calculating 'EffortScore' (StudyHours × Attendance).
4. **Data Analysis**: Calculating basic statistics, correlations, and identifying top/low performers.
5. **Group-Based Analysis**: Aggregating data by performance levels to compare effort and scores.

## Key Insights
- The average marks across the entire student population is approximately 69.99.
- Student_342 achieved the highest marks in the dataset, becoming the top performer.
- There is a weak positive correlation (0.0213) between study hours and marks in this specific dataset.
- About 31.00% of the students fall into the "Needs Improvement" category (Marks < 60).
- Students in the "Excellent" category maintain an average EffortScore of 404.73.

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## Technologies Used
Python, pandas, numpy, matplotlib, seaborn
