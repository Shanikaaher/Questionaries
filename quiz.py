from fetch_questions import fetch_questions

# Define the correct answers
correct_answers = {
    1: "1",  # The correct answer for question 1 is option 1
    2: "2",  # The correct answer for question 2 is option 2
    3: "3",  # The correct answer for question 3 is option 3
    4: "2",  # The correct answer for question 4 is option 2
    5: "1"   # The correct answer for question 5 is option 1
}

def run_quiz():
    student_id = input("Enter Student ID: ")

    # Fetch the questions based on student ID
    questions = fetch_questions(student_id)

    # Initialize student's answers and score
    student_answers = {}
    score = 0

    # Fetch and display questions with options
    if questions:
        print("\nHere are your quiz questions:\n")
        for idx, question_data in enumerate(questions, start=1):
            question_text = question_data["question"]
            options = question_data["options"]
            
            # Display question and options
            print(f"{idx}. {question_text}")
            for i, option in enumerate(options, start=1):
                print(f"   {i}. {option}")
            
            # Get the student's answer
            answer = input("Please select an answer (1-4): ")
            student_answers[idx] = answer

            # Check if the answer is correct
            if answer == correct_answers[idx]:
                score += 1

            print()  # Just print an empty line between questions for better readability

        # Show final score
        print(f"\nYour final score is: {score} out of {len(questions)}")

    else:
        print("No questions found.")

if __name__ == "__main__":
    run_quiz()
