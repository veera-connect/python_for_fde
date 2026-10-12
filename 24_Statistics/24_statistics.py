# Python examples extracted from 24_statistics.md
# Run one section at a time in VS Code using the cell play buttons.
# Some examples require packages or services described in the lesson.

# %%
# Example 1: Importing NumPy
# How to import numpy
    import numpy as np
    # How to check the version of the numpy package
    print('numpy:', np.__version__)
    # Checking the available methods
    print(dir(np))

# %%
# Example 2: Creating int numpy arrays
# Creating python List
    python_list = [1,2,3,4,5]

    # Checking data types
    print('Type:', type (python_list)) # <class 'list'>
    #
    print(python_list) # [1, 2, 3, 4, 5]

    two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

    print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Creating Numpy(Numerical Python) array from python list

    numpy_array_from_list = np.array(python_list)
    print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
    print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

# %%
# Example 3: Creating float numpy arrays
# Python list
    python_list = [1,2,3,4,5]

    numy_array_from_list2 = np.array(python_list, dtype=float)
    print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])

# %%
# Example 4: Creating boolean numpy arrays
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
    print(numpy_bool_array) # array([False,  True,  True, False, False])

# %%
# Example 5: Creating multidimensional array using numpy
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
    numpy_two_dimensional_list = np.array(two_dimensional_list)
    print(type (numpy_two_dimensional_list))
    print(numpy_two_dimensional_list)

# %%
# Example 6: Converting numpy array to list
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# %%
# Example 7: Creating numpy array from tuple
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]

# %%
# Example 8: Shape of numpy array
nums = np.array([1, 2, 3, 4, 5])
    print(nums)
    print('shape of nums: ', nums.shape)
    numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
    print(numpy_two_dimensional_list)
    print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
    three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10,11]]
    print(three_by_four_array)
    print('shape of three_by_four_array: ', three_by_four_array.shape)

# %%
# Example 9: Data type of numpy array
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# %%
# Example 10: Size of a numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3

# %%
# Example 11: Addition
# Mathematical Operation
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)

# %%
# Example 12: Subtraction
# Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)

# %%
# Example 13: Multiplication
# Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

# %%
# Example 14: Division
# Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)

# %%
# Example 15: Modulus
# Modulus; Finding the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

# %%
# Example 16: Floor Division
# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

# %%
# Example 17: Exponential
# Exponential is finding some number the power of another:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)

# %%
# Example 18: Checking data types
#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# %%
# Example 19: Converting types
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr

# %%
# Example 20: Converting types
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr

# %%
# Example 21: Converting types
np.array([-3, -2, 0, 1,2,3], dtype='bool')

# %%
# Example 22: Converting types
numpy_float_list.astype('int').astype('str')

# %%
# Example 23: Multi-dimensional Arrays
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# %%
# Example 24: Getting items from a numpy array
# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

# %%
# Example 25: Getting items from a numpy array
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

# %%
# Example 26: Slicing Numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

# %%
# Example 27: How to reverse the rows and the whole array?
two_dimension_array[::]

# %%
# Example 28: Reverse the row and column positions
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
    two_dimension_array[::-1,::-1]

# %%
# Example 29: How to represent missing values ?
print(two_dimension_array)
    two_dimension_array[1,1] = 55
    two_dimension_array[1,2] =44
    print(two_dimension_array)

# %%
# Example 30: How to represent missing values ?
# Numpy Zeroes
    # numpy.zeros(shape, dtype=float, order='C')
    numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
    numpy_zeroes

# %%
# Example 31: How to represent missing values ?
# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

# %%
# Example 32: How to represent missing values ?
twoes = numpy_ones * 2

# %%
# Example 33: How to represent missing values ?
# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

# %%
# Example 34: How to represent missing values ?
flattened = reshaped.flatten()
flattened

# %%
# Example 35: How to represent missing values ?
## Horitzontal Stack
    np_list_one = np.array([1,2,3])
    np_list_two = np.array([4,5,6])

    print(np_list_one + np_list_two)

    print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

# %%
# Example 36: How to represent missing values ?
## Vertical Stack
    print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

# %%
# Example 37: Generating Random Numbers
# Generate a random float  number
    random_float = np.random.random()
    random_float

# %%
# Example 38: Generating Random Numbers
# Generate a random float  number
    random_floats = np.random.random(5)
    random_floats

# %%
# Example 39: Generating Random Numbers
# Generating a random integers between 0 and 10

    random_int = np.random.randint(0, 11)
    random_int

# %%
# Example 40: Generating Random Numbers
# Generating a random integers between 2 and 11, and creating a one row array
    random_int = np.random.randint(2,10, size=4)
    random_int

