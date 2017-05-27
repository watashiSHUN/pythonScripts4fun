import matplotlib.pyplot as plt

fig = plt.figure()
center = (1,1)
radius = 0.5
c1 = plt.Circle(center,radius)

ax = fig.add_subplot(111)
ax.add_artist(c1)
plt.show()
