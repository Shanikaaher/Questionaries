# question_fetcher.py
import pymysql
from db_connection import create_db_connection

# Function to get student interest based on student ID
def get_student_interest(student_id):
    conn = create_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Using DictCursor to get data in key-value format

    # Query to get the student's interest based on student_id from 'prediction' table
    query = """
    SELECT Student_id, Computed_Final_Interests 
    FROM Prediction 
    WHERE Student_id = %s
    """
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()

    if result:
        return result  # Return the entire result (Student_id and Computed_Final_Interests)
    else:
        print(f"No student found with student_id: {student_id}")
        return None

    cursor.close()
    conn.close()
