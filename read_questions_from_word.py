import os
from docx import Document

# Function to read questions from a Word document
def read_questions_from_word(subject_name):
    base_path = r"C:\Users\shanika aher\Desktop\algo\questions\data"
    file_name = f"{subject_name}.docx"  
    file_path = os.path.join(base_path, file_name)

    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' not found!")  
        return []

    doc = Document(file_path)
    questions = [(para.text.strip(), file_name) for para in doc.paragraphs if para.text.strip()]  # Remove empty lines

    return questions
