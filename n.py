import numpy as np 
# arr= np.array([1,2,3])

# ar1=np.array((1,3,5,4,7,8))

# print(ar1)

# 0 demensional array 


# arr=np.array(40)
# print(arr)

# 1 demensional array 

# arr= np.array([1,2,3,4,5,])
# print(arr)

# 2 demensional array 

# arr= np.array([[1,2,3],[4,5,4]])
# print(arr)

# 3 demensional array 

# arr= np.array([[[1,2,3],[4,5,4]],[[6,7,8],[9,10,11]]])
# print(arr)
# print(arr.ndim)


# import numpy as np 
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[0])



# function in numpy array-------------------->------>
# ------------------------------------------->------>

# np.zeros
# arr=np.zeros(2)
# print(arr)



# np.ones 
# arr=np.ones(2)
# print(arr)


# np.empty 
# arr=np.empty(2)
# print(arr)



# np . arrange 
# arr=np.arange(4)
# print(arr)




# np.linspace 
# arr=np.linspace(0,10,num=5)
# print(arr)


# d type 

# arr=np.ones(2,dtype=int)
# print(arr)
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array(['Hello', 'BCA', 'Class'])   # Stored as Unicode characters with length of characters ranging to 5 
# arr3 = np.array([1, 2, 3, 4], dtype='S')  # Creating numpy array of defined type string
# print(arr1.dtype)
# print(arr2.dtype)
# print(arr3.dtype)




# Minimum Dimension:

# import numpy as np 
# a = np.array([1, 2, 3,4,5], ndmin = 2) 
# print (a)


# nd array. shape
# a=np.array([[1,2,3],[4,5,6]])
# # print(arr.shape)
# a.shape=(3,2)
# print(a)

# Reshaping and getting back to linear array


# a=np.arange(24)
# b=a.reshape(2,3,4)
# arr=b.ravel()
# print(arr)



# ndarray.itemsize

# x = np.array([1,2,3,4,5], dtype = np.int8)

# print (x.itemsize)
# print (x.size)



# indexing the array

# 1 d array
# arr=np.array([1,2,3,4])
# print(arr[0])
# print(arr[0]+arr[3])

# 2 d array 
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr[1,2])

# 3 d array
# arr= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr[0,0,2]+arr[0,1,2])

# using negative indexing 
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr[0,-4])
# print(arr[1,-4])


#print all of the values in the array that are less than 5
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr[arr>5])

#select elements that are divisible by 2
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr[arr%2==0])


# select elements that satisfy two conditions using the & and | operators:

# a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# # c=a[(a>2)&(a<11)]
# d=a[(a>5)|(a==5)]
# print(d)



# slicing method -------------------->

# arr = np.array([10, 20, 30, 40, 50, 60, 70])

# print(arr[1:5])
# print(arr[4:])
# print(arr[:4])

# negative slicing 

# print(arr[-3:-1])

# Step wise method 

# print(arr[1:5:3])

# print(arr[::2])

# slicing in 2 d array 

# arr = np.array([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]])
# print(arr[1,1:4:2])
# print(arr[0:2,2])
# print(arr[0:2,1:4])

# numpy copy and view array 

# arr = np.array([10, 20, 30, 40, 50])
# x = arr.copy()
# arr[0] = 100
# print(arr)
# x[0]=500
# print(x)

# arr[0]=100
# x=arr.view()
# print(arr)
# print (x)

# Check if array Owns its data 

# x=arr.copy()
# y=arr.view()
# print(x.base)
# print(y.base)

# Iterating Arrays 
# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)

# Iterate on elements 2-D Array
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)

#iterate on each scalar element in 2-D array

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#     for y in x:
#         print(y)

#Iterate on elements in 3-D array

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# # for x in arr:
# #   print(x)

# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)

#iterating each scalar element in 3-D array


# arr = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
# for x in np.nditer(arr):
#   print(x)


# Joining NumPy Arrays -------------->
#Join two 2-D arrays along rows (axis=1):

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)


# Searching Arrays --->

# Find the indexes where the value is 40:

# arr = np.array([10, 20, 30, 40, 50, 40, 40])
# x = np.where(arr == 40)
# y= np.where(arr == 50)
# print(y)
# print(x)

# Find indexes where the values are even 

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 != 0)
# print(x)


# Reversing a NumPy array 

# arr=np.array([1,2,3,4,5])
# print(arr[::-1])

# Method 2: flipud function: This function is provided by NumPy to reverse the NumPy array.

# arr=np.array([1,2,3,4,5])
# x= np.flipud(arr)
# print(x)

#  from loop 

# for  i in range(10,0,-1) :
#   print(i)

# import the array module

# import array as arr

# a=arr.array("i",[1,2,3,4,5])
# # print("the array is :", a)
# a.reverse()
# print("the reversed array",a)


