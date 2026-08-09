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
