# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:24:50 2019

@author: frick
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
print(sys.argv[0])


# load data and set index
titanic_data = pd.read_csv("Titanic.csv")
titanic_data = titanic_data.set_index("Name")
print(titanic_data.head())

# get the shape of the data set
titanic_data.shape

# get the data types
titanic_data.dtypes

# get the first entry
titanic_data.iloc[0]

#frequency table
titanic_data['Pclass'].value_counts(sort=False)

# bar plot of passenger classes (absolute)
titanic_data['Pclass'].value_counts(sort=False).plot('bar')
plt.grid()
plt.title('Absolute Häufigkeiten der Passagierklassen')
plt.show()

# pie chart of passenger classes 
freq = 100*titanic_data['Pclass'].value_counts(sort=False, normalize=True)
freq.plot('pie', labels = ['1st', '2nd', '3rd'], figsize=(6, 6), autopct='%.2f')
plt.title('Relative Häufigkeiten der Passagierklassen')

#frequency table (%)
100*titanic_data['Pclass'].value_counts(sort=False, normalize=True)

# bar plot of passenger classes (relative in percent)
freq = 100*titanic_data['Pclass'].value_counts(sort=False, normalize=True)
freq.plot('bar')
plt.grid()
plt.ylabel('Rel. Häufigkeit in %')
plt.xlabel('Passagierklassen')
plt.title('Relative Häufigkeiten der Passagierklassen')

# grouping of variables
titanic_pclass = titanic_data.groupby('Pclass')
print(titanic_pclass.mean())

# pivoting two variables
titanic_pivot = titanic_data.pivot_table(index='Pclass', columns='Sex', values='Survived')

# pivoting two variables
titanic_pivot = titanic_data.pivot_table(index='Pclass', columns='Sex', values='Fare', aggfunc = np.sum)

# cross table of passenger class and sex
titanic_crosstab = pd.crosstab(titanic_data, index='Pclass', columns='Sex')
