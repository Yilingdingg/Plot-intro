import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y= [2,4,6,8,10,12,14,16,18]
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
