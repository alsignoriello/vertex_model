#!/usr/bin/python
import numpy as np 
from scipy.spatial import Voronoi
import matplotlib.pyplot as plt
from geometry import periodic_diff, euclidean_distance

"""

generate_voronoi.py - generates voronoi diagram
to use as input to vertex model


author: Lexi Signoriello
date: 2/15/16

"""


def plot_vertices(vertices):
	count = 0
	for x,y in vertices:
		plt.scatter(x,y,color="b")
		if x >= 0 and y >= 0:
			if x <= 1 and y <=1:
				count += 1
	print count
	return 

def plot_voronoi(edges, filename, color):
	# plt.cla()
	for edge in edges:
		e1 = edge[0]
		e2 = edge[1]
	
		if -1 not in edge:
			x1,y1 = vertices[edge[0]]
			x2,y2 = vertices[edge[1]]
			plt.plot([x1,x2],[y1,y2],color=color)
	
		else:
			if e1 != -1:
				x,y = vertices[e1]
				plt.scatter(x,y,color="r")
			else:
				x,y = vertices[e2]
				plt.scatter(x,y,color="r")
	
	plt.axis([-0.5,1.5,-0.5,1.5])
	# plt.savefig(filename)
	# plt.close()
	return



# Assumes coordiantes are between 0 and 1 
def tile_coordinates(coords, N):

	# 9 tiles surrounding individual coordinates
	coord_tile = np.zeros((9 * N, 2)) 

	# original coordinates
	coord_tile[:N] = coords

	# upper left 
	coord_tile[N:2*N, 0] = coords[:,0] - 1
	coord_tile[N:2*N, 1] = coords[:,1] + 1

	# directly above
	coord_tile[2*N:3*N, 0] = coords[:,0]
	coord_tile[2*N:3*N, 1] = coords[:,1] + 1

	# upper right
	coord_tile[3*N:4*N, 0] = coords[:,0] + 1
	coord_tile[3*N:4*N, 1] = coords[:,1] + 1

	# right
	coord_tile[4*N:5*N, 0] = coords[:,0] + 1
	coord_tile[4*N:5*N, 1] = coords[:,1]

	# lower right
	coord_tile[5*N:6*N, 0] = coords[:,0] + 1
	coord_tile[5*N:6*N, 1] = coords[:,1] - 1

	# under
	coord_tile[6*N:7*N, 0] = coords[:,0]  
	coord_tile[6*N:7*N, 1] = coords[:,1] - 1

	# lower left
	coord_tile[7*N:8*N,0] = coords[:,0] - 1
	coord_tile[7*N:8*N,1] = coords[:,1] - 1

	# left 
	coord_tile[8*N:,0] = coords[:,0] - 1
	coord_tile[8*N:,1] = coords[:,1]

	return coord_tile



# number of points
N = 48


# L = length of box
lx = 1.
ly = 1.

# generate random coordinates between 0 and 1
coords = np.random.uniform(0,1,size=(N,2))


# To get a configuration that works with periodic boundaries,
# Make a tile 3 x 3 tile with same coordinates
coord_tile = tile_coordinates(coords, N)
# plt.scatter(coord_tile[:,0],coord_tile[:,1])
# plt.show()


# generate voronoi diagram
# vor = Voronoi(coords)
vor = Voronoi(coord_tile)

# vertices corresponding to voronoi cells
vertices = vor.vertices
plot_vertices(vertices)
edges =  vor.ridge_vertices
plot_voronoi(edges, "voronoi_tile.jpg", "k")


# generate voronoi diagram
# vor = Voronoi(coords)
vor = Voronoi(coords)


# vertices corresponding to voronoi cells
vertices = vor.vertices
edges =  vor.ridge_vertices
plot_voronoi(edges, "voronoi.jpg", "c")


# plot lines for axes
plt.plot([0,1], [0,0], color="k")
plt.plot([0,0], [0,1], color="k")
plt.plot([1,1], [0,1], color="k")
plt.plot([1,0], [1,1], color="k")

plt.savefig("voronoi_test.jpg")





# export vertices

# export cells

# export edges











# # scale to box length
# vertices[:,0] = (vertices[:,0] - np.min(vertices[:,0])) / (np.max(vertices[:,0]) - np.min(vertices[:,0]))
# vertices[:,1] = (vertices[:,1] - np.min(vertices[:,1])) / (np.max(vertices[:,1]) - np.min(vertices[:,1]))
# print np.min(vertices[:,0]), np.max(vertices[:,0])
# print np.min(vertices[:,1]), np.max(vertices[:,1])




# Finds edges on boundaries
# # show plot
# count = {}
# matches = []
# for edge in edges:
# 	e1 = edge[0]
# 	e2 = edge[1]
# 	if e1 not in count:
# 		count[e1] = 1
# 	else:
# 		count[e1] += 1
# 	if e2 == -1:
# 		count[e1] -= 1

# 	if e2 not in count:
# 		count[e2] = 1
# 	else:
# 		count[e2] += 1
# 	if e1 == -1:
# 		count[e2] -= 1


# 	if -1 not in edge:
# 		x1,y1 = vertices[edge[0]]
# 		x2,y2 = vertices[edge[1]]
# 		plt.plot([x1,x2],[y1,y2],color="k")

# 	else:
# 		if e1 != -1:
# 			x,y = vertices[e1]
# 			plt.scatter(x,y,color="r")
# 			matches.append((x,y))
# 		else:
# 			x,y = vertices[e2]
# 			plt.scatter(x,y,color="r")
# 			matches.append((x,y))

# for key in count:
# 	if count[key] != 3:
# 		print key, count[key]
