import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)

hist = data.hist()

plot = data.plot(kind='box')

scatter_matrix(data)
plt.show()