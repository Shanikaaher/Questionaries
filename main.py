from fetch_questions import fetch_questions

# Get student ID input
student_id = input("Enter Student ID: ")

# Fetch and display questions with filenames
questions = fetch_questions(student_id)

if questions:
    print("\nHere are your questions:\n")
    for idx, (question, filename) in enumerate(questions, start=1):
        print(f"{idx}. {question}  [Source: {filename}]")
else:
    print("No questions found.")
