#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from parser import build_cells
from plot import plot_network
import random

"""

generate_network.py - generates a random vertex network 


generates hexagonal network 
with hexagon area = 1
scale the area 
adds noise

author: Lexi Signoriello
date: 2/1/16


Area = ((3 * sqrt(3)) / 2) * s^2
where s = side length

nx = number of hexagons in x direction
ny = number of hexagons in y direction

The hexagons are generated flat topped
	* can be transformed to be flat sided with rotation

NOTE: numpy matrix == [x,y]
	  Grid matrix  == [y,x]


"""



# hexagonal grid should be spaced as such:
# 0.5 height on y axis
# 0.25 width on x axis
# The final length of the grid should be a scale of:
# 1.5 width 
# 1 height	
# http://www.redblobgames.com/grids/hexagons/	
def generate_grid(nx, ny, w, h):

	# length of box on x axis
	lx = (nx / 2.) * 1.5 * w

	# length of box on y axis
	ly = ny * h 

	# generate grid of coordinates
	xs = np.linspace(0., lx, 3 * nx + 1)
	xs = xs[:-1] # periodic boundary condition

	ys = np.linspace(0., ly, 2 * ny + 1)
	ys = ys[:-1]  # periodic boundary condition

	xx, yy = np.meshgrid(xs, ys)

	L = np.array((lx,ly))

	return xx, yy, L


def plot_grid(xx, yy, L):
	plt.scatter(xx, yy)
	plt.axis([0, L[0], 0, L[1]])
	plt.show()
	return 


def trace_hex_vertices(nx, ny, xx, yy, w, h, L):
	n_hex = nx * ny
	print "There are %d hexagons" % n_hex

	# indices in counter-clockwise order
	hex_indices = np.zeros((n_hex, 6))

	# each vertex has 3 polygons attached
	n_vertices = (6 * n_hex) / 3

	# list of x,y vertices
	vertices = np.zeros((n_vertices, 2))
	vertices.fill(-1)

	# left corner indices
	x_left_0 = []
	x_left_1 = []
	for i in range(0,len(xx[0,:]),3):
		if i % 2 == 0:
			x_left_1.append(i)
		if i % 2 != 0:
			x_left_0.append(i)

	# keep track of vertices and indices
	curr_v = 0 # current vertex
	hex_counter = 0
	for i in range(0, 2 * ny):
		iy = i
		if i % 2 == 0:
			for j in x_left_0:
				ix = j
				indices = trace_hexagon(xx, yy, vertices, ix, iy, L)
				hex_indices[hex_counter, :] = indices 
				hex_counter += 1
		else:
			for j in x_left_1:
				ix = j
				indices = trace_hexagon(xx, yy, vertices, ix, iy, L)
				hex_indices[hex_counter, :] = indices 
				hex_counter += 1				

	return vertices, hex_indices


def periodic_indices(index, length):
	if index == -1:
		return length - 1
	if index == length:
		return 0
	return index

		

# if vertex is already in list
# return the index of the vertex
# else
# add vertex to vertices
# return index
def pos_in_list(vertices, x, y):

	for j,v in enumerate(vertices):
		if v[0] == x and v[1] == y:
			return j
		if v[0] == -1 and v[1] == -1:
			vertices[j][0] = x
			vertices[j][1] = y
			return j
	# should always return an index
	# Error if not
	return -1


