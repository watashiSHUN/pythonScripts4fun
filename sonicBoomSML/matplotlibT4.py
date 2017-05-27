import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.scatter(x,y,label='test',marker="X",s=100)

plt.xlabel('x axis')
plt.ylabel('y-axis')
plt.title('second tutorial')
plt.legend()

plt.show()
