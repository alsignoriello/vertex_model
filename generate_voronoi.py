#!/usr/bin/python
import numpy as np 
from scipy.spatial import Voronoi
import matplotlib.pyplot as plt


"""

generate_voronoi.py - generates voronoi diagram
to use as input to vertex model


author: Lexi Signoriello
date: 2/15/16

"""


def plot_bounds(x_min, x_max, y_min, y_max, color):
	plt.plot([x_min,x_max], [y_min,y_min], color=color)
	plt.plot([x_min,x_min], [y_min,y_max], color=color)
	plt.plot([x_max,x_max], [y_min,y_max], color=color)
	plt.plot([x_max,x_min], [y_max,y_max], color=color)
	return

def plot_vertices(vertices, color):
	for x,y in vertices:
		plt.scatter(x,y,color=color)
	return 

# edges correspond to indices of vertices
def plot_voronoi(vertices, edges, color):
	for edge in edges:
		e1 = edge[0]
		e2 = edge[1]
	
		if -1 not in edge:
			x1,y1 = vertices[edge[0]]
			x2,y2 = vertices[edge[1]]
			plt.plot([x1,x2],[y1,y2],color=color)

	return


# get vertices with respect to periodic boundaries
def get_vertices(vertices, x_min, x_max, y_min, y_max):
	count = 0
	v = []
	index_map = {}
	for i,(x,y) in enumerate(vertices):
		if x >= x_min and y >= y_min:
			if x <= x_max and y <= y_max:
				index_map[i] = len(v)
				v.append((x,y))
				count += 1
	print "There are %d vertices\n" % count 

	return np.array(v), index_map

# get edges with respect to periodic boundaries
# vertices and edges are from voronoi with tiled coordinates
def get_edges(vertices, edges, index_map, L):
	e = []
	for edge in edges:
		i1 = edge[0]
		i2 = edge[1]

		# Case 1: i1 and i2 in index map
		# Append indices for vertex list wrt periodic bounds
		if i1 in index_map and i2 in index_map:
			e.append((index_map[i1],index_map[i2]))

		# Case 2: neither in index map
		# Do nothing

		# Case 3: i1 or i2 in index map
		# 		  but not both 
		# Because of periodicity, this edge needs to have a 
		# connecting edge that wraps around
		if i1 in index_map and i2 not in index_map:
			# find the vertex that it "wraps around" to
			# v = vertex in plane
			v = np.array(vertices[i1])
			# v1 = vertex out of plane
			v1 = np.array(vertices[i2])

			# print v1
			if v1[0] < 0:
				v1[0] = 1 + v1[0]

			if v1[0] > L[0]:
				v1[0] = v1[0] - 1

			if v1[1] < 0:
				v1[1] = 1 + v1[1]

			if v1[1] > L[0]:
				v1[1] = v1[1] - 1

			# print v, v1

			# # # find index of this vertex 
			for key in index_map:
				if abs(vertices[key][0] - v1[0]) < 10**-6:
					e.append((index_map[i1], index_map[key]))
					# print "yes"


		# include this IF you want duplicate edges...
		# if i1 not in index_map and i2 in index_map:
		# 	# find the vertex that it "wraps around" to
		# 	# v = vertex in plane
		# 	v = np.array(vertices[i2])
		# 	# v1 = vertex out of plane
		# 	v1 = np.array(vertices[i1])


		# 	# print v1
		# 	if v1[0] < 0:
		# 		v1[0] = 1 + v1[0]

		# 	if v1[0] > L[0]:
		# 		v1[0] = v1[0] - 1

		# 	if v1[1] < 0:
		# 		v1[1] = 1 + v1[1]

		# 	if v1[1] > L[0]:
		# 		v1[1] = v1[1] - 1

		# 	# print v, v1

		# 	# # find index of this vertex 
		# 	for key in index_map:
		# 		if abs(vertices[key][0] - v1[0]) < 10**-6:
		# 			e.append((index_map[i2], index_map[key]))
		# 			# print "yes"


	return e


# get cells
def get_cells(vertices, edges):
	
	cells = {}


	# cycle through cells
	for i,vertex in enumerate(vertices):

		# find edges associated with this vertex
		for edge in edges:
			




	return cells


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



np.random.seed([1938420])

# number of points
N = 48

x_min = 0.
x_max = 1.
y_min = 0.
y_max = 1.

L = np.array([x_max, y_max])

# generate random coordinates between 0 and 1
coords = np.random.uniform(x_min, x_max, size=(N,2))

# To get a configuration that works with periodic boundaries,
# Make a tile 3 x 3 tile with same coordinates
coord_tile = tile_coordinates(coords, N)

# generate voronoi diagram for tiled boxes
vor = Voronoi(coord_tile)


tile_vertices = vor.vertices
plot_vertices(tile_vertices, "k")

tile_edges = vor.ridge_vertices
plot_voronoi(tile_vertices, tile_edges, "k")

# get vertices for cells in center tile
vertices, index_map = get_vertices(tile_vertices, x_min, x_max, y_min, y_max)
plot_vertices(vertices, "c")

# plot boundaries
plot_bounds(x_min, x_max, y_min, y_max, "m")
plt.axis([-0.5,1.5,-0.5,1.5])

# for key in index_map:
# 	print key, index_map[key]


edges = get_edges(tile_vertices, tile_edges, index_map, L)
# plotting routine does not understand periodic boundaries currently...
# plot_voronoi(vertices, edges, "c")
# plt.savefig("voronoi_periodic.jpg")

cells = get_cells(vertices, edges)

# ADD CHECK TO ASSERT CYCLES ARE IN COUNTER CLOCKWISE ORDER!!



# Write data to text files

# write vertices
np.savetxt("voronoi_vertices.txt", vertices)


# write edges
np.savetxt("voronoi_edges.txt", edges, fmt="%d")

# write cells




























# # generate voronoi diagram
# # vor = Voronoi(coords)
# vor = Voronoi(coords)

# # vertices corresponding to voronoi cells
# vertices = vor.vertices
# edges =  vor.ridge_vertices
# plot_voronoi(vertices, edges, "voronoi.jpg", "c")

# plt.savefig("voronoi_test.jpg")

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