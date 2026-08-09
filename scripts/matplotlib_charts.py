import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter MySQL password: "),
    database="hospital_db"
)

# ============ CHART 1: Patient count by age group (bar with labels) ============
query1 = """
SELECT 
    CASE 
        WHEN age<18 THEN '0-17' 
        WHEN age BETWEEN 18 AND 35 THEN '18-35' 
        WHEN age BETWEEN 36 AND 50 THEN '36-50' 
        WHEN age BETWEEN 51 AND 65 THEN '51-65' 
        ELSE '65+' 
    END AS age_group, 
    COUNT(*) AS patients
FROM patient_records 
GROUP BY age_group
ORDER BY FIELD(age_group, '0-17','18-35','36-50','51-65','65+')
"""
df1 = pd.read_sql(query1, conn)

plt.figure(figsize=(8,5))
bars = plt.bar(df1["age_group"], df1["patients"], color="#4C72B0")
plt.title("Patient Count by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")

# Add the actual number on top of each bar - makes small differences readable
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 200, f"{int(height):,}",
             ha="center", fontsize=9)

plt.tight_layout()
plt.savefig("chart1_age_group_distribution.png")
plt.show()

# ============ CHART 2: Monthly admissions trend (cleaner x-axis) ============
query2 = """
SELECT DATE_FORMAT(date_of_admission, '%Y-%m') AS month, COUNT(*) AS admissions
FROM patient_records
GROUP BY month
ORDER BY month
"""
df2 = pd.read_sql(query2, conn)

plt.figure(figsize=(14,5))
plt.plot(df2["month"], df2["admissions"], color="#DD8452", linewidth=1.5)

# Add a flat average line so viewers can see if a month is above/below normal
avg_admissions = df2["admissions"].mean()
plt.axhline(avg_admissions, color="gray", linestyle="--", linewidth=1,
            label=f"Average ({avg_admissions:.0f}/month)")

plt.title("Monthly Patient Admissions Trend")
plt.xlabel("Month")
plt.ylabel("Number of Admissions")

# Only show every 3rd month label instead of all ~60 - removes clutter
tick_positions = range(0, len(df2), 3)
plt.xticks(tick_positions, df2["month"].iloc[tick_positions], rotation=90, fontsize=8)

plt.legend()
plt.tight_layout()
plt.savefig("chart2_monthly_admissions_trend.png")
plt.show()

# ============ CHART 3: Patient share by medical condition (PIE - values are close together) ============
query3 = """
SELECT medical_condition, COUNT(*) AS patient_count
FROM patient_records
GROUP BY medical_condition
ORDER BY patient_count DESC
"""
df3 = pd.read_sql(query3, conn)

plt.figure(figsize=(7,7))
plt.pie(df3["patient_count"], labels=df3["medical_condition"], autopct="%1.1f%%",
        colors=["#55A868", "#4C72B0", "#DD8452", "#C44E52", "#8172B2", "#937860"])
plt.title("Patient Share by Medical Condition")
plt.tight_layout()
plt.savefig("chart3_condition_distribution.png")
plt.show()

# ============ CHART 4: Claims share by insurance provider (PIE - values are close together) ============
query4 = """
SELECT insurance_provider, COUNT(*) AS claims
FROM patient_records
GROUP BY insurance_provider
ORDER BY claims DESC
"""
df4 = pd.read_sql(query4, conn)

plt.figure(figsize=(7,7))
plt.pie(df4["claims"], labels=df4["insurance_provider"], autopct="%1.1f%%",
        colors=["#C44E52", "#4C72B0", "#55A868", "#DD8452", "#8172B2"])
plt.title("Claims Share by Insurance Provider")
plt.tight_layout()
plt.savefig("chart4_insurance_claims.png")
plt.show()

conn.close()
print("All 4 charts generated and saved as PNG files in your project folder.")