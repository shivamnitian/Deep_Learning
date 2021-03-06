# -*- coding: utf-8 -*-
"""Diabates.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R8-1WSRBzmXJZPwhfoUC5GuN6eDwjlJh
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

diabates = datasets.load_diabetes()
print(diabates.keys())

diabates.data

diabates_X = diabates.data[:, np.newaxis, 2]

diabates_X

diabates_X_train = diabates_X[:-30]
diabates_X_test = diabates_X[-30:]

diabates_y_train = diabates.target[:-30]
diabates_y_test = diabates.target[-30:]

model = linear_model.LinearRegression()
model.fit(diabates_X_train,diabates_y_train)
diabates_y_predicted = model.predict(diabates_X_test)

from sklearn.metrics import mean_squared_error
print("mean squared_error: ",mean_squared_error(diabates_y_test,diabates_y_predicted))

#from sklearn.metrics import mean_squared_error
#print("mean squared_error: ",mean_squared_error(diabates_y_test,diabates_y_predicted))

#print("weight: ",model.coef_)

#print("Intercept: ",model.intercept_)

#plt.scatter(diabates_X_test,diabates_y_test)
#plt.plot(diabates_X_test,diabates_y_predicted)



