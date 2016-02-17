#!/usr/bin/python
import numpy as np 
from Cell import Cell
from geometry import periodic_diff
from energy import *
import copy
from plot import *


""" 

transition.py - implements T1 transition for short bond lengths

author: Lexi Signoriello
date: 2/12/16

4 cells involved in transition are 1-4 counter-clockwise order

Cells defined such that:
Cell 0: i4, i1, i2, i5
Cell 1: i3, i1, i4
Cell 2: i6, i2, i1, i3
Cell 3: i5, i2, i6


Edges defined such that:
Edge 0: i1 - i2
Edge 1: i1 - i3
Edge 2: i1 - i4
Edge 3: i2 - i1
Edge 4: i2 - i5
Edge 5: i2 - i6
Edge 6: i3 - i1 # reverse edges
Edge 7: i4 - i1
Edge 8: i5 - i2 
Edge 9: i6 - i2



"""



def get_6_indices(cells, i1, i2, cell_ids):
	cells_copy = []
	for i in cell_ids:
		cell = copy.deepcopy(cells[i])
		cells_copy.append(cell)

	# define cells
	cell_0 = cells_copy[0]
	cell_1 = cells_copy[1]
	cell_2 = cells_copy[2]
	cell_3 = cells_copy[3]

	# Find indices wrt Cell 1
	pos = int(np.where(cell_1.indices == i1)[0])
	# i3: cell 1 before i1
	if pos == 0:
		i_left = len(cell_1.indices) - 1
	else:
		i_left = pos - 1
	i3 = cell_1.indices[i_left]
	# i4: cell 1 after i1
	if pos == len(cell_1.indices) - 1:
		i_right = 0
	else:
		i_right = pos + 1
	i4 = cell_1.indices[i_right]
	# i5: cell 3 before i2
	pos = int(np.where(cell_3.indices == i2)[0])
	if pos == 0:
		i_left = len(cell_3.indices) - 1
	else: 
		i_left = pos - 1
	i5 = cell_3.indices[i_left]
	# i6: cell 3 after i2
	if pos == len(cell_3.indices) - 1:
		i_right = 0
	else:
		i_right = pos + 1
	i6 = cell_3.indices[i_right]

	indices = [i1,i2,i3,i4,i5,i6]

	return indices



# get cells and edges associated with short bond length
def T1_0(cells, i1, i2, cell_ids, indices):
	cells_0 = []

	for i in cell_ids:
		# copy cell so it can be manipulated without changing
		# current configuation
		cell = copy.deepcopy(cells[i])
		cells_0.append(cell)

	# define cells
	cell_0 = cells_0[0]
	cell_1 = cells_0[1]
	cell_2 = cells_0[2]
	cell_3 = cells_0[3]

	i1 = indices[0]
	i2 = indices[1]
	i3 = indices[2]
	i4 = indices[3]
	i5 = indices[4]
	i6 = indices[5]

	edges_0 = np.zeros((10,2))
	# Edge 0: i1 - i2
	edges_0[0,0] = i1
	edges_0[0,1] = i2

	# Edge 1: i1 - i3
	edges_0[1,0] = i1
	edges_0[1,1] = i3

	# Edge 2: i1 - i4
	edges_0[2,0] = i1
	edges_0[2,1] = i4

	# Edge 3: i2 - i1
	edges_0[3,0] = i2
	edges_0[3,1] = i1

	# Edge 4: i2 - i5
	edges_0[4,0] = i2
	edges_0[4,1] = i5

	# Edge 5: i2 - i6
	edges_0[5,0] = i2
	edges_0[5,1] = i6

	# Edge 6: i3 - i1 # reverse edges
	edges_0[6,0] = i3
	edges_0[6,1] = i1

	# Edge 7: i4 - i1
	edges_0[7,0] = i4
	edges_0[7,1] = i1

	# Edge 8: i5 - i2 
	edges_0[8,0] = i5
	edges_0[8,1] = i2

	# Edge 9: i6 - i2
	edges_0[9,0] = i6
	edges_0[9,1] = i2

	return cells_0, edges_0

# get cells and edges associated with 
def T1_left(cells, i1, i2, cell_ids, indices):

	# Cells
	cells_l = []
	# ids in correct order already
	for i in cell_ids:
		cell = copy.deepcopy(cells[i])
		cells_l.append(cell)

	# define cells
	cell_0 = cells_l[0]
	cell_1 = cells_l[1]
	cell_2 = cells_l[2]
	cell_3 = cells_l[3]

	# define indices
	i1 = indices[0]
	i2 = indices[1]
	i3 = indices[2]
	i4 = indices[3]
	i5 = indices[4]
	i6 = indices[5]

	# Cell 0: remove i2
	pos = int(np.where(cell_0.indices == i2)[0])
	indices = np.delete(cell_0.indices, pos)
	cells_l[0].indices = indices


	# Cell 1: insert i2 before i1 
	pos = int(np.where(cell_1.indices == i1)[0])
	left_indices = cell_1.indices[:pos]
	right_indices = cell_1.indices[pos:]
	indices = np.concatenate((left_indices, [i2], right_indices))
	cells_l[1].indices = indices

	# Cell 2: remove i1
	pos = int(np.where(cell_2.indices == i1)[0])
	indices = np.delete(cell_2.indices, pos)
	cells_l[2].indices = indices

	# Cell 3: insert i1 before i2
	pos = int(np.where(cell_3.indices == i2)[0])
	left_indices = cell_3.indices[:pos]
	right_indices = cell_3.indices[pos:]
	indices = np.concatenate((left_indices, [i1], right_indices))
	cells_l[3].indices = indices


	# Edges
	edges_l = np.zeros((10,2))
	# Edge 0: i1 - i2
	edges_l[0,0] = i1
	edges_l[0,1] = i2

	# Edge 1: i2 - i3
	edges_l[1,0] = i2
	edges_l[1,1] = i3

	# Edge 2: i1 - i4
	edges_l[2,0] = i1
	edges_l[2,1] = i4

	# Edge 3: i2 - i1
	edges_l[3,0] = i2
	edges_l[3,1] = i1

	# Edge 4: i1 - i5
	edges_l[4,0] = i1
	edges_l[4,1] = i5

	# Edge 5: i2 - i6
	edges_l[5,0] = i2
	edges_l[5,1] = i6

	# Edge 6: i3 - i2 # reverse edges
	edges_l[6,0] = i3
	edges_l[6,1] = i2

	# Edge 7: i4 - i1
	edges_l[7,0] = i4
	edges_l[7,1] = i1

	# Edge 8: i5 - i1 
	edges_l[8,0] = i5
	edges_l[8,1] = i1

	# Edge 9: i6 - i2
	edges_l[9,0] = i6
	edges_l[9,1] = i2


	return cells_l, edges_l

def T1_right(cells, i1, i2, cell_ids, indices):

	cells_r = []
	for i in cell_ids:
		cell = copy.deepcopy(cells[i])
		cells_r.append(cell)

	# define cells
	cell_0 = cells_r[0]
	cell_1 = cells_r[1]
	cell_2 = cells_r[2]
	cell_3 = cells_r[3]

	# define indices
	i1 = indices[0]
	i2 = indices[1]
	i3 = indices[2]
	i4 = indices[3]
	i5 = indices[4]
	i6 = indices[5]

	# Cell 0: remove i1
	pos = int(np.where(cell_0.indices == i1)[0])
	indices = np.delete(cell_0.indices, pos)
	cells_r[0].indices = indices


	# Cell 1: insert i2 after i1
	pos = int(np.where(cell_1.indices == i1)[0])
	left_indices = cell_1.indices[:pos+1]
	right_indices = cell_1.indices[pos+1:]
	indices = np.concatenate((left_indices, [i2], right_indices))
	cells_r[1].indices = indices

	# Cell 2: remove i2
	pos = int(np.where(cell_2.indices == i2)[0])
	indices = np.delete(cell_2.indices, pos)
	cells_r[2].indices = indices

	# Cell 3: insert i1 after i2
	pos = int(np.where(cell_3.indices == i2)[0])
	left_indices = cell_3.indices[:pos+1]
	right_indices = cell_3.indices[pos+1:]
	indices = np.concatenate((left_indices, [i1], right_indices))
	cells_r[3].indices = indices 

	# # Edges
	edges_r = np.zeros((10,2))
	# Edge 0: i1 - i2
	edges_r[0,0] = i1
	edges_r[0,1] = i2

	# Edge 1: i1 - i3
	edges_r[1,0] = i1
	edges_r[1,1] = i3

	# Edge 2: i1 - i6
	edges_r[2,0] = i1
	edges_r[2,1] = i6

	# Edge 3: i2 - i1
	edges_r[3,0] = i2
	edges_r[3,1] = i1

	# Edge 4: i2 - i5
	edges_r[4,0] = i2
	edges_r[4,1] = i5

	# Edge 5: i2 - i4
	edges_r[5,0] = i2
	edges_r[5,1] = i4

	# Edge 6: i3 - i1 # reverse edges
	edges_r[6,0] = i3
	edges_r[6,1] = i1

	# Edge 7: i4 - i2
	edges_r[7,0] = i4
	edges_r[7,1] = i2

	# Edge 8: i5 - i2 
	edges_r[8,0] = i5
	edges_r[8,1] = i2

	# Edge 9: i6 - i1
	edges_r[9,0] = i6
	edges_r[9,1] = i1


	return cells_r, edges_r