# trace hexagon vertices -- counter-clockwise
# starting from ix, iy
# add vertices to list if they aren't there already
def trace_hexagon(xx, yy, vertices, ix, iy, L):
	
	# counter-clockwise indices for vertices in hexagon
	indices = np.zeros(6)

	# necessary for periodic bounary condition
	len_x = len(xx[0,:])
	len_y = len(yy[:,0])

	# counter-clockwise order
	# Index 0 = left corner index 
	vx = xx[iy,ix]
	vy = yy[iy,ix]
	pos = pos_in_list(vertices, vx, vy)
	indices[0] = pos

	# Index 1 = right 1, down 1
	ix_1 = periodic_indices(ix + 1, len_x)
	iy_1 = periodic_indices(iy - 1, len_y)
	vx = xx[iy_1,ix_1]
	vy = yy[iy_1,ix_1]
	pos = pos_in_list(vertices, vx,vy)
	indices[1] = pos

	# Index 2 = right 2
	ix_2 = periodic_indices(ix_1 + 2, len_x)
	iy_2 = periodic_indices(iy_1, len_y)
	vx = xx[iy_2, ix_2]
	vy = yy[iy_2, ix_2]
	pos = pos_in_list(vertices, vx, vy)
	indices[2] = pos

	# Index 3 = up 1, right 1
	ix_3 = periodic_indices(ix_2 + 1, len_x)
	iy_3 = periodic_indices(iy_2 + 1, len_y)
	vx = xx[iy_3, ix_3]
	vy = yy[iy_3, ix_3]
	pos = pos_in_list(vertices, vx, vy)
	indices[3] = pos

	# Index 4 = up 1, left 1
	ix_4 = periodic_indices(ix_3 - 1, len_x)
	iy_4 = periodic_indices(iy_3 + 1, len_y)
	vx = xx[iy_4, ix_4]
	vy = yy[iy_4, ix_4]
	pos = pos_in_list(vertices, vx, vy)
	indices[4] = pos

	# Index 5 = left 2
	ix_5 = periodic_indices(ix_4 - 2, len_x)
	iy_5 = periodic_indices(iy_4, len_y)
	vx = xx[iy_5, ix_5]
	vy = yy[iy_5, ix_5]
	pos = pos_in_list(vertices, vx, vy)
	indices[5] = pos

	# Index 6 == Index 0 = left 1, down 1
	ix_6 = periodic_indices(ix_5 - 1, len_x)
	iy_6 = periodic_indices(iy_5 - 1, len_y)
	vx = xx[iy_6, ix_6]
	vy = yy[iy_6, ix_6]
	if ix_6 != ix and iy_6 != iy:
		print "Did not cycle back to vertex"

	return indices



# Make polygons = area != 1
def scale_area():
	pass


# shift vertices randomly
def shift_vertices(vertices, s):
	for i,(x,y) in enumerate(vertices):
		x += random.uniform(-s/2.,s/2.)
		y += random.uniform(-s/2.,s/2.)
		vertices[i,0] = x
		vertices[i,1] = y
	return vertices


def write_edges(indices):
	pass



def main():

	# Number of hexagons across x axis
	nx = 4
	# should be a factor of 2 across x axis
	if nx % 2 != 0:
		print "Number of hexagons on x axis should be a multiple of 2"
		nx += 1

	# Number of hexagons across y axis
	ny = 4

	# side length of hexagon such that area = 1
	s = (2)**(0.5) / (3 * (3)**0.5)**(0.5)

	# width
	w = 2. * s

	# height
	h = (3**(0.5) / 2.) * w

	# # 1 for testing purposes
	# w = 1.
	# h = 1.

	# generate correctly spaced points on the grid
	# will be more hexagons later due to periodic boundaries
	xx, yy, L = generate_grid(nx, ny, w, h)


	# plot coordinates 
	# plot_grid(xx, yy, L)

	# trace vertices for hexagons
	# return list of vertices
	# list of cell indices in counter-clockwise order
	vertices, hex_indices = trace_hex_vertices(nx, ny, xx, yy, w, h, L)

	# build cells
	cells = build_cells(hex_indices, 0.65, 3)

	# scale the area to not be = 1
	scale_area()

	# add noise
	# pass side length so shift is reasonable
	vertices = shift_vertices(vertices, s)

	# plot network
	plot_network(vertices, cells, L, "hex_test.jpg")

	# write vertices
	np.savetxt("hex_vertices.txt", vertices)

	# write cells
	np.savetxt("hex_indices.txt", hex_indices, fmt="%d")


	# write edges
	write_edges(hex_indices)



if __name__ == "__main__":
	main()