# %%
# Example 41: Generating Random Numbers
# Generating a random integers between 0 and 10
    random_int = np.random.randint(2,10, size=(3,3))
    random_int

# %%
# Example 42: Generationg random numbers
# np.random.normal(mu, sigma, size)
    normal_array = np.random.normal(79, 15, 80)
    normal_array

# %%
# Example 43: Numpy and Statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)

# %%
# Example 44: Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))

# %%
# Example 45: Matrix in numpy
four_by_four_matrix

# %%
# Example 46: Matrix in numpy
np.asarray(four_by_four_matrix)[2] = 2
four_by_four_matrix

# %%
# Example 47: What is Arrange?
# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
lst

# %%
# Example 48: What is Arrange?
range(0, 11, 2)

# %%
# Example 49: What is Arrange?
for l in lst:
    print(l)

# %%
# Example 50: What is Arrange?
# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
whole_numbers

# %%
# Example 51: What is Arrange?
natural_numbers = np.arange(1, 20, 1)
natural_numbers

# %%
# Example 52: What is Arrange?
odd_numbers = np.arange(1, 20, 2)
odd_numbers

# %%
# Example 53: What is Arrange?
even_numbers = np.arange(2, 20, 2)
even_numbers

# %%
# Example 54: Creating sequence of numbers using linspace
# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
np.linspace(1.0, 5.0, num=10)

# %%
# Example 55: Creating sequence of numbers using linspace
# not to include the last value in the interval
np.linspace(1.0, 5.0, num=5, endpoint=False)

# %%
# Example 56: Creating sequence of numbers using linspace
# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

np.logspace(2, 4.0, num=4)

# %%
# Example 57: Creating sequence of numbers using linspace
# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)

# %%
# Example 58: Creating sequence of numbers using linspace
x

# %%
# Example 59: Creating sequence of numbers using linspace
x.itemsize

# %%
# Example 60: Creating sequence of numbers using linspace
# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
np_list

# %%
# Example 61: Creating sequence of numbers using linspace
print('First row: ', np_list[0])
print('Second row: ', np_list[1])

# %%
# Example 62: NumPy Statistical Functions with Example
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

# %%
# Example 63: NumPy Statistical Functions with Example
min:  1
max:  55
mean:  14.777777777777779
sd:  18.913709183069525

# %%
# Example 64: NumPy Statistical Functions with Example
print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))

# %%
# Example 65: How to create repeating sequences?
a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

# %%
# Example 66: How to generate random numbers?
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)

# %%
# Example 67: How to generate random numbers?
0.4763968133790438

# %%
# Example 68: How to generate random numbers?
# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)

# %%
# Example 69: How to generate random numbers?
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

# %%
# Example 70: How to generate random numbers?
['i' 'u' 'e' 'o' 'a' 'i' 'e' 'u' 'o' 'i']

# %%
# Example 71: How to generate random numbers?
## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
rand

# %%
# Example 72: How to generate random numbers?
rand2 = np.random.randn(2,2)
rand2

# %%
# Example 73: How to generate random numbers?
# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
rand_int

# %%
# Example 74: How to generate random numbers?
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

# %%
# Example 75: How to generate random numbers?
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

# %%
# Example 76: How to generate random numbers?
# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax

# numpy.dot(x, y, out=None)

# %%
# Example 77: Linear Algebra
## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23

# %%
# Example 78: NumPy Matrix Multiplication with np.matmul()
### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)

# %%
# Example 79: NumPy Matrix Multiplication with np.matmul()
## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)

# %%
# Example 80: NumPy Matrix Multiplication with np.matmul()
np.linalg.det(i)

# %%
# Example 81: NumPy Matrix Multiplication with np.matmul()
Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

# %%
# Example 82: NumPy Matrix Multiplication with np.matmul()
Z

# %%
# Example 83: NumPy Matrix Multiplication with np.matmul()
new_list = [ x + 2 for x in range(0, 11)]

# %%
# Example 84: NumPy Matrix Multiplication with np.matmul()
new_list

# %%
# Example 85: NumPy Matrix Multiplication with np.matmul()
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# %%
# Example 86: NumPy Matrix Multiplication with np.matmul()
np_arr = np.array(range(0, 11))
np_arr + 2

# %%
# Example 87: NumPy Matrix Multiplication with np.matmul()
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
pressure

# %%
# Example 88: NumPy Matrix Multiplication with np.matmul()
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

# %%
# Example 89: NumPy Matrix Multiplication with np.matmul()
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
