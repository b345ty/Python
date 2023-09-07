#!/usr/bin/env python
# Convert csv files to xlsx format in directory.

import pandas as pd
import glob
import sys  # We import the sys module for error handling

# Specify the directory containing your CSV files
directory = (r"C:\Users\User1\Documents\Test")

# Get a list of all CSV files in the directory
csv_files = glob.glob(directory + '/*.csv')

# Check if there are CSV files to convert
if not csv_files:
    print("No CSV files found in the specified directory.")
    sys.exit(1)  # Exit with an error code

# Loop through each CSV file and convert to XLSX
for csv_file in csv_files:
    # Read the CSV file into a DataFrame using pandas
    df = pd.read_csv(csv_file)

    # Create the XLSX filename by replacing the .csv extension with .xlsx
    xlsx_file = csv_file.replace('.csv', '.xlsx')

    # Write the DataFrame to an XLSX file
    df.to_excel(xlsx_file, index=False)

print("Conversion complete.")
