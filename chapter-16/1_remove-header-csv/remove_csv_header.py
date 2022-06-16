# remove_csv_header.py - Removes the header from all CSV files in the current working directory.

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csv_file_name in os.listdir('.'):
    if not csv_file_name.endswith('.csv'):
        continue    # skip non-csv files

    print('Removing header from ' + csv_file_name + '...')

    # Read the CSV file in (skipping first row).
    csv_rows = []
    csv_file_obj = open(csv_file_name)
    reader_obj = csv.reader(csv_file_obj)
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue    # skip first row   
        csv_rows.append(row)
    csv_file_obj.close()

    # Write out the CSV file.
    csv_file_obj = open(os.path.join('headerRemoved', csv_file_name), 'w', newline='')
    csv_writer = csv.writer(csv_file_obj)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_file_obj.close()