import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (Change user and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this to your MySQL username
            password='yourpassword'  # Change this to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Explicitly handling MySQL errors
        print(f"MySQL Connector Error: {e}")

    except Exception as e:  # Handling other unexpected errors
        print(f"General Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
