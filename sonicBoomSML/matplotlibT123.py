import matplotlib.pyplot as plt
# plot x's and y's
x1 = [1,2,3]
# in practice, pass the x1 to your f, output y1
y1 = [1,2,3]

x2 = [1,2,3]
y2 = [4,5,6]

x3 = [0.5,1,1.5,2,2.5,3]
y3 = [10,5,8,2,1,3]

# width is represented by absolute value, 0.2 means it from x=0 ==> x=0.2
plt.bar(x3,y3,label="bar chart",color="r",width=0.2,edgecolor="black")
plt.plot(x1,y1,label="first line")
plt.plot(x2,y2,label="second line")
# once this function is invoked, the graph is finished at background
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('basic graph test')
plt.legend()
# plt.show bring it to the front
plt.show()
