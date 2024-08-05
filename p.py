import pandas as pd 
# import numpy as np 

# panda series 
# l = [10, 70, 20]
# var = pd.Series(l)
# print(var)


# empty series 
# l=pd.Series()
# print(l)


# Creating a series from an array ----------->
# data = np.array(['A', 'd', 'i', 't', 'y','a'])
# s= pd.Series(data ,index=[10,11,12,13,14,15])
# print(s)


# Creating a series from Lists ---------------->
# list=['s','a','n','t','o','s','h']
# var= pd.Series(list)
# print(var)

# Creating a series from Dictionary--------------->

# dict={'a':101,'b':102,'c':103}
# var= pd.Series(dict)
# print(var)


# Creating a series from Scalar value 

# ser=pd.Series(101,index=[0,1,2,3,4,5])
# print(ser)

# Labels-------------------->

# a = [100, 700, 2000]
# myvar = pd.Series(a)
# print(myvar[0])


# a = [100, 700, 2000]
# myvar = pd.Series(a,index=['x','y','z'])
# print(myvar)

# Data Frames 
# creating empty data frame 

# df=pd.DataFrame()
# print(df)

# creating the data frame by using the list 

# data=[1,2,3,4,5]
# df=pd.DataFrame(data,columns=['student_id'])
# print(df)


# creating the list under list 
# data=[["santosh",80],["arpan",21]]
# df=pd.DataFrame(data,columns=[ 'name','Student_RollNo'])
# print(df)



# Creating DataFrame from dict of ndarray/lists: 

# data={'name':["santosh","arpan","ayush"],
# "roll_no":[80,21,29]}
# df=pd.DataFrame(data)
# print(df)

# Create pandas dataframe from lists using a dictionary: 

# data=[{'a':1,'b':2,'c':3},
# {'aa':10,'bb':20,'cc':30}]
# df=pd.DataFrame(data)
# print(df)

# Creating dataframe from series 
# y=pd.DataFrame([1,2,3,4])
# df=pd.DataFrame(y)
# print(df)




# Creating DataFrame from Dictionary of series: 


# d = {'one': pd.Series([10, 20, 30, 40],
# 					index=['a', 'b', 'c', 'd']),
# 	'two': pd.Series([10, 20, 30, 40],
# 					index=['a', 'b', 'c', 'd'])}
# # creates Dataframe.
# df = pd.DataFrame(d)
# # print the data.
# print(df)


# Locate Row
# initialize data of lists.
# data = {'Name': ['Aditya', 'Subham', 'Riya', 'Saumya'],
# 		'RollNo': [10, 31, 91, 48]}
# # Create DataFrame
# df = pd.DataFrame(data)
# # Print the output.
# print(df)
# print(df.loc[0])
# print(df.loc[[0,1]])

# Named Indexes
# data = {
#   "Exercise": ['Skipping', 'CrossTrainer', 'Treadmill'],
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]

# }
# df=pd.DataFrame(data,index=["Day1","Day2","Day3"])
# print(df)
# print(df.loc['Day2'])


# Pandas read CSV ----->
# usecols = ['S.No.','rank','salary']

# data=pd.read_csv ( r"c:\Users\santo\OneDrive\Desktop\customers-100.csv",index_col=0,usecols=usecols)
# # View the first 5 rows---->
# print(data.head())
# # View the last 5 rows------->
# print(data.tail())
# print(data.head())


# Reading Data from the URL --------------------->

# Webpage URL
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# # Define the column names
# col_names = ["sepal_length_in_cm",
#             "sepal_width_in_cm",
#             "petal_length_in_cm",
#             "petal_width_in_cm",
#             "class"]

# # Read data from URL
# iris_data = pd.read_csv(url, names=col_names)

# print(iris_data) 
 


# max_rows ----------------->

# to check the capcity of file in your laptop 

# print(pd.options.display.max_rows)   

# Exporting data to CSV file ----------------------------->


# data=pd.read_csv ( r"c:\Users\santo\OneDrive\Desktop\customers-100.csv")
# data.to_csv('santosh.csv')
# print(data)


# Using nrows in read_csv()----------->
# Using skiprows in read_csv()--------------->


# data=pd.read_csv (r"c:\Users\santo\OneDrive\Desktop\customers-100.csv",nrows=15,skiprows=[5,8])
# print(data)


# Getting info about your dataset ---->


data=pd.read_csv (r"c:\Users\santo\OneDrive\Desktop\customers-100.csv")
print(data.columns)
# print(data.info())

# Another fast and useful attribute is .shape, which outputs just a tuple of (rows, columns):

# print(data.shape)


# Handling Duplicates  by using append()------------->



# temp_df = data.append(data)
# print(temp_df.shape)




# How to work with missing values ------------->
  # checking by is null() 
# print(data.isnull())
# checking to count the null by sum() 
# print(data.isnull().sum())

# removing the null values -------->
# by dropna() ------->
# data.dropna()
# data.dropna(axis=1)

# print(data.value_counts().head())
# print(data.corr())
# print(data.describe())