import pandas as pd
import mysql.connector

# Load CSV file into DataFrame
df = pd.read_excel("cleaned_healthcare_dataset.xlsx")


# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter MySQL password: "),
)
cursor = conn.cursor()

# Create database and table if they do not exist
cursor.execute("CREATE DATABASE IF NOT EXISTS hospital_bd")
cursor.execute("USE hospital_bd")

cursor.execute("""
CREATE TABLE IF NOT EXISTS patient_records (
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    blood_type VARCHAR(5),
    medical_condition VARCHAR(100),
    date_of_admission DATE,
    doctor VARCHAR(100),
    hospital VARCHAR(100),
    insurance_provider VARCHAR(100),
    billing_amount DECIMAL(12,2),
    room_number INT,
    admission_type VARCHAR(50),
    discharge_date DATE,
    medication VARCHAR(100),
    test_results VARCHAR(100)
)
""")

print("Database and table ready!")

# Insert all rows from DataFrame into MySQL table
# Explicitly select columns in the exact order the INSERT expects - safest against any column reordering
sql = """
INSERT INTO patient_records 
(name, age, gender, blood_type, medical_condition, date_of_admission, doctor, hospital, insurance_provider, billing_amount, room_number, admission_type, discharge_date, medication, test_results)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

print("About to insert rows...")

try:
    cursor.executemany(sql, df.values.tolist())
    conn.commit()
    print("Rows inserted:", cursor.rowcount)
except Exception as e:
    print("Error inserting data:", e)
    conn.rollback()

print("Insert attempt finished.")

# Close connection
cursor.close()
conn.close()