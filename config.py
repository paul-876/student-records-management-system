import mysql.connector

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',           # Default XAMPP MySQL user
    'password': 'Escape254',           # Default XAMPP MySQL password (empty)
    'database': 'student_db'  # Change if you use a different database name
}

def get_db_connection():
    """Create and return a MySQL database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        raise
