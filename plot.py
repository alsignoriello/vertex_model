import matplotlib.pyplot as plt
import sys
from parser import *
from geometry import periodic_diff

"""

plot.py - plots the network for vertex model


author: Lexi Signoriello
date: 1/19/16

[vertices] [edges]

options:
	vertices

	line color

	color by number of neighbors
	color by area


"""


def plot_network(vertices, poly, L, file):
	plt.cla()
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	# for x,y in vertices:
	# 	ax.scatter(x, y, c="m", marker=".", s=100)

	for poly in poly:
		indices = poly.indices
		for i,index in enumerate(indices):
			x1,y1 = vertices[index]
			if i == len(indices) - 1:
				x2,y2 = vertices[indices[0]]
			else:
				x2,y2 = vertices[indices[i+1]]

			v1 = np.array((x1,y1))
			v2 = np.array((x2,y2))
			v2 = v1 + periodic_diff(v2, v1, L)
			x2,y2 = v2
			ax.plot([x1,x2], [y1,y2], c="c")

			v2 = np.array((x2,y2))
			v1 = v2 + periodic_diff(v1, v2, L)
			x1,y1 = v1
			ax.plot([x1,x2], [y1,y2], c="c")


		# # plot centers
		x,y = poly.get_center(vertices, L)
		if x <= 0:
			x = x + L[0]
		if x >= L[0]:
			x = x - L[0]
		if y <= 0:
			y = y + L[1]
		if y >= L[1]:
			y = y - L[1]
		
		plt.scatter(x,y,color="c", marker=".")

	# remove axis ticks
	ax.axes.get_xaxis().set_ticks([])
	ax.axes.get_yaxis().set_ticks([])

	ax.axis([0,L[0],0,L[1]])
	plt.savefig(file)
	plt.close(fig)
	return

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


# # Plots to test T1 transition
# def plot_4_poly(vertices, poly, i1, i2, L, file, E):
# 	plt.cla()
# 	x1,y1 = vertices[i1]
# 	x2,y2 = vertices[i2]
# 	plt.scatter(x1,y1,color="r",marker="*")
# 	plt.scatter(x2,y2,color="m",marker="*")

# 	colors = ["c", "r", "g", "m"]
# 	for i,cell in enumerate(cells):
# 		indices = cell.indices
# 		for e1,e2 in zip(indices,np.concatenate((indices[1:],[indices[0]]))):
# 			x1,y1 = vertices[e1]
# 			x2,y2 = vertices[e2]
# 			plt.plot([x1,x2], [y1,y2], color=colors[i])

# 	plt.axis([0,L[0]+0.2,0,L[1]+0.2])
# 	plt.title("Energy = %f" % E)
# 	plt.savefig(file)
# 	return

# def plot_6_indices(vertices, indices):
# 	colors = ["c", "r", "g", "m", "k", "b"]
# 	print indices
# 	for i,index in enumerate(indices):
# 		x,y = vertices[index]
# 		plt.scatter(x,y,color=colors[i],marker="*")
# 	plt.show()
# 	return 

# def plot_10_edges(vertices, edges, L):

# 	for edge in edges:
# 		x1,y1 = vertices[edge[0]]
# 		x2,y2 = vertices[edge[1]]
# 		plt.plot([x1,x2],[y1,y2],color="k")
# 	plt.show()
# 	return





