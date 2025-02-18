import pymysql
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# MySQL Database connection details
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# MongoDB Connection URI
MONGO_URI = "mongodb://admin:admin@195.35.45.44:27017/Question?authSource=admin"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
mongo_db = client["Question"]  # Your database name

# Function to get a specific subject collection dynamically
def get_collection(subject_name):
    return mongo_db[subject_name]  # Subject names are collections

# Function to create a MySQL connection
def create_db_connection():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return None
