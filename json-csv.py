import json
import csv

# Open the JSON file and load the data
with open("input.json") as json_file:
    json_data = json.load(json_file)

# Open a CSV file for writing and create a CSV writer
with open("output.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

# Iterate over the JSON data and write each row to the CSV file
for row in json_data:
    csv_writer.writerow(row)
#%%
# This code will open the input JSON file, read the data, create an output CSV file, and
# then write the data from the JSON file to the CSV file. You can then
# use a program like Excel or Google Sheets to open and view the resulting CSV file.