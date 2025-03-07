import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Step 1: Establish a connection to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',       # Replace with your MySQL host
            user='root',           # Replace with your MySQL username
            password='#Aug2003',   # Replace with your MySQL password
            database='student_db'  # Replace with your database name
        )

        if conn.is_connected():
            print("Connected to MySQL database!")

            # Step 2: Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Step 3: Create a table (if it doesn't exist)
            create_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                date_of_birth DATE NOT NULL
            )
            """
            cursor.execute(create_table_query)
            print("Table 'students' created or already exists.")

            # Step 4: Insert sample data into the table
            insert_query = """
            INSERT INTO students (first_name, email, date_of_birth)
            VALUES (%s, %s, %s)
            """
            student_data = [
                ('John Doe', 'john.doe@example.com', '2000-05-15'),
                ('Jane Smith', 'jane.smith@example.com', '2001-07-22'),
                ('Alice Johnson', 'alice.johnson@example.com', '1999-12-30')
            ]
            cursor.executemany(insert_query, student_data)
            conn.commit()
            print("Inserted sample data into the 'students' table.")

            # Step 5: Fetch and display data from the table
            select_query = "SELECT * FROM students"
            cursor.execute(select_query)
            rows = cursor.fetchall()

            print("\nStudents in the database:")
            for row in rows:
                print(row)

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Step 6: Close the cursor and connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

# Run the function
connect_to_mysql()