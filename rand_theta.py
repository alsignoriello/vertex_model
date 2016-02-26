#!/usr/bin/python
import numpy as np 
import matplotlib.pyplot as plt
from math import sin, cos, pi
from geometry import unit_vector, magnitude


def plot_hex(vertices, indices, count):
	plt.cla()
	for i in indices:
		plt.scatter(vertices[i,0],vertices[i,1],color="m")

		if i != len(indices) - 1:
			plt.plot([vertices[i,0],vertices[i+1,0]],
				[vertices[i,1],vertices[i+1,1]],color="k")
		else:
			plt.plot([vertices[i,0],vertices[0,0]],
				[vertices[i,1],vertices[0,1]],color="k")
	plt.axis([-10,10,-10,10])
	plt.savefig("move/%d.jpg" % count)
	plt.close()



# generate hexagon
vertices = np.zeros((6,2))
x0 = 0.
y0 = 0.5
vertices[0,0] = x0
vertices[0,1] = y0

x1 = 0.5
y1 = 0.
vertices[1,0] = x1
vertices[1,1] = y1

x2 = 1.
y2 = 0.
vertices[2,0] = x2
vertices[2,1] = y2

x3 = 1.5
y3 = 0.5
vertices[3,0] = x3
vertices[3,1] = y3

x4 = 1.
y4 = 1.
vertices[4,0] = x4
vertices[4,1] = y4

x5 = 0.5
y5 = 1.
vertices[5,0] = x5
vertices[5,1] = y5


indices = [0,1,2,3,4,5]

# plot_hex(vertices,indices)

delta_t = 0.05

for i in range(0,50):

	xa = np.random.uniform(-pi, pi)
	ya = np.random.uniform(-pi, pi)
	
	x = sin(xa)
	y = cos(ya)
	# print x,y
	v1 = np.array([x,y])
	v2 = np.array([0,0])
	
	
	uv = unit_vector(v1,v2)
	# print uv
	# print magnitude(uv)

	vertices = vertices +  uv
	plot_hex(vertices, indices, i)





