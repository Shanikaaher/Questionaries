from pymongo import MongoClient
from get_student_interest import get_student_interest

MONGO_URI = "mongodb://admin:admin@195.35.45.44:27017/Question?authSource=admin"
client = MongoClient(MONGO_URI)
db = client["Question"]

def fetch_questions(student_id):
    student_interests = get_student_interest(student_id)

    if not student_interests:
        print("No valid interests found. Exiting.")
        return []

    selected_questions = []
    total_questions = 20  

    for subject in student_interests:
        collection = db[subject.strip()]
        questions = list(collection.aggregate([{"$sample": {"size": 5}}]))  

        for q in questions:
            if "question" in q and "options" in q:
                selected_questions.append({
                    "question": q["question"],
                    "options": q["options"]
                })
            else:
                print(f"⚠️ Skipping question from {subject}: Missing 'question' or 'options' field")

    return selected_questions
