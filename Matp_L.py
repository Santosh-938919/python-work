import matplotlib.pyplot as plt
import numpy as np 


# line plot --------------->

# x=[5,2,9,4,7]
# y=[10,5,8,4,2]
# plt.plot(x,y)
# plt.show()


# x=[1,5,8,7,3,9]
# y=[5,3,4,8,6,7]
# plt.plot(x,y)
# plt.show()

# Plotting x and y points  by using array 

# x=np.array([0,10])
# y=np.array([0,350])
# plt.plot(x,y)
# plt.show()

# xpoints = np.array([1, 10])
# ypoints = np.array([4, 20])
# plt.plot(xpoints, ypoints,)
# plt.show()


# Plotting Without Line ----------->
# xpoints = np.array([1, 10])
# ypoints = np.array([4, 20])
# plt.plot(xpoints, ypoints,'o:b')
# plt.show()

# Multiple Points: --------------------->
# x=np.array([1,2,6,8])
# y=np.array([3,8,1,10])
# plt.plot(x,y)
# plt.show()


# Markers ---------------->
# x=np.array([1,2,6,8])
# y=np.array([3,8,1,10])
# plt.plot(x,y ,marker='h')
# plt.show()

# Marker Size and marker colour(edge colour and face colour) --------->

# x=np.array([1,2,6,8])
# y=np.array([3,8,1,10])
# plt.plot(x,y ,marker='h',ms=20,mec='b',mfc='r')
# plt.show()


# linestyle method or ls 

# x=np.array([1,2,6,8])
# y=np.array([3,8,1,10])
# # plt.plot(x,y,linestyle='dashed')
# # plt.plot(x,y,ls='dashed')
# plt.plot(x,y,ls='dashed',color='red')
# plt.plot(x,y,ls='dashed',c='red', linewidth='20')

# plt.show()


# Muliple Lines------------->
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

# Label and title 

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x,y)
# plt.xlabel("Average pluse")
# plt.ylabel("calories burnage")
# plt.title("sport")
# plt.grid()
# plt.show()


# subplot --------------->


# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.suptitle("normal graph")
# plt.grid()
# plt.show()








# A simple Scatter Plot --------------------------------------------->
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x,y)
# plt.show()


# Comparing two plots on same figure
#  1 plot 
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

# #  2 plot 
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show()





# Color map and Color bars --------------->


# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x,y, c=colors , cmap='Viridis’)
# plt.colorbar()
# plt.show()


# Size and Alpha ----------->

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# plt.scatter(x, y, s=sizes, alpha=0.5)
# plt.show()

# Pie Chart -------------------->

# y = np.array([55, 15, 15, 10])
# plt.pie(y)
# plt.show()

# label in pie chart  --------------->


# y = np.array([55, 15, 15, 10])
# x=["mon","tue","thur","fri"]
# plt.pie(y,labels=x)
# plt.show()


# Explode and shadow --->

# y = np.array([55, 15, 15, 10])
# x=["mon","tue","thur","fri"]
# e=[0.2,0.2,0.2,0]
# plt.pie(y,labels=x,explode=e,shadow=True)
# plt.show()


# Color and legend  -------------------->

# y = np.array([55, 15, 15, 10])
# x=["mon","tue","thur","fri"]
# e=[0.2,0,0,0]
# c=["hotpink","red","orange","yellow"]
# plt.pie(y,labels=x,explode=e,shadow=True,colors=c)
# plt.legend(title="Days")
# plt.show()

# giving auto percentage to  them --------------->
# y = np.array([55, 15, 15, 10])
# mylabels = ["Mon", "Tue", "Wed", "Thur"]
# myexplode = [0.2, 0, 0, 0]
# total=sum(y)
# mycolors = ["white", "hotpink", "b", "#4CAF50"]
# plt.pie(y, labels=mylabels, autopct=lambda p: '{:.0f}%'.format(p * total / 100), explode=myexplode, shadow=True, colors=mycolors)
# plt.legend(title="Days")
# plt.show() 


# Bar plot ------------------------------------------->

x=np.array(["a","b","c","d"])
y=np.array([1,5,3,7])
plt.bar(x,y)
plt.show()

#  to plot the bar in horizontal so use barh() ---------------------------->


# x=np.array(["a","b","c","d"])
# y=np.array([1,5,3,7])

# plt.barh(x,y )
# plt.show()

# histrogram plot -------------->
# Lets create a normal distribution and histogram--------------->

# x = np.random.normal(150, 10, 300)

# print(x)
# plt.hist(x)
# plt.show()
# plt.figure(figsize=(10,10)) 

# x=np.array([10,20,30,40,50])
# y=np.array([5,20,60,80,100])
# plt.hist(x,y)
# plt.figure(figsize=(2,2)) 
# plt.show()











name = 'Aditya'
def msg():
    global name
    name = 'Joshi'
    print('Hello ', name)
msg()
print(name)
