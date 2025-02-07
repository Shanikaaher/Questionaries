# main.py
from question_fetcher import get_student_interest

# Example student_id
student_id = 'S2025001'  # Replace with the actual student ID you want to check

# Fetch student interest based on student_id
student_interest = get_student_interest(student_id)

# Check if a valid result is returned
if student_interest:
    print(f"Student ID: {student_interest['Student_id']}")
    print(f"Computed Final Interests: {student_interest['Computed_Final_Interests']}")
else:
    print("No student found.")
