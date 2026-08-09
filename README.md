# Hospital Billing & Operations Analytics

End-to-end data analytics pipeline built on a ~55,000-row healthcare dataset — cleaning raw hospital billing data and turning it into a full business intelligence dashboard across 5 tools.

**Pipeline:** `CSV → Python/Pandas (clean) → MySQL (store) → SQL (analyze) → Matplotlib / Excel / Tableau (visualize)`

## 📊 Problem Statement

Real-world hospital billing logs contain blanks, duplicate records from system logging bugs, and unformatted columns. This project builds a clean, reproducible data pipeline to fix that — then analyzes revenue, patient volume, and operational patterns across clinical conditions.

## 🗂️ Dataset

[Healthcare Dataset by Prasad Patil — Kaggle](https://www.kaggle.com/datasets/prasad22/healthcare-dataset)
~55,000 patient records: demographics, medical condition, admission/discharge dates, billing amount, insurance provider, and more.

## 🛠️ Tools & Workflow

| Stage | Tool | What it does |
|---|---|---|
| 1. Cleaning | Python (Pandas) | Removes duplicates, handles nulls, standardizes text/date formats |
| 2. Storage | MySQL | Cleaned data loaded into a `patient_records` table |
| 3. Analysis | SQL | Aggregation queries — revenue, patient volume, billing trends |
| 4. Verification | Matplotlib | 4 charts confirming the cleaned data looks correct |
| 5. Reporting | Excel | Pivot Tables + charts summarizing condition, admission type, insurance |
| 6. Dashboard | Tableau | Interactive executive dashboard (Treemap, Histogram, Combo chart, Box Plot) |

## 📁 Repo Structure
```
hospital-billing-analytics/
├── data/
│   └── healthcare_dataset.csv
├── scripts/
│   ├── cleaning_data.py
│   ├── load_csv_to_MySql.py
│   ├── load_data_MysqlToPython.py
│   └── matplotlib_charts.py
├── sql/
│   └── healthcare_dataset_queries.sql
├── charts/
│   ├── chart1_age_group_distribution.png
│   ├── chart2_monthly_admissions_trend.png
│   ├── chart3_condition_distribution.png
│   └── chart4_insurance_claims.png
├── excel/
│   └── cleaned_healthcare_dataset_with_pivot.xlsx
├── tableau/
│   └── HealthcareDataset_Dashboard.twbx
└── presentation/
    └── Hospital_Analytics_ppt.pptx
```

## 🔑 Key Finding

Billing amount and length of stay show **minimal variance** across medical condition, admission type, age group, and insurance provider — a genuine property of this dataset rather than a forced pattern. Instead, **total revenue tracks patient admission volume almost directly**, since per-patient billing stays nearly constant. This was confirmed both statistically (box plots, aggregated SQL queries) and visually (dual-axis combo chart in Tableau).

## ▶️ How to Run

**1. Install dependencies**
```bash
pip install pandas mysql-connector-python matplotlib openpyxl
```

**2. Set up MySQL**
- Start your local MySQL server
- Each script will prompt you to enter your MySQL password when run

**3. Run in order**
```bash
python scripts/cleaning_data.py
python scripts/load_csv_to_MySql.py
python scripts/load_data_MysqlToPython.py
python scripts/matplotlib_charts.py
```

**4. Excel & Tableau**
- Open `excel/cleaned_healthcare_dataset_with_pivot.xlsx` for Pivot Table reporting
- Open the `.twbx` file in Tableau Public/Desktop for the interactive dashboard

## 📈 Sample Insight

| Medical Condition | Patients | Avg. Billing (₹) |
|---|---|---|
| Diabetes | 9,216 | 25,660.5 |
| Obesity | 9,146 | 25,804.4 |
| Arthritis | 9,218 | 25,511.8 |
| Hypertension | 9,151 | 25,503.1 |
| Asthma | 9,095 | 25,633.5 |
| Cancer | 9,140 | 25,152.3 |

## 👤 Author

**Saarth**
VIPS (GGSIPU) — BCA, 2nd Year
