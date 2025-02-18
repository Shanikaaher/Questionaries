import random
from db_connection import mongo_db
from get_student_interest import get_student_interest

# Common subjects list (40% of the questions will be from here)
common_subjects = [
    "Drawing", "Sports", "Defence", "Logical", "Psychological Puzzles", 
    "Scenario-Based", "Creative Pursuits", "Reasoning", 
    "Social Emotional Learning", "Sci-Fi", "Fun Questions"
]

# Function to fetch questions based on the student's interests and subjects
def fetch_questions(student_id):
    student_interests = get_student_interest(student_id)

    if not student_interests:
        print("No valid interests found. Exiting.")
        return []

    selected_questions = []
    total_questions = 20  # Number of total questions (set to 20 as per your requirement)
    interest_count = len(student_interests)

    # Calculate how many questions to fetch from student interests and common subjects
    primary_question_count = int(total_questions * 0.6)  # 60% for student interests
    common_question_count = total_questions - primary_question_count  # Remaining 40% for common subjects

    # Fetch questions from student interests
    if interest_count == 1:
        # If the student has only one interest, fetch all 60% from that subject
        selected_questions += fetch_questions_from_mongo(student_interests[0], primary_question_count)

    elif interest_count > 1:
        # If the student has more than one interest, divide the 60% equally between them
        primary_subject, secondary_subject = student_interests[:2]
        selected_questions += fetch_questions_from_mongo(primary_subject, primary_question_count // 2)
        selected_questions += fetch_questions_from_mongo(secondary_subject, primary_question_count // 2)

    # Fetch questions from common subject collections (40% of total questions)
    common_selected_questions = []
    common_subjects_for_distribution = ["Logical", "Psychological Puzzles", "Scenario-Based", 
                                        "Creative Pursuits", "Reasoning", "Social Emotional Learning", "Sci-Fi"]

    # 20% from logical reasoning, puzzles, scenario-based, etc.
    primary_common_count = common_question_count // 2
    # 20% from drawing, sports, defence, etc.
    secondary_common_count = common_question_count - primary_common_count

    # Fetch questions for primary common subjects (logical, psychological, etc.)
    for subject in common_subjects_for_distribution:
        if len(common_selected_questions) < primary_common_count:
            num_needed = primary_common_count - len(common_selected_questions)
            common_selected_questions += fetch_questions_from_mongo(subject, num_needed)

    # Fetch questions for secondary common subjects (drawing, sports, etc.)
    for subject in common_subjects:
        if len(common_selected_questions) < secondary_common_count:
            num_needed = secondary_common_count - len(common_selected_questions)
            common_selected_questions += fetch_questions_from_mongo(subject, num_needed)

    selected_questions += common_selected_questions

    # If not enough questions are fetched, fetch additional questions from available subjects
    remaining_needed = total_questions - len(selected_questions)
    if remaining_needed > 0:
        selected_questions += fetch_questions_from_mongo(student_interests[0], remaining_needed)  # Fill with primary subject

    random.shuffle(selected_questions)  # Shuffle questions to randomize order

    return selected_questions

# Function to fetch questions from MongoDB based on subject
def fetch_questions_from_mongo(subject, limit):
    collection = mongo_db[subject]  # Access the subject-based collection
    questions = list(collection.find({}, {"question": 1, "filename": 1, "_id": 0}).limit(limit))
    
    # Ensure missing 'filename' field is handled
    return [(q["question"], q.get("filename", "Unknown")) for q in questions]

# Main function to run the process
if __name__ == "__main__":
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
