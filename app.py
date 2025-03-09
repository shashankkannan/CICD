from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# EC2 MySQL Database Configuration
DB_HOST = "3.96.66.19"  # Your EC2 instance's public IP
DB_USER = "appuser"      # Your MySQL username
DB_PASSWORD = "yourpassword"  # Your MySQL password
DB_NAME = "mysql_test"   # Your database name

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None



# # RDS MySQL Database Configuration
# DB_HOST = "database-1.c9eu4gewe0tu.ca-central-1.rds.amazonaws.com"  # Replace with your RDS Endpoint
# DB_USER = "admin"      # Your RDS MySQL username
# DB_PASSWORD = "Mvss1234"  # Your RDS MySQL password
# DB_NAME = "database-1"   # Your RDS database name

# def get_db_connection():
#     try:
#         conn = mysql.connector.connect(
#             host=DB_HOST,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             database=DB_NAME
#         )
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Database connection error: {err}")
#         return None

@app.route('/users')
def get_users():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM table1")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
