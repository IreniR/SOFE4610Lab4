import random
import numpy as np

list_1 = [1, 3, 5]
list_2 = [2, 4, 6]

print(type(list_1))

a = np.array([list_1])
print(type(a))

a_float = np.zeros(5)
print("Contents of array:", a_float)
print("Array type:", type(a_float))
print("Array shape:", a_float.shape)
print("Array itemSize:", a_float.itemsize)
print("Array size:", a_float.size)

a2 = np.zeros([2, 4])
print("Zeros Array: \n", a2)
arr_ones = np.ones([3, 5])
print("Print array of ones: \n", arr_ones)
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Print random number from given list:", random.choice([10, 20, 30]))

print("Print an array from 1 to 10:", np.arange(1, 11))
print("Reshaped array: \n", np.arange(1, 11).reshape([2, 5]))
lst = np.array(
    [[[1, 2, 3, 4], [4, 5, 6, 7]],
     [[7, 8, 9, 10], [10, 11, 12, 13]],
     [[14, 15, 16, 17], [18, 19, 20, 21]]])
sum = np.sum(lst, 0)
print("Sum of array using 0 axis: \n", sum)

lst1 = np.array([10, 20, 30, 40])
lst2 = np.array([4, 3, 2, 1])
print("Print sum of two arrays: \n", np.add([lst1], [lst2]))









