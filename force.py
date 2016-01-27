#!/usr/bin/python
import numpy as np
import sys

"""

force.py - computes forces in the current configuration
of the vertex model


author: Lexi Signoriello
date: 1/20/16

"""


def get_clockwise(index, indices, vertices):
	
	# get position of vertex in list
	pos = [i for i,x in enumerate(indices) if x == index]
	pos = pos[0]

	# clockwise is position to right
	# wrap around to 0 if at end of the list
	if pos == len(indices) - 1:
		pos = 0

	if pos != len(indices) - 1:
		pos += 1

	return vertices[indices[pos]]



def get_counter_clockwise(index, indices, vertices):
		
	# get position of vertex in list
	pos = [i for i,x in enumerate(indices) if x == index]
	pos = pos[0]
	
	# clockwise is position to left
	# wrap around to end of list if first value
	if pos == 0:
		pos = len(indices) - 1

	if pos != 0:
		pos -= 1

	return vertices[indices[pos]]


# Force on vertex due to elasticity
def F_elasticity(cells, A0, ka, vertices):
	n_vertices = len(vertices)

	# evert vertex has an associated force
	forces = np.zeros((n_vertices, 2))

	# iterate over vertices and get force
	for i,vertex in enumerate(vertices):

		# find cells with this vertex
		for cell in cells:

			# if this vertex is in current cell
			# compute force contributed from this cell
			if i in cell.indices:
				# force contributed from this cell stored in f
				f = ka * (A0 - cell.area)

				# get clockwise vector
				vc = get_clockwise(i, cell.indices, vertices)

				# get counter-clockwise vector
				vcc = np.zeros(2)

				# get the difference vector
				diff = vc - vcc

				# compute perpendicular vector
				# assure correct direction (pointing towards vertex)
				perp_matrix = np.zeros((2,2))
				perp_matrix[0,1] = 1.
				perp_matrix[1,0] = -1.

				f *= np.dot(perp_matrix, diff)

				# move to midpoint of difference vector
				f *= 0.5

				forces[i,:] +=  f


	return 0.




# Force on vertex due to line tension
def F_tension(cells, P0, kp, vertices):
	return 0.
