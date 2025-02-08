from db_connection import create_db_connection

# Function to get student interests from the database
def get_student_interest(student_id):
    conn = create_db_connection()
    if not conn:
        return None

    cursor = conn.cursor()

    query = """
    SELECT Computed_Final_Interests  
    FROM Prediction 
    WHERE Student_id = %s
    """
    
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        # Handling multiple interests if stored as "Algebra,Geometry"
        interests = result['Computed_Final_Interests'].split(",")
        return [interest.strip() for interest in interests]
    else:
        print(f"No interest found for Student ID: {student_id}")
        return None
