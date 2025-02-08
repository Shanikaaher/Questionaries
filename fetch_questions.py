import random
from get_student_interest import get_student_interest
from read_questions_from_word import read_questions_from_word

# Function to fetch questions based on student interests
def fetch_questions(student_id):
    student_interests = get_student_interest(student_id)
    
    if not student_interests:
        print("No valid interests found. Exiting.")
        return []

    common_subjects = ["Sports", "Logical", "Reasoning", "Drawing", "Sci-Fi", 
                       "Social Emotional Learning", "Creative Pursuits", 
                       "Scenario-Based", "Puzzles", "Psychological"]
    
    # Read questions for interested subjects
    subject_questions = {subject: read_questions_from_word(subject) for subject in student_interests}
    
    # Read questions for common subjects
    common_questions = {subject: read_questions_from_word(subject) for subject in common_subjects}

    # Define question distribution
    total_questions = 10  
    selected_questions = []

    if len(student_interests) == 1:
        primary_subject = student_interests[0]
        primary_question_count = int(total_questions * 0.6)  # 60% from primary interest
        common_question_count = total_questions - primary_question_count  # Remaining from common subjects

        selected_questions += random.sample(subject_questions[primary_subject], min(primary_question_count, len(subject_questions[primary_subject])))

    elif len(student_interests) >= 2:
        primary_subject, secondary_subject = student_interests[:2]  
        primary_question_count = int(total_questions * 0.3)  # 30% from each interest
        secondary_question_count = int(total_questions * 0.3)
        common_question_count = total_questions - (primary_question_count + secondary_question_count)  # Remaining from common subjects

        selected_questions += random.sample(subject_questions[primary_subject], min(primary_question_count, len(subject_questions[primary_subject])))
        selected_questions += random.sample(subject_questions[secondary_subject], min(secondary_question_count, len(subject_questions[secondary_subject])))

    # Fetch common subject questions
    common_selected_questions = []
    for subject in common_subjects:
        if len(common_selected_questions) < common_question_count:
            available_questions = common_questions[subject]
            num_needed = common_question_count - len(common_selected_questions)
            common_selected_questions += random.sample(available_questions, min(num_needed, len(available_questions)))

    selected_questions += common_selected_questions  

    # Shuffle questions for randomness
    random.shuffle(selected_questions)

    return selected_questions
