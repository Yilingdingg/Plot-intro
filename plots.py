import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9]
y = [2,4,6,8,10,12,14,16,18]
z = [1,4,9,16,25,36,49,64,81]
# plot diagram
# different markings and colors ro, g^, r--, b--, b-
# plt.plot(x,y,'x')
plt.plot(x,y,'ro', label = "y=x*2")
plt.plot(x,z,'g^', label = "y=x**2")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Time vs Distance")
plt.legend()
plt.show()

x = range(-50,60)
m = 0.2
c = 4
y = []
for i in x :
    temp = (m*i)+ c
    y.append(temp)
plt.plot(x,y,'b-', label=f"y=({m}*x)+{c}")
plt.title("y=mx+p")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# bar plot
# x co ordinate = position of bar
# y coordinate = length of the bar
colors = ['blue','green','red','yellow','orange']
# overlapping if same x, bottom --> stacking
plt.bar(['blue','green','red','yellow','orange'],[15,5,11,2,21], color = 'c', label = 'group 1', width = 0.5)
plt.bar(['blue','green','red','yellow','orange'],[32,12,6,23,7], color = 'm', label = 'group 2', width = 0.5, bottom = [15,5,11,2,21]) 
plt.title("Bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# histogram

ages = [22,55,36,45,21,67,45,23,89,11,33,72,88,67,89,12,6,9,48,75,18] #values
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #intervals
plt.hist(ages, bins, rwidth = 0.7)
plt.xlabel("Age")
plt.ylabel("Intervals")
plt.show()

# scatter plot

x = [1,2,6,8,11]
y = [12,15,9,6,17]
plt.scatter(x,y, label = 'Dots', color= colors, s = 50)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.show()

# pie charts

slices = [26,28,27]
category = ['Class 1', 'Class 2', 'Class 3']
color = ['cyan', 'yellow', 'magenta']
plt.pie(slices, labels = category, colors = color, startangle = 90)
plt.title("Pie Chart")
plt.show()

# stack plot

days = [1,2,3,4,5]
sleeping = [7,8,7,8,8]
eating = [3,2.5,3,3,2.5]
exercising = [1,2,1.5,2,1]
plt.plot([],[], color = 'yellow', label = 'sleeping', linewidth = 4)
plt.plot([],[], color = 'orange', label = 'eating', linewidth = 5)
plt.plot([],[], color = 'red', label = 'exercising', linewidth = 6)
plt.stackplot(days, sleeping, eating, exercising, colors = ['yellow','orange','red'])
plt.title('5 days routine')
plt.xlabel('days')
plt.ylabel('hours')
plt.legend()
plt.show()

# plot division 

p1 = np.arange(0,5,0.5)
p2 = np.arange(0,5,0.5)
p3 = np.cos(2*p2)
plt.figure()
plt.subplot(221)
plt.plot(p1,p2, 'b-')
plt.subplot(224)
plt.plot(p1,p3, 'r-')
plt.show()