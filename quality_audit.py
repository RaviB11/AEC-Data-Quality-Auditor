# quality_audit.py
# A Python script to audit a sample AEC dataset for quality issues.

import pandas as pd

def run_quality_audit(source_file):
    """
    Reads a CSV file and performs a series of data quality checks.
    Prints a summary report of the findings.
    """
    print("--- Starting AEC Data Quality Audit ---")
    
    try:
        # Read the data, keeping empty values as they are for now
        df = pd.read_csv(source_file)
        print(f"Successfully read {len(df)} rows from {source_file}.\n")
    except FileNotFoundError:
        print(f"ERROR: Could not find the source file: {source_file}")
        return

    # --- Data Quality Report ---
    print("--- Generating Data Quality Report ---\n")
    has_issues = False

    # 1. Completeness Check: Look for missing values in any column
    if df.isnull().values.any():
        has_issues = True
        print("[ISSUE FOUND] Completeness Check: Missing values detected!")
        print(df.isnull().sum())
        print("-" * 30)
    else:
        print("[OK] Completeness Check: No missing values found.")

    # 2. Validity Check: Ensure 'Quantity' is a positive number
    if 'Quantity' in df.columns and (df['Quantity'] < 0).any():
        has_issues = True
        print("[ISSUE FOUND] Validity Check: Negative values found in 'Quantity' column.")
        print(df[df['Quantity'] < 0])
        print("-" * 30)
    else:
        print("[OK] Validity Check: All quantities are positive.")

    # 3. Consistency Check: Check if a MaterialID has multiple Units of Measure
    if 'MaterialID' in df.columns and 'UnitOfMeasure' in df.columns:
        material_units = df.groupby('MaterialID')['UnitOfMeasure'].nunique()
        inconsistent_materials = material_units[material_units > 1]
        if not inconsistent_materials.empty:
            has_issues = True
            print("[ISSUE FOUND] Consistency Check: Some materials have multiple units of measure.")
            print(inconsistent_materials)
            print("-" * 30)
        else:
            print("[OK] Consistency Check: All materials have consistent units.")

    print("\n--- Audit Complete ---")
    if not has_issues:
        print("SUCCESS: The data has passed all quality checks!")
    else:
        print("ACTION REQUIRED: Please review the issues found above.")


# --- Run the audit ---
if __name__ == "__main__":
    data_file = 'material_logs.csv'
    run_quality_audit(data_file)
