import os
import numpy

script_dir = os.path.dirname(__file__)
rel_path = 'pima-indians-diabetes.data.csv'
csv_file_path = os.path.join(script_dir, rel_path)
print("Open CSV: {}".format(csv_file_path))

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
csvdata = numpy.loadtxt(csv_file_path, dtype=None, delimiter=',')
print(csvdata)