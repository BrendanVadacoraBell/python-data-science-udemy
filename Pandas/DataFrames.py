import numpy
import pandas
from numpy.random import randn

numpy.random.seed(101)

dataFrame = pandas.DataFrame(randn(5,4), ['a','b','c','d','e'],['w','x','y','z'])

print(dataFrame['w'])

print(dataFrame[['w','z']])

"""Drop without mutating"""

print(dataFrame.drop('z', 1))
print(dataFrame)

#Rows

print(dataFrame.loc['d'])
print(dataFrame.loc[['d','e'],['x','y']])

#Conditionals

print(dataFrame[dataFrame > 0])

