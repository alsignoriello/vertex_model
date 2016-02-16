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

	# print lx,ly

	# generate grid of coordinates
	xs = np.linspace(0., lx, 3 * nx + 1)
	# print xs

	ys = np.linspace(0., ly, 2 * ny + 1)
	# print ys

	xx, yy = np.meshgrid(xs, ys)

	L = [lx,ly]

	return xx, yy, L


def plot_grid(xx, yy, L):
	plt.scatter(xx, yy)
	plt.axis([0, L[0], 0, L[1]])
	plt.show()
	return 



def trace_hex_vertices(nx, ny, xx, yy, w, h):

	n_cells = nx * ny
	print "There are %d cells" % n_cells

	# indices in counter-clockwise order
	cell_indices = np.zeros((n_cells, 6))

	# each vertex has 3 polygons attached
	n_vertices = (6 * n_cells) / 3
	# list of x,y vertices, no order
	vertices = np.zeros((n_vertices, 2))

	# # get left pointed corner for all cells
	# # this will correspond to index 0 for every cell
	# height = 0
	# x = 0.75w, 2.25w
	# height = 0.5h
	# x = 0w, 1.5w,
	# height = 1h
	# x = 0.75w, 2.25w
	# height = 1.5
	# x = 


	# curr_h = 0
	# for i in range(0,nx):
	# 	# curr_x = 
	# 	for j in range(0,ny):
	# 		# curr_y = 
	# 		print i, j, curr_h, curr_w

	# trace counter-clockwise
	# diagonal down right
	# right 0.5 w
	# diagonal up right
	# diagonal up left
	# left 0.5 w
	# diagonal down left
	# if the next vertex == lx or ly -> should actually be 0 (periodic bounds)




	return 



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
	ny = 2

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


	# plot grid
	plot_grid(xx, yy, L)


	trace_hex_vertices(nx, ny, xx, yy, w, h)

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
