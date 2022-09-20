from cgi import test
import numpy as np
import pandas as pd

dataset = pd.read_csv('/Users/mahin/Downloads/Boston.csv')

x=dataset.drop(['Unnamed: 0', 'medv'], axis=1)
y=dataset['medv']

print(dataset)
 
# import train_test_split

# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)