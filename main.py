from fetch_questions import fetch_questions  # Importing the function to fetch questions

# Get student ID input
student_id = input("Enter Student ID: ")

# Fetch the questions based on student ID
questions = fetch_questions(student_id)

# Fetch and display questions with filenames
if questions:
    print("\nHere are your questions:\n")
    for idx, question_data in enumerate(questions, start=1):
        question_text = question_data[0]  # First element is question text
        filename = question_data[1]  # Second element is filename
        print(f"{idx}. {question_text}  [Source: {filename}]")
else:
    print("No questions found.")
