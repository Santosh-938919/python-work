# Pie chart 
import matplotlib.pyplot as plt 
import numpy as np 
y = np.array([55, 15, 15, 10]) 
mylabels = ["Mon", "Tue", "Wed", "Thur"] 
plt.pie(y, labels=mylabels) 
plt.show()