# db_connection.py

import pymysql
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection details from .env file
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Function to create a database connection using PyMySQL
def create_db_connection():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor  # To get results as dictionaries
        )
        return conn
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return None
