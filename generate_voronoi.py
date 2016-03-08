#!/usr/bin/python
import numpy as np 
from scipy.spatial import Voronoi
import matplotlib.pyplot as plt
from geometry import periodic_diff
from math import pi
from plot import plot_network
from parser import build_cells


"""

generate_voronoi.py - generates voronoi diagram
to use as input to vertex model


author: Lexi Signoriello
date: 2/15/16

"""


def adjacency_matrix(vertices, edges):
	n = len(vertices)
	matrix = np.zeros((n,n))
	for i1,i2 in edges:
		matrix[i1,i2] = 1
	return matrix




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

def plot_cell(vertices, indices):
	for i1,i2 in zip(indices, indices[1:] + [indices[0]]):
		x1,y1 = vertices[i1]
		x2,y2 = vertices[i2]
		plt.scatter(x1,y1,color="c")
		plt.scatter(x2,y2,color="c")
		plt.plot([x1,x2],[y1,y2],color="r")
	plt.show()
	return

def plot_edges(vertices, edges, L):
	for i1,i2 in edges:
		x1,y1 = vertices[i1]
		x2,y2 = vertices[i2]
		# plt.plot([x1,x2],[y1,y2],color="r")

		v1 = np.array((x1,y1))
		v2 = np.array((x2,y2))
		v2 = v1 + periodic_diff(v2, v1, L)
		x2,y2 = v2
		plt.plot([x1,x2],[y1,y2],c="r")

		v2 = np.array((x2,y2))
		v1 = v2 + periodic_diff(v1, v2, L)
		x1,y1 = v1
		plt.plot([x1,x2],[y1,y2],c="r")

	return



# get vertices with respect to periodic boundaries
def get_vertices(vertices, x_min, x_max, y_min, y_max):
	count = 0
	v = []
	index_map = {}
	for i,(x,y) in enumerate(vertices):
		if x >= x_min and y >= y_min:
			if x <= x_max and y <= y_max:
				curr_indx = len(v)
				index_map[i] = curr_indx
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
			e.append((index_map[i2],index_map[i1]))

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
		if i1 not in index_map and i2 in index_map:
			# find the vertex that it "wraps around" to
			# v = vertex in plane
			v = np.array(vertices[i2])
			# v1 = vertex out of plane
			v1 = np.array(vertices[i1])


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

			# # find index of this vertex 
			for key in index_map:
				if abs(vertices[key][0] - v1[0]) < 10**-6:
					e.append((index_map[i2], index_map[key]))
					# print "yes"


	return e


def get_new_index_map(vertices, v, index_map):

	# add indices mapping to new vertices outside of bounds
	for i,(x,y) in enumerate(vertices):
		x1 = -100
		y1 = -100

		if x < x_min and x > -1.:
			x1 = x + 1.

		if x > x_max and x < 2.:
			x1 = x - 1.

		if y < y_min and y > -1.:
			y1 = y + 1.

		if y > y_max and y < 2.:
			y1 = y - 1.

		if x1 != -100 and y1 != -100:
			# look up new x,y in list
			for j,(x2,y2) in enumerate(v):
				if abs(x1 - x2) < 10**-6:
					if abs(y1 - y2) < 10**-6:
						index_map[i] = j

	return index_map

# get cells
# iterate over edges, building cycles
def get_cells(regions, index_map):

	cells = []

	for region in vor.regions:
		count = 0
		cell = []
		for index in region:
			if index in index_map:
				count += 1
				# print index_map[index]
				cell.append(index_map[index])
		if count == len(region):
			cells.append(cell)

	print len(cells)
	for cell in cells:
		print cell
	
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
# plot_vertices(tile_vertices, "k")

tile_edges = vor.ridge_vertices
# plot_voronoi(tile_vertices, tile_edges, "k")


# get vertices for cells in center tile
vertices, index_map = get_vertices(tile_vertices, x_min, x_max, y_min, y_max)
# plot_vertices(vertices, "c")

# # plot boundaries
# plot_bounds(x_min, x_max, y_min, y_max, "m")
# plt.axis([-0.5,1.5,-0.5,1.5])

# for key in index_map:
# 	print key, index_map[key]


edges = get_edges(tile_vertices, tile_edges, index_map, L)
print len(edges)



# plot_voronoi(vertices, edges, "c")
# plt.savefig("voronoi_periodic.jpg")

index_map = get_new_index_map(tile_vertices, vertices, index_map)

regions = vor.regions
cells = get_cells(regions, index_map)
print cells

# build cells
cell_class = build_cells(cells, 1, 1, 0.)

plot_network(vertices, cell_class, L, "voronoi_test.jpg")


exit()



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




# if edges were always to the left...
# not true..

# if edge2[0] == cell[-1] and edge2[1] != cell[-2]:
# 	print cell[-2], cell[-1], edge2[0], edge2[1]
# 	print vertices[cell[-2]], vertices[cell[-1]], vertices[edge2[1]]
# 	i0 = cell[-2]
# 	i1 = cell[-1]
# 	i2 = edge2[0]
# 	i3 = edge2[1]
# 	v1 = vertices[i0] - vertices[i1]
# 	v2 = vertices[i2] - vertices[i3]
# 	delta = (v1[0] * v2[1]) - (v1[1] * v2[0])
# 	print delta


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





# first attempt to find cycles....

	# cells = []
	# edge_used = np.zeros(len(edges))
	# cell_count = 0
	
	# for i,edge in enumerate(edges):

	# 	# if this edge is not used
	# 	if edge_used[i] != 1:
	# 		i1, i2 = edge

	# 		cell = []
	# 		cell.append(i1)
	# 		cell.append(i2)

	# 		cycle = False
	# 		edge_used[i] = 1

	# 		while cycle == False:
	# 			# every vertex should have 2 edges 
	# 			# other than the edge leading to current vertex
	# 			# choose the edge that cycles counter-clockwise, ie, smallest angle
	# 			min_angle = 2. * pi
	# 			next_i = -1 
	# 			edge_idx = -1

	# 			for j,edge2 in enumerate(edges):

	# 				if edge_used[j] != 1:

	# 					if i2 == edge2[0]: #  and edge2[1] != i1: not necessary because edge_used
	# 						# print i1, i2, edge2[0], edge2[1]	
	# 						v1 = vertices[i1]
	# 						v2 = vertices[i2]
	# 						v3 = vertices[edge2[1]]	
	# 						angle = get_angle(v2, v1, v3)
	# 						# print angle
	# 						if angle < min_angle:
	# 							min_angle = angle
	# 							next_i = edge2[1]
	# 							edge_idx = j
	
	# 					if i2 == edge2[1]: #and edge2[0] != i1:
	# 						# print i1, i2, edge2[0], edge2[1]				
	# 						v1 = vertices[i1]
	# 						v2 = vertices[i2]
	# 						v3 = vertices[edge2[0]]		
	# 						angle = get_angle(v2, v1, v3)
	# 						# print angle
	# 						if angle < min_angle:
	# 							min_angle = angle
	# 							next_i = edge2[0]
	# 							edge_idx = j


	# 			# print min_angle, next_i, edge_idx
	# 			# print min_angle, next_i, edge_idx
	# 			if next_i == cell[0]:
	# 				cycle = True
	# 				# ADD CHECK TO ASSERT CYCLES ARE IN COUNTER CLOCKWISE ORDER!!
	# 				# REVERSE ORDER IF NOT!
	# 				# print cell
	# 				plot_cell(vertices, cell)
	# 				cells.append(cell)
	# 				cell_count += 1

	# 			if next_i != -1 and cycle == False:
	# 				cell.append(next_i)
	# 				edge_used[edge_idx] = 1
	# 				i1 = i2
	# 				i2 = next_i

	# 			if next_i == -1:
	# 				# print "wtf"
	# 				plot_cell(vertices, cell)
	# 				exit()

	# 			print min_angle, next_i, edge_idx, cell