# # find 4 cells involved with 2 vertices
# Labeled cells 0-3 in counter-clockwise order
# Cell 0 and Cell 3 are neighbors
def get_4_cells(cells, i1, i2):

	cell_ids = np.zeros(4).astype(int)
	cell_ids.fill(-1) # catch errors later

	for cell in cells:
		# Cell 0 or Cell 2
		# Current neighboring cells
		# Cell 1 should have i1 before i2 in counter-clockwise orde
		if i1 in cell.indices and i2 in cell.indices:
			pos1 = np.where(cell.indices == i1)
			pos2 = np.where(cell.indices == i2)

			if pos1 == len(cell.indices) - 1:
				pos1 = -1
			if pos2 == len(cell.indices) - 1:
				pos2 = -1

			# if Cell 1: i1 is before i2
			if pos1 < pos2:
				cell_ids[0] = cell.id
			# if Cell 3: i2 is before i1
			if pos2 < pos1:
				cell_ids[2] = cell.id
		
		# Cell 3
		if i2 in cell.indices and i1 not in cell.indices:
			cell_ids[3] = cell.id
		# Cell 1
		if i1 in cell.indices and i2 not in cell.indices:
			cell_ids[1] = cell.id

	return cell_ids
	


def T1_transition(network, vertices, cells, edges, min_dist):
	L = network.L

	for edge in edges:
		i1 = edge[0]
		i2 = edge[1]

		v1 = vertices[i1]
		vertex2 = vertices[i2]
		v2 = v1 + periodic_diff(vertex2, v1, L)

		dist = euclidean_distance(v1[0], v1[1], v2[0], v2[1])

		if dist < min_dist:
			print "T1"
			cell_ids = get_4_cells(cells, i1, i2)
			if -1 in cell_ids:
				# print cell_ids
				pass
			else:
				# find minimum configuration

				# 6 indices for vertices involved in transition
				indices = get_6_indices(cells, i1, i2, cell_ids)

				# original configuration
				cells_0, edges_0 = T1_0(cells, i1, i2, cell_ids, indices)
				E0 = network.get_energy(vertices, cells_0, edges_0)
				print E0
				# plot_4_cells(vertices, cells_0, i1, i2, L, "0.jpg", E0)

				# left T1 transition 
				cells_l, edges_l = T1_left(cells, i1, i2, cell_ids, indices)
				E_left = network.get_energy(vertices, cells_l, edges_l)
				print E_left
				# plot_4_cells(vertices, cells_l, i1, i2, L, "l.jpg", E_left)

				# # right T1 transition
				cells_r, edges_r = T1_right(cells, i1, i2, cell_ids, indices)
				E_right = network.get_energy(vertices, cells_r, edges_r)
				print E_right 
				# plot_4_cells(vertices, cells_r, i1, i2, L, "r.jpg", E_right)

				# get minimum
				min_energy = np.min((E0, E_left, E_right))
				min_i = np.argmin((E0, E_left, E_right))

				# do nothing - same configuration
				if min_i == 0:
					pass

				# if min_i == 1:
				# set_T1_left(cells, cells_l, cell_ids, edges, indices)
				# np.savetxt("edges2.txt", edges, fmt="%d")

				# if min_i == 2:
				set_T1_right(cells, cells_r, cell_ids, edges, indices)
				exit()

	return cells, edges


def set_T1_left(cells, cells_l, cell_ids, edges, indices):
	# set new cell indices
	for i,cell in enumerate(cells_l):
		cells[cell_ids[i]].indices = cell.indices

	# set new edges
	i1 = indices[0]
	i2 = indices[1]
	i3 = indices[2]
	i5 = indices[4]
	for i,edge in enumerate(edges):

		# i1 - i3 becomes i2 - i3
		if edge[0] == i1 and edge[1] == i3:
			edges[i][0] = i2
	
		# i2 - i5 becomes i1 - i5
		if edge[0] == i2 and edge[1] == i5:
			edges[i][0] = i1

		# i3 - i1 becomes i3 - i2
		if edge[0] == i3 and edge[1] == i1:
			edges[i][1] = i2

		# i5 - i2 becomes i5 - i1
		if edge[0] == i5 and edge[1] == i2:
			edges[i][1] = i1
	
	return 


def set_T1_right(cells, cells_r, cell_ids, edges, indices):

	# set new cell indices
	for i,cell in enumerate(cells_r):
		cells[cell_ids[i]].indices = cell.indices
	

	# set new edges
	i1 = indices[0]
	i2 = indices[1]
	i4 = indices[3]
	i6 = indices[5]

	for i,edge in enumerate(edges):

		# i1 - i4 becomes i2 - i4
		if edge[0] == i1 and edge[1] == i4:
			edges[i][0] = i2

		# i2 - i6 becomes i1 - i6
		if edge[0] == i2 and edge[1] == i6:
			edges[i][0] = i1

		# i4 - i1 becomes i4 - i2
		if edge[0] == i4 and edge[1] == i1:
			edges[i][1] = i2

		# i6 - i2 becomes i6 - i1
		if edge[0] == i6 and edge[1] == i2:
			edges[i][1] = i1

	return 
























