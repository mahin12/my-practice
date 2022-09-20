from sklearn.model_selection import sklearn
from cgi import test
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('https://forge.scilab.org/index.php/p/rdataset/source/tree/master/csv/MASS/Boston.csv')

x=dataset.drop(['Unnamed: 0', 'medv'], axis=1)
y=dataset['medv']

 
import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)