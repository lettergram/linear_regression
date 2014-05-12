import numpy as np
import matplotlib.pyplot as plt

'''
Determines the linear regression line on
the given input array of points [x][y]
'''
def LS(array):

    sumxy = 0.0
    sumx = 0.0
    sumy = 0.0
    sumxx = 0.0
 
    x = 0
    y = 1

    for i in range(len(array)):
        sumxy += (array[i][x] * array[i][y])
        sumx += array[i][x]
        sumy += array[i][y]
        sumxx += array[i][x]**2

    slope = sumxy - ((sumx * sumy) / len(array))
    slope /= sumxx - (sumx**2 / len(array))

    initial = (sumy - (slope * sumx)) / len(array)

    LinearRegression = []

    for i in range(len(array)):
        LinearRegression.append([i, initial + (slope * i)])

    return LinearRegression

'''
Plots the differences between the linear regression line
and the given points which we attempted to fit the line to.
'''
def plotDifferences(points, fit):

    x = []
    y = []

    for i in range(len(points)):
        line = [points[i][1], fit[i][1]]
        iter = [i, i]
        plt.plot(iter, line,'b', label='Difference', linewidth=2)

'''
Plots the linear regression line,
Or really any array as a line
'''
def plotLinearRegression(fit):

    x = []
    y = []

    for i in range(len(fit)):
        x.append(fit[i][0])
        y.append(fit[i][1])
    plt.plot(x, y, 'g', label='Linear Regression', linewidth=2)


'''
Plots various points given an input array
'''
def plotPoints(points):
    
    x = []
    y = []
    
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])

    plt.plot(x, y,'ro')




''' ___MAIN___ '''
points = [[0, 2.2], [1, 2.2], [2, 1], [3, 3],\
[4, 3], [5, 4], [6, 3], [7, 6], [8, 6], [9, 7],\
[10, 11], [11, 12], [12, 14], [13, 10], [14, 11]]

y = []
x = []
fit = LS(points)


plotPoints(points)
plotLinearRegression(fit)
plt.title('Simple Linear Regression Example')
plt.show()


plotDifferences(points, fit)
plotLinearRegression(fit)
plotPoints(points)
plt.title('Difference in Simple Linear Regression Example')
plt.show()
