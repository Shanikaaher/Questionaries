from pymongo import MongoClient

MONGO_URI = "mongodb://admin:admin@195.35.45.44:27017/Question?authSource=admin"
client = MongoClient(MONGO_URI)
db = client["Question"]

subjects = ["Geography", "Computer", "Defence"]

for subject in subjects:
    collection = db[subject.strip()]
    print(f"Updating missing fields in {subject}...")

    # Ensure every document has a 'question' field
    collection.update_many(
        {"question": {"$exists": False}}, 
        {"$set": {"question": "Default question text"}}
    )

    # Ensure every document has an 'options' field
    collection.update_many(
        {"options": {"$exists": False}}, 
        {"$set": {"options": ["Option A", "Option B", "Option C", "Option D"]}}
    )

    print(f"✅ Updated missing fields in {subject}")
