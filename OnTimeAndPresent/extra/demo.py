import numpy as np
import scipy 
from matplotlib import pyplot as plt

# Numpy Practice
# Q. Create a 1D array of numbers from 0 to 9
print('---------------------------')
print('#1')
arr = np.arange(10) #.array, .zeros, .ones, .empty, .linspace
print(arr)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(a)

# Q. Import the iris dataset keeping the text intact.
print('---------------------------')
print('#2')
iris = np.genfromtxt('extra/iris.data', delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris[:3])


# Q. Find the mean, median, standard deviation of iris's sepallength (1st column)
print('---------------------------')
print('#3')
sepallength = np.genfromtxt('extra/iris.data', delimiter=',', dtype='float', usecols=[0])
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(mu, med, sd)

# Q. Matplotlib
print('---------------------------')
print('#4')
x = np.arange(15)
y = 10 * x + 1
plt.title = ("Example")
plt.xlabel("Fish to fish food ratio")
plt.ylabel("# of running flask apps")
plt.plot(x,y)
plt.show()

"""Scipy Practice"""
from scipy import cluster, constants
help(cluster)
print('---------------------------')
print('#5')
print(f'Golden Ratio: {scipy.constants.golden_ratio}')
print(f'Rydberg Constant: {scipy.constants.Rydberg}')

# https://docs.scipy.org/doc/scipy/reference/special.html
print(f'Gamma Function: {scipy.special.gamma(10)}')




# https://www.machinelearningplus.com/python/101-numpy-exercises-python/