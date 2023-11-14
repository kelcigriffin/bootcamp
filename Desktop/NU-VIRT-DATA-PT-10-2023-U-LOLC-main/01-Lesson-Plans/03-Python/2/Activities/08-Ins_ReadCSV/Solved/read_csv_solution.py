# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join(os.path.dirname(__file__),'..', 'Resources', 'contacts.csv')
#can also say csvpath = /Users/kelcigriffin/Desktop/NU-VIRT-DATA-PT-10-2023-U-LOLC-main/01-Lesson-Plans/03-Python/2/Activities/08-Ins_ReadCSV/Resources/contacts.csv

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
