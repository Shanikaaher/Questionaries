from db_connection import create_db_connection

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
        interests = result['Computed_Final_Interests'].split(",")  # Example: "Algebra,Geometry"
        print(f"Student interests for {student_id}: {interests}")  # Debug line to check interests
        return [interest.strip() for interest in interests]  
    else:
        print(f"No interest found for Student ID: {student_id}")
        return None
