import psycopg2

# Database connection parameters
db_params = {
    "dbname": "qa_auto",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",  # or IP address, e.g., "127.0.0.1"
    "port": "5432"  # Default PostgreSQL port
}

try:
    # Establishing the connection
    connection = psycopg2.connect(r'/home/natakhor/repos/LnD?Become QA Auto' + r'become_qa_auto.db')

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example: Execute a simple query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL database version: {db_version}")

    # Commit transactions (if needed)
    connection.commit()

except Exception as error:
    print(f"Error connecting to PostgreSQL database: {error}")

finally:
    # Close the cursor and connection to free resources
    if cursor:
        cursor.close()
    if connection:
        connection.close()
