import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password=input("Enter MySQL password: "),password = "saarth4149",
    database = "hospital_db"
)

cursor = conn.cursor()

# Fetching ONE row
cursor.execute("select count(*) from patient_records")
result = cursor.fetchone()
print("Total no of rows :-",result[0])


#fetching More than ONE row
cursor.execute("SELECT Name, Age FROM patient_records LIMIT 5")
rows = cursor.fetchall()
print("First 5 rows:")
for row in rows:
    print(row)

conn.close()