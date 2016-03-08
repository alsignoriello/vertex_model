import numpy as np 
from geometry import get_angle_points, get_angle_vectors
import matplotlib.pyplot as plt
from math import pi

def plot_6_indices(vertices, indices):
	colors = ["c", "r", "g", "m", "k", "b"]
	print indices
	for i,index in enumerate(indices):
		x,y = vertices[index]
		plt.scatter(x,y,color=colors[i],marker="*")
	plt.show()
	return 

def plot_angle(p1, p2, p3):
	plt.scatter(p1[0], p2[1], color="c")
	plt.scatter(p2[0], p2[1], color="c")
	plt.scatter(p3[0], p3[1], color="c")
	plt.plot([p1[0],p2[0]], [p1[1],p2[1]], color="k")
	plt.plot([p1[0],p3[0]], [p1[1],p3[1]], color="k")
	plt.show()
	return


# # angle between 3 points
# x1 = 0.
# y1 = 0.
# p1 = np.array([x1,y1])

# x2 = 1.
# y2 = 0.
# p2 = np.array([x2,y2])

# x3 = 0.
# y3 = -1.
# p3 = np.array([x3,y3])

# plot_angle(p1,p2,p3)
# print get_angle_points(p1,p2,p3) * (360 / (2 * pi))
# print get_angle_vectors(p2,p3) * (360 / (2 * pi))

vertices = []
vertices.append((0, 0.5))
vertices.append((0.5, 0))
vertices.append((1, 0))
vertices.append((1.5, 0.5))
vertices.append((1, 1))
vertices.append((0.5, 1))

indices1 = [0,1,2,3,4,5]
indices2 = [5,4,3,2,1,0]


print vertices
# plot_6_indices(vertices, indices)

print vertices[0]
print vertices[1]
v1 = np.array(vertices[0]) - np.array(vertices[1])

print vertices[1]
print vertices[2]
v2 = np.array(vertices[1]) - np.array(vertices[2])

# v1 -> v2
delta =  (v1[0] * v2[1]) - (v1[1] * v2[0])
print delta


# assure reverse is negative..

print vertices[0]
print vertices[1]
v2 = np.array(vertices[1]) - np.array(vertices[0])

print vertices[1]
print vertices[2]
v1 = np.array(vertices[2]) - np.array(vertices[1])

# v1 -> v2
delta =  (v1[0] * v2[1]) - (v1[1] * v2[0])
print delta



# print delta

# if delta is positive
# then p3 is to the left of p2

# if delta is negative 
# then p3 is to the right of p2

# if delta is 0
# then p3 is the opposite direction of p2