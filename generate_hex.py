#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

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



"""



# hexagonal grid should be spaced as such:
# 0.5 height on y axis
# 0.25 width on x axis
# The final length of the grid should be a scale of:
# 1.5 width 
# 1 height	
# http://www.redblobgames.com/grids/hexagons/	
def generate_grid(nx, ny, w, h):
	# print nx, ny
	# print w,h
	# length of box on x axis
	lx = (nx / 2.) * 1.5 * w

	# length of box on y axis
	ly = ny * h 

	# print lx, ly

	# generate grid of coordinates
	xs = np.linspace(0., lx, 3 * nx + 1)
	xs = xs[:-1] # periodic boundary condition
	# print xs

	ys = np.linspace(0., ly, 2 * ny + 1)
	ys = ys[:-1]  # periodic boundary condition
	# print ys

	xx, yy = np.meshgrid(xs, ys)

	L = [lx,ly]

	return xx, yy, L


def plot_grid(xx, yy, L):
	plt.scatter(xx, yy)
	plt.axis([0, L[0], 0, L[1]])
	# plt.show()
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

		if i % 2 == 0:
			for j in x_left_0:
				indices, curr_v = trace_hexagon(xx, yy, vertices, i, j, curr_v)
				hex_indices[hex_counter, :] = indices 
				hex_counter += 1
		else:
			for j in x_left_1:
				indices, curr_v = trace_hexagon(xx, yy, vertices, i, j, curr_v)
				hex_indices[hex_counter, :] = indices 
				hex_counter += 1				

	return 


def periodic_indices(index, length):
	if index == -1:
		return length - 1
	if index == length:
		return 0
	return index

# trace hexagon vertices -- counter-clockwise
# starting from ix, iy
# add vertices to list if they aren't there already
def trace_hexagon(xx, yy, vertices, ix, iy, v_index):
	
	indices = np.zeros(6)

	# necessary for periodic bounary condition
	len_x = len(xx[0,:])
	len_y = len(yy[:,0])
	# print len_x, len_y

	# counter-clockwise order
	# Index 0 = left corner index
	print ix, iy 
	vx = xx[ix,iy]
	vy = yy[ix,iy]
	print vx, vy

	# Index 1 = right 1, down 1
	ix_1 = periodic_indices(ix + 1, len_x)
	iy_1 = periodic_indices(iy - 1, len_y)
	print ix_1, iy_1
	print xx[ix_1,iy_1]
	print yy[ix_1,iy_1]

	# Index 2 = right 2
	ix_2 = periodic_indices(ix_1 + 2, len_x)
	iy_2 = periodic_indices(iy_1, len_y)
	print ix_2, iy_2

	# Index 3 = up 1, right 1
	ix_3 = periodic_indices(ix_2 + 1, len_x)
	iy_3 = periodic_indices(iy_2 + 1, len_y)
	print ix_3, iy_3

	# Index 4 = up 1, left 1
	ix_4 = periodic_indices(ix_3 - 1, len_x)
	iy_4 = periodic_indices(iy_3 + 1, len_y)
	print ix_4, iy_4

	# Index 5 = left 2
	ix_5 = periodic_indices(ix_4 - 2, len_x)
	iy_5 = periodic_indices(iy_4, len_y)
	print ix_5, iy_5

	# Index 6 == Index 0 = left 1, down 1
	ix_6 = periodic_indices(ix_5 - 1, len_x)
	iy_6 = periodic_indices(iy_5 - 1, len_y)
	print ix_6, iy_6

	# indices = [(ix,iy),(ix_1,iy_1), (ix_2,iy_2), (ix_3,iy_3),
	# 			(ix_4,iy_4), (ix_5,iy_5)]

	plot_hexagon(vertices)


	exit()

	return

def plot_hexagon(vertices):
	for v1,v2 in zip(vertices, vertices[1:] + [vertices[0]]):
		# print i1,i2
		x1 = v1[0]
		y1 = v1[1]
		x2 = v2[0]
		y2 = v2[0]
		plt.plot([x1,x2],[y1,y2],color="k")
	plt.show()
	return


	# # # find position of vertex in list
	# # pos = pos_in_list(vertices, vx, vy)

	# # # if not in list, add it 
	# # if pos == -1:
	# # 	vertices[v_index, 0] = xx[ix,iy]
	# # 	vertices[v_index, 1] = yy[ix,iy]
	# # 	indices[0] = v_index
	# # 	v_index += 1

	# # # Index 1
	# # # diagonal down right
	# # ix = ix + 1
	# # iy = iy - 1

	# # vx = xx[ix,iy]
	# # vy = yy[ix,iy]

	# # # if this vertex = length,
	# # # make it equal to 0 to wrap around
	# # if vx == L[0]:
	# # 	vx = 0.
	# # if vy == L[1]:
	# # 	vy = 0.


	# # # # if this vertex is in list
	# # pos = pos_in_list(vertices, vx, vy)
	# # print pos

	# # if pos == -1:
	# # 	vertices[v_index, 0] = xx[ix,iy]
	# # 	vertices[v_index, 1] = yy[ix,iy]
	# # 	indices[1] = v_index
	# # 	v_index += 1

	# # # Index 2
	# # # right 0.5 w = right 2 indices
	# # ix = ix + 2
	# # vx = xx[ix,iy]
	# # vy = yy[ix,iy]

	# # # if this vertex = length,
	# # # make it equal to 0 to wrap around
	# # if vx == L[0]:
	# # 	vx = 0.
	# # if vy == L[1]:
	# # 	vy = 0.


	# # # # if this vertex is in list
	# # pos = pos_in_list(vertices, vx, vy)

	# # if pos == -1:
	# # 	vertices[v_index, 0] = xx[ix,iy]
	# # 	vertices[v_index, 1] = yy[ix,iy]
	# # 	indices[2] = v_index
	# # 	v_index += 1


	# # # Index 3
	# # # diagonal up right
	# # ix = ix + 1
	# # iy = iy + 1
	# # vx = xx[ix,iy]
	# # vy = yy[ix,iy]

	# # # if this vertex = length,
	# # # make it equal to 0 to wrap around
	# # if vx == L[0]:
	# # 	vx = 0.
	# # if vy == L[1]:
	# # 	vy = 0.


	# # # # if this vertex is in list
	# # pos = pos_in_list(vertices, vx, vy)

	# # if pos == -1:
	# # 	vertices[v_index, 0] = xx[ix,iy]
	# # 	vertices[v_index, 1] = yy[ix,iy]
	# # 	indices[3] = v_index
	# # 	v_index += 1


	# # # Index 4
	# # # diagonal up left
	# # ix = ix - 1
	# # iy = iy + 1
	# # vx = xx[ix,iy]
	# # vy = yy[ix,iy]

	# # # if this vertex = length,
	# # # make it equal to 0 to wrap around
	# # if vx == L[0]:
	# # 	vx = 0.
	# # if vy == L[1]:
	# # 	vy = 0.


	# # # # if this vertex is in list
	# # pos = pos_in_list(vertices, vx, vy)

	# # if pos == -1:
	# # 	vertices[v_index, 0] = xx[ix,iy]
	# # 	vertices[v_index, 1] = yy[ix,iy]
	# # 	indices[4] = v_index
	# # 	v_index += 1

	# # # Index 5
	# # # left 0.5 w = left 2 indices
	# # ix = ix - 2
	# # vx = xx[ix,iy]
	# # vy = yy[ix,iy]

	# # # if this vertex = length,
	# # # make it equal to 0 to wrap around
	# # if vx == L[0]:
	# # 	vx = 0.
	# # if vy == L[1]:
	# # 	vy = 0.


	# # # # if this vertex is in list
	# # pos = pos_in_list(vertices, vx, vy)

	# # if pos == -1:
	# # 	vertices[v_index, 0] = xx[ix,iy]
	# # 	vertices[v_index, 1] = yy[ix,iy]
	# # 	indices[5] = v_index
	# # 	v_index += 1


	# # # Index 6 should be index 0
	# # # Check this is true
	# # # Else: throw error
	# # # diagonal down left
	# # ix = ix - 1
	# # iy = iy - 1
	# # vx = xx[ix,iy]
	# # vy = yy[ix,iy]

	# # # if this vertex = length,
	# # # make it equal to 0 to wrap around
	# # if vx == L[0]:
	# # 	vx = 0.
	# # if vy == L[1]:
	# # 	vy = 0.


	# # if vx != vertices[indices[0]][0]:
	# # 	print "fuck"
	# # if vy != vertices[indices[0]][1]:
	# # 	print "fuck"


	# # return indices, v_index
	# return 


		
def pos_in_list(vertices, x, y):
	pos = -1 
	for j,v in enumerate(vertices):
		if v[0] == x and v[1] == y:
			return j
	return pos


def scale_area():
	pass


def gaussian_noise():
	pass





def main():

	# Number of hexagons across x axis
	nx = 4
	# should be a factor of 2 across x axis
	if nx % 2 != 0:
		print "Number of hexagons on x axis should be a multiple of 2"
		nx += 1

	# Number of hexagons across y axis
	ny = 3
	# if ny % 2 != 0:
	# 	print "Number of hexagons on y axis should be a multiple of 2"
	# 	ny += 1

	# # side length of hexagon such that area = 1
	# s = (2)**(0.5) / (3 * (3)**0.5)**(0.5)

	# # width
	# w = 2. * s

	# # height
	# h = (3**(0.5) / 2.) * w

	# 1 for testing purposes
	w = 1.
	h = 1.

	# generate correctly spaced points on the grid
	# will be more hexagons later due to periodic boundaries
	xx, yy, L = generate_grid(nx, ny, w, h)


	# plot coordinates 
	plot_grid(xx, yy, L)

	# trace vertices for hexagons
	# return list of vertices
	# list of cell indices in counter-clockwise order
	trace_hex_vertices(nx, ny, xx, yy, w, h, L)

	# plot hexagons 
	# plot_hexagons(xx, yy, L)

	# scale the area 


	# add noise


	# write vertices


	# write cells


	# write edges





if __name__ == "__main__":
	main()




# def plot_hexagons(xx, yy, L):
# 	print xx.shape
# 	print yy.shape

# 	# Polygon 1

# 	# Height 0
# 	x1 = xx[0,1]
# 	x2 = xx[0,2]
# 	y1 = yy[0,1]
# 	y2 = yy[0,2]
# 	plt.plot([x1,x2],[y1,y2],color="m")

# 	x1 = xx[0,2]
# 	x2 = xx[0,3]
# 	y1 = yy[0,2]
# 	y2 = yy[0,3]
# 	plt.plot([x1,x2],[y1,y2],color="m")

	
# 	# Height 1 = intervals of 2
# 	x1 = xx[2,1]
# 	x2 = xx[2,2]
# 	y1 = yy[2,1]
# 	y2 = yy[2,2]
# 	plt.plot([x1,x2],[y1,y2],color="m")

# 	x1 = xx[2,2]
# 	x2 = xx[2,3]
# 	y1 = yy[2,2]
# 	y2 = yy[2,3]
# 	plt.plot([x1,x2],[y1,y2],color="m")

# 	# Side 1
# 	x1 = xx[0,1]
# 	x2 = xx[1,0]
# 	y1 = yy[0,1]
# 	y2 = yy[1,0]
# 	plt.plot([x1,x2],[y1,y2],color="m")

# 	# Side 2
# 	x1 = xx[2,1]
# 	x2 = xx[1,0]
# 	y1 = yy[2,1]
# 	y2 = yy[1,0]
# 	plt.plot([x1,x2],[y1,y2],color="m")
	
# 	# Side 3
# 	x1 = xx[0,3]
# 	x2 = xx[1,4]
# 	y1 = yy[0,3]
# 	y2 = yy[1,4]
# 	plt.plot([x1,x2],[y1,y2],color="m")

# 	# Side 4
# 	x1 = xx[2,3]
# 	x2 = xx[1,4]
# 	y1 = yy[2,3]
# 	y2 = yy[1,4]
# 	plt.plot([x1,x2],[y1,y2],color="m")


# 	plt.show()

# 	return
