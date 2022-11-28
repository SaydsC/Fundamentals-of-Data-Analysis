# practise code 
import numpy as np

# list of data points
speed = [78, 74, 77, 79, 80, 76, 75, 80, 69, 71, 74, 78, 79, 71, 70]
x = np.var(speed)
#sample size 15, SD = 13.17

speed2 = [79, 80, 76, 75, 80, 69, 71, 74, 78, 79]
y = np.var(speed2)
 #sample size 10, SD = 13.29

speed3 = [75, 80, 69, 71, 74]
z = np.var(speed3)
print(z)#sample size 5, SD = 14.16

#Standard deviation is important as it allows you to essentially assess the level of stability in the data. 
# To elaborate, if there is a relatively high standard deviation, 
# then there is high variability in the data. If the standard deviation is relatively low, then there is low variability.