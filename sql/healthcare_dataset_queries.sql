-- ================================================================================
-- PROJECT: HOSPITAL HEALTHCARE DATA ANALYSIS
-- STUDENT NAME: SAARTH
-- DESCRIPTION: ADVANCED BUSINESS INTELLIGENCE & REVENUE CYCLE QUERIES
-- ================================================================================

-- =============================================================================
-- A. REVENUE PERFORMANCE (What's driving the money)
-- =============================================================================

-- Q1: What's total revenue, and what's the average bill per patient?
SELECT 
    FORMAT(SUM(billing_amount),2) AS total_revenue, 
    FORMAT(AVG(billing_amount), 2) AS avg_bill_per_patient 
FROM patient_records;


-- Q2: Which medical conditions contribute the most to total revenue?
SELECT 
    medical_condition, 
    FORMAT(COUNT(*),2) AS patient_count, 
    FORMAT(SUM(billing_amount),2) AS total_revenue, 
    FORMAT(AVG(billing_amount),2) AS avg_billing 
FROM patient_records 
GROUP BY medical_condition 
ORDER BY total_revenue DESC;


-- Q3: Which insurance provider brings in the most revenue, and does any provider systematically pay less per claim?
-- Payer-mix analysis — a real revenue-cycle question hospitals ask about insurers.
SELECT 
    insurance_provider, 
    FORMAT(COUNT(*), 2) AS claims, 
    FORMAT(SUM(billing_amount), 2) AS total_revenue, 
    FORMAT(AVG(billing_amount), 2) AS avg_claim 
FROM patient_records 
GROUP BY insurance_provider 
ORDER BY total_revenue DESC;
-- Because every single provider averages right around $25,400 to $25,600 per patient, no insurance company is systematically paying less or getting a massive discount. They are all paying the exact same rate on average.


-- =============================================================================
-- B. COST & RISK SEGMENTATION (Who costs the most, and why)
-- =============================================================================

-- Q4: Which age group generates the highest average billing?
SELECT 
    CASE 
        WHEN age < 18 THEN '0-17' 
        WHEN age BETWEEN 18 AND 35 THEN '18-35' 
        WHEN age BETWEEN 36 AND 50 THEN '36-50' 
        WHEN age BETWEEN 51 AND 65 THEN '51-65' 
        ELSE '65+' 
    END AS age_group, 
    FORMAT(COUNT(*),2) AS patients, 
    FORMAT(AVG(billing_amount), 2) AS avg_billing 
FROM patient_records 
GROUP BY age_group 
ORDER BY avg_billing DESC;


-- Q5: Does admission urgency (Emergency vs Elective vs Urgent) actually cost more?
-- Tests a real hypothesis: emergency care is assumed pricier — worth proving with data.
SELECT 
    admission_type, 
    FORMAT(COUNT(*), 2) AS cases, 
    FORMAT(AVG(billing_amount), 2) AS avg_billing 
FROM patient_records 
GROUP BY admission_type 
ORDER BY avg_billing DESC;


-- Q6: Which condition + admission type combination is the costliest, and is it high-volume or a rare outlier?
-- Separates "expensive but rare" from "expensive and common" — focus for cost-control.
SELECT 
    medical_condition, 
    admission_type, 
    FORMAT(COUNT(*), 2) AS cases, 
    FORMAT(AVG(billing_amount), 2) AS avg_billing 
FROM patient_records 
GROUP BY medical_condition, admission_type 
ORDER BY avg_billing DESC
LIMIT 10;


-- Q7: Are abnormal test results associated with higher billing?
-- Tests whether clinical severity (proxied by test result) correlates with cost.
SELECT 
    test_results, 
    ROUND(AVG(billing_amount), 2) AS avg_billing, 
    COUNT(*) AS cases 
FROM patient_records 
GROUP BY test_results 
ORDER BY avg_billing DESC;


-- =============================================================================
-- C. OPERATIONAL EFFICIENCY (Length of stay, capacity)
-- =============================================================================

-- Q8: What's the average length of stay by condition, and which conditions tie up beds longest?
-- Bed/resource planning — hospitals use Length of Stay (LOS) to forecast capacity.
SELECT
	medical_condition,
    ROUND(AVG(DATEDIFF(discharge_date, date_of_admission)), 3) AS avg_stay_days
FROM patient_records
GROUP BY medical_condition 
ORDER BY avg_stay_days DESC;

-- Q9: Does length of stay correlate with billing amount?
-- Tests the assumption "longer stay = higher bill" directly, rather than assuming it.
SELECT 
	DATEDIFF(discharge_date, date_of_admission) AS stay_length,
	ROUND(AVG(billing_amount) ,2)  AS avg_bill,
    COUNT(*) as cases
FROM patient_records
GROUP BY stay_length
ORDER BY stay_length;
-- The assumption “longer stay = higher bill” is not supported here


-- Q10: Is Emergency admission linked to shorter or longer stays than Elective?
-- Emergency care is often assumed shorter/triage-focused vs Elective's planned recovery stays.
SELECT 
    admission_type, 
    ROUND(AVG(DATEDIFF(discharge_date, date_of_admission)), 1) AS avg_stay 
FROM patient_records 
GROUP BY admission_type;
-- The assumption “Emergency = shorter stay” is not supported here


-- =============================================================================
-- D. TREND OVER TIME (Dashboard-worthy visual insights)
-- =============================================================================

-- Q11: How do admissions and revenue trend month-over-month?
-- THE chart every hospital BI dashboard leads with — reveals seasonality or growth.
SELECT 
    DATE_FORMAT(date_of_admission, '%Y-%m') AS month, 
    COUNT(*) AS admissions, 
    ROUND(SUM(billing_amount), 2) AS monthly_revenue 
FROM patient_records 
GROUP BY month 
ORDER BY month;


-- Q12: Is there a seasonal spike in any particular condition across months?
-- Real hospitals staff up seasonally based on exactly this pattern.
SELECT 
    DATE_FORMAT(date_of_admission, '%m') AS month_num, 
    medical_condition, 
    COUNT(*) AS cases 
FROM patient_records 
GROUP BY month_num, medical_condition 
ORDER BY month_num, cases DESC;


-- =============================================================================
-- E. ADVANCED SQL ANALYTICS (Window Functions)
-- =============================================================================

-- Q13: Within each condition, how does each patient's bill rank against peers with the same condition?
-- Useful for flagging outliers/overbilling within a diagnosis group — audit-style logic.
SELECT 
    name, 
    medical_condition, 
    billing_amount, 
    RANK() OVER (PARTITION BY medical_condition ORDER BY billing_amount DESC) AS billing_rank 
FROM patient_records;