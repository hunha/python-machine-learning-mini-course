import pandas

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
description = data.describe()
head = data.head()
correlation = data.corr()

print('---------------------------------[description]-------------------------------')
print(description)
print('------------------------------------[head]-----------------------------------')
print(head)
print('------------------------------------[shape]----------------------------------')
print(data.shape)
print('-----------------------------------[dtypes]----------------------------------')
print(data.dtypes)
print('---------------------------------[correlation]-------------------------------')
print(correlation)