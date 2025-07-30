# AEC Data Quality Auditor

## Objective
This project is a self-study initiative to demonstrate core data engineering principles, specifically focusing on **data quality and integrity**.

The goal is to simulate a real-world scenario where data from a construction project needs to be audited for errors before it can be used in downstream systems like BI dashboards or machine learning models.

## The Process

This project uses a Python script to perform a data quality audit on a sample dataset of material logs from a construction site (`material_logs.csv`).

The script performs the following checks:
1.  **Completeness Check:** Scans for any missing or null values in critical columns.
2.  **Format Check:** Validates that date columns are in the correct `YYYY-MM-DD` format.
3.  **Validity Check:** Ensures that numerical data (like `Quantity`) is logical (e.g., not negative).
4.  **Consistency Check:** Verifies that a `UnitOfMeasure` is consistent for the same `MaterialID`.

The script then generates a simple, human-readable **Data Quality Report** in the console, summarizing the issues found.

## Technologies & Concepts Demonstrated
* **Languages:** Python (Pandas)
* **Data Engineering:** Data Quality & Validation, ETL/ELT Processes, Data Auditing, Troubleshooting
* **Skills:** Critical Thinking, Problem-Solving, Attention to Detail

## How to Run
1.  Ensure you have Python and the Pandas library installed (`pip install pandas`).
2.  Clone this repository.
3.  Run the script from your terminal: `python quality_audit.py`
