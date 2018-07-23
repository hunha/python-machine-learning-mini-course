import os
import csv

script_dir = os.path.dirname(__file__)
rel_path = 'pima-indians-diabetes.data.csv'
csv_file_path = os.path.join(script_dir, rel_path)
print("Open CSV: {}".format(csv_file_path))
with open(csv_file_path, 'rt', encoding='utf8') as csvfile:
    csvdata = csv.reader(csvfile)
    for row in csvdata:
        print(row)