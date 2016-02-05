#!/usr/bin/python
import numpy as np
from geometry import periodic_diff, unit_vector


"""

force.py - computes forces in the current configuration
of the vertex model


author: Lexi Signoriello
date: 1/20/16

"""


def get_clockwise(index, indices, vertices, L):
	
	# get position of vertex in list
	pos = [i for i,x in enumerate(indices) if x == index]
	pos = pos[0]

	# clockwise is position to right
	# wrap around to 0 if at end of the list
	if pos == len(indices) - 1:
		pos = 0
	else:
		pos += 1

	# compute vertex wrt periodic boundaries
	v0 = vertices[index]
	v = vertices[indices[pos]]
	vc = v0 + periodic_diff(v, v0, L)

	return vc 



def get_counter_clockwise(index, indices, vertices, L):
		
	# get position of vertex in list
	pos = [i for i,x in enumerate(indices) if x == index]
	pos = pos[0]
	
	# clockwise is position to left
	# wrap around to end of list if first value
	if pos == 0:
		pos = len(indices) - 1
	else:
		pos -= 1

	v0 = vertices[index]
	v = vertices[indices[pos]]
	vcc = v0 + periodic_diff(v, v0, L)

	return vcc


# Force on vertex due to elasticity
def F_elasticity(vertices, cells, ka,  L):
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

				# get clockwise vector
				vc = get_clockwise(i, cell.indices, vertices, L)

				# get counter-clockwise vector
				vcc = get_counter_clockwise(i, cell.indices, vertices, L)

				# get the difference vector
				diff = vc - vcc

				# compute perpendicular vector
				# assure correct direction (pointing towards vertex)
				perp_matrix = np.zeros((2,2))
				perp_matrix[0,1] = 1.
				perp_matrix[1,0] = -1.

				f = -0.5 * np.dot(perp_matrix, diff)

				# force contributed from this cell stored in f
				coeff = ka * (cell.A0 - cell.get_area(vertices, L))

				forces[i,:] += coeff * f


	return -forces



def F_actin_myosin(vertices, cells, gamma, L):

	# every vertex has an associated force
	n_vertices = len(vertices)
	forces = np.zeros((n_vertices, 2))

	for i,vertex in enumerate(vertices):

		# find cells with this vertex
		for cell in cells:

			if i in cell.indices:

				# get clockwise vector
				vc = get_clockwise(i, cell.indices, vertices, L)
				uvc = unit_vector(vertex, vc)
	
				# get counter-clockwise vector
				vcc = get_counter_clockwise(i, cell.indices, vertices, L)
				uvcc = unit_vector(vcc, vertex)


				# get perimeter for this cell
				p = cell.get_perim(vertices, L)

				forces[i,:] -= (gamma * p) * (uvc - uvcc)

	return forces

def F_adhesion(vertices, edges, tau, L):

	# every vertex has an associated force
	n_vertices = len(vertices)
	forces = np.zeros((n_vertices, 2))

	for i,vertex in enumerate(vertices):
		edge_list = edges[i]
		for edge in edge_list:
			v2 = vertices[edge]
			vertex2 = vertex + periodic_diff(v2, vertex, L)
			uv = unit_vector(vertex, vertex2)
			forces[i,:] -= tau * uv
	return forces



