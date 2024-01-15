import psycopg2
import csv

connection_name = "postgres://postgres:ananas_2@localhost:5432/postgres"

def create_table():
    try:
        with psycopg2.connect(connection_name) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS students_performance (
                        student_id SERIAL PRIMARY KEY,
                        math_score INTEGER,
                        reading_score INTEGER,
                        writing_score INTEGER
                    );
                """)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

create_table()



def import_data(csv_file_path):
    try:
        with psycopg2.connect(connection_name) as conn:
            with conn.cursor() as cur:
                with open(csv_file_path, 'r') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip the header row
                    for row in reader:
                        # Extract only the math_score, reading_score, and writing_score columns
                        math_score, reading_score, writing_score = row[5], row[6], row[7]
                        cur.execute(
                            "INSERT INTO students_performance (math_score, reading_score, writing_score) VALUES (%s, %s, %s)",
                            (math_score, reading_score, writing_score)
                        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    except FileNotFoundError as fnf_error:
        print(fnf_error)

import_data(r'C:\PythonProjects\Dissertation\Jupyter_Notebook_Data_Exploration_Analysis\StudentsPerformanceData.csv')



create_table()
import_data(r'C:\PythonProjects\Dissertation\Jupyter_Notebook_Data_Exploration_Analysis\StudentsPerformanceData.csv')
