#!/usr/bin/python

import numpy as np 
import matplotlib.pyplot as plt


# Difference with respect to periodic boundaries
def periodic_diff(v1,v2,L):
	return ((v1 - v2 + L/2) % L) - L/2


def plot_edges(vertices, edges, L):
	plt.cla()
	for vertex in vertices:
		x = vertex[0]
		y = vertex[1]
		plt.scatter(x, y, c="c")

	for edge in edges:
		i1 = edge[0]
		i2 = edge[1]
		x1,y1 = vertices[i1]
		x2,y2 = vertices[i2]
		v1 = np.array((x1,y1))
		v2 = np.array((x2,y2))
		v2 = v1 + periodic_diff(v2, v1, L)
		x2,y2 = v2
		plt.plot([x1,x2],[y1,y2],c="k")

	plt.axis([0,L[0],0,L[1]])
	plt.show()
	return

cells = np.loadtxt("cell_indices.txt").astype(int)
edges = np.loadtxt("edges_T1.txt").astype(int)
vertices = np.loadtxt("network_vertices.txt")

# Side length of box in x direction
lx = 9 * (2 / (3 * (3**0.5)))**0.5

# Side length of box in y directions
ly = 4 * (2 / (3**0.5))**0.5

L = np.array([lx,ly])

plot_edges(vertices, edges, L)






