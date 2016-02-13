#!/usr/bin/python
import numpy as np 
from Cell import Cell
from geometry import periodic_diff
from energy import *


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


# get cells and edges associated with short bond length
def T1_0(cells, edges, i1, i2, cell_ids):
	cells_0 = []
	# ids in correct order already
	for i in cell_ids:
		cell = cells[i]
		cells_0.append(cell)

	# define cells
	cell_0 = cells_0[0]
	cell_1 = cells_0[1]
	cell_2 = cells_0[2]
	cell_3 = cells_0[3]

	# Find indices wrt Cell 1
	pos = np.where(cell_1.indices == i1)[0]

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
	pos = np.where(cell_3.indices == i2)[0]
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
def T1_left(cells, edges, i1, i2, cell_ids):

	# Cells
	cells_l = []
	# ids in correct order already
	for i in cell_ids:
		cell = cells[i]
		cells_l.append(cell)

	# define cells
	cell_0 = cells_l[0]
	cell_1 = cells_l[1]
	cell_2 = cells_l[2]
	cell_3 = cells_l[3]


	# Find indices wrt Cell 1
	pos = np.where(cell_1.indices == i1)[0]

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
	pos = np.where(cell_3.indices == i2)[0]
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

	# Cell 0: remove i2
	pos = np.where(cell_0.indices == i2)[0]
	indices = np.delete(cell_0.indices, pos)
	cells_l[0].indices = indices


	# Cell 1: insert i2 before i1 
	pos = np.where(cell_1.indices == i1)[0]
	left_indices = cell_1.indices[:pos]
	right_indices = cell_1.indices[pos:]
	indices = np.concatenate((left_indices, [i2], right_indices))
	cells_l[1].indices = indices

	# Cell 2: remove i1
	pos = np.where(cell_2.indices == i1)[0]
	indices = np.delete(cell_2.indices, pos)
	cells_l[2].indices = indices

	# Cell 3: insert i1 after i2
	pos = np.where(cell_3.indices == i2)[0]
	left_indices = cell_3.indices[:pos+1]
	right_indices = cell_3.indices[pos+1:]
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

def T1_right(cells, edges, i1, i2, cell_ids):

	cells_r = []
	for i in cell_ids:
		cell = cells[i]
		print cell.indices
		# this is the problem.... cells should be constant
		# but the edits from cells_l (cell from left transition)
		# are in cells 
		cells_r.append(cell)

	# define cells
	cell_0 = cells_r[0]
	cell_1 = cells_r[1]
	cell_2 = cells_r[2]
	cell_3 = cells_r[3]

	# # Find indices wrt Cell 1
	# pos = np.where(cell_1.indices == i1)[0]

	# # i3: cell 1 before i1
	# if pos == 0:
	# 	i_left = len(cell_1.indices) - 1
	# else:
	# 	i_left = pos - 1
	# i3 = cell_1.indices[i_left]

	# # i4: cell 1 after i1
	# if pos == len(cell_1.indices) - 1:
	# 	i_right = 0
	# else:
	# 	i_right = pos + 1
	# i4 = cell_1.indices[i_right]

	# # i5: cell 3 before i2
	# cell_3 = cells_0[3]
	# pos = np.where(cell_3.indices == i2)[0]
	# if pos == 0:
	# 	i_left = len(cell_3.indices) - 1
	# else: 
	# 	i_left = pos - 1
	# i5 = cell_3.indices[i_left]

	# # i6: cell 3 after i2
	# if pos == len(cell_3.indices) - 1:
	# 	i_right = 0
	# else:
	# 	i_right = pos + 1
	# i6 = cell_3.indices[i_right]

	# # Cell 0: remove i1
	# pos = np.where(cell_0.indices == i1)[0]
	# indices = np.delete(cell_0.indices, pos)
	# cells_r[0].indices = indices


	# # # Cell 1: insert i2 after i1
	# print cell_1.indices
	# pos = np.where(cell_1.indices == i1)[0]
	# print pos, i1, i2
	# left_indices = cell_1.indices[:pos+1]
	# right_indices = cell_1.indices[pos+1:]
	# print left_indices, right_indices
	# indices = np.concatenate((left_indices, [i2], right_indices))
	# cells_r[1].indices = indices
	# print indices

	# # Cell 2: remove i2
	# pos = np.where(cell_2.indices == i2)[0]
	# indices = np.delete(cell_2.indices, pos)
	# cells_r[0].indices = indices

	# Cell 3: insert i1 after i2
	# print cell_3.indices
	# pos = np.where(cell_3.indices == i2)[0]
	# left_indices = cell_3.indices[:pos+1]
	# right_indices = cell_3.indices[pos+1:]
	# indices = np.concatenate((left_indices, [i1], right_indices))
	# cells_r[3].indices = indices 

	# # Edges
	edges_r = np.zeros((10,2))
	# # Edge 0: i1 - i2
	# edges_r[0,0] = i1
	# edges_r[0,1] = i2

	# # Edge 1: i1 - i3
	# edges_r[1,0] = i1
	# edges_r[1,1] = i3

	# # Edge 2: i2 - i4
	# edges_r[2,0] = i2
	# edges_r[2,1] = i4

	# # Edge 3: i2 - i1
	# edges_r[3,0] = i2
	# edges_r[3,1] = i1

	# # Edge 4: i2 - i5
	# edges_r[4,0] = i2
	# edges_r[4,1] = i5

	# # Edge 5: i2 - i4
	# edges_r[5,0] = i2
	# edges_r[5,1] = i4

	# # Edge 6: i3 - i1 # reverse edges
	# edges_r[6,0] = i3
	# edges_r[6,1] = i1

	# # Edge 7: i4 - i2
	# edges_r[7,0] = i4
	# edges_r[7,1] = i2

	# # Edge 8: i5 - i2 
	# edges_r[8,0] = i5
	# edges_r[8,1] = i2

	# # Edge 9: i6 - i1
	# edges_r[9,0] = i6
	# edges_r[9,1] = i1


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
			# print pos1, pos2

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
	



def set_T1_left():
	pass

def set_T1_right():
	pass


















































	# edges_r = np.zeros((6,2))
	# for edge in edges:
	# 	e1 = edge[0]
	# 	e2 = edge[1]

	# 	if e1 == i1:
	# 		# edge 1: i1 - i2
	# 		if e2 == i2:
	# 			edges_0[0,0] = e1
	# 			edges_0[0,1] = e2

	# 		cell_2 = cells[cell_ids[1]]
	# 		pos = np.where(cell_2.indices == i1)[0]
	# 		if pos == 0:
	# 			i_left = len(cell_2.indices) - 1
	# 		else:
	# 			i_left = pos - 1

	# 		if pos == len(cell_2.indices) - 1:
	# 			i_right = 0
	# 		else:
	# 			i_right = pos + 1


	# 		# edge 2: i1 - Cell 2 before i1
	# 		if e2 == cell_2.indices[i_left]:
	# 			edges_0[1,0] = e1
	# 			edges_0[1,1] = e2

	# 		# edge 3: i1 - Cell 2 after i1
	# 		if e2 == cell_2.indices[i_right]:
	# 			edges_0[2,0] = e1
	# 			edges_0[2,1] = e2

		
	# 	if e1 == i2:
	# 		# edge 4: i2 - i1
	# 		if e2 == i2:
	# 			edges_0[3,0] = e2
	# 			edges_0[3,1] = e1

	# 		cell_4 = cells[cell_ids[3]]
	# 		pos = np.where(cell_4.indices == i2)[0]
	# 		if pos == 0:
	# 			i_left = len(cell_4.indices) - 1
	# 		else:
	# 			i_left = pos - 1

	# 		if pos == len(cell_4.indices) - 1:
	# 			i_right = 0
	# 		else:
	# 			i_right = pos + 1

	# 		# edge 5: i2 - Cell 4 before i2
	# 		if e2 == cell_4.indices[i_left]:
	# 			edges_0[4,0] = e2
	# 			edges_0[4,1] = cell_4.indices[i_left]


	# 		# edge 6: i2 - Cell 4 after i
	# 		if e2 == cell_4.indices[i_right]:	
	# 			edges_0[5,0] = e2
	# 			edges_0[5,1] = cell_4.indices[i_right]




# # T1 transiton
# def T1(cells, edges, L, i1, i2):


# 	# Labeled cells 1-4 in counter-clockwise order
# 	# Cell 1 and Cell 4 are neighbors
# 	cell_ids = np.zeros(4).astype(int)
# 	cell_ids.fill(-1) # catch errors later
# 	for cell in cells:

# 		# Cell 1 or Cell 3
# 		# Current neighboring cells
# 		# Cell 1 should have i1 before i2 in counter-clockwise order
# 		if i1 in cell.indices and i2 in cell.indices:

# 			pos1 = np.where(cell.indices == i1)
# 			pos2 = np.where(cell.indices == i2)

# 			if pos1 == len(cell.indices) - 1:
# 				pos1 = -1

# 			if pos2 == len(cell.indices) - 1:
# 				pos2 = -1

# 			# if Cell 1: i1 is before i2
# 			if pos1 < pos2:
# 				cell_ids[0] = cell.id


# 			# if Cell 3: i2 is before i1
# 			if pos2 < pos1:
# 				cell_ids[2] = cell.id


		
# 		# Cell 4
# 		if i2 in cell.indices and i1 not in cell.indices:
# 			cell_ids[3] = cell.id

# 		# Cell 2
# 		if i1 in cell.indices and i2 not in cell.indices:
# 			cell_ids[1] = cell.id

# # 	# print cell_ids
# # 	if -1 in cell_ids:
# # 		return cells, edges


# 	# Calculate F0 = original energy
# 	cells_0 = []
# 	for i in cell_ids:
# 		cell = cells[i]
# 		cells_0.append(cell)



# 	# Calculate F- = energy left T1 transition
# 	cells_l = []
# 	for i in cell_ids:
# 		cell = cells[i]
# 		cells_l.append(cell)


# 	# Calculate F+ = energy right T1 transition
# 	cells_right = []
# 	for i in cell_ids:
# 		cell = cells[i]
# 		cells_right.append(cell)


# 	# Take minimum energy configuration



# 	# Replace old cells with new cells

# 	return cells, edges




































	# # LEFT HANDED TRANSITION
	# # Cell 1
	# # Delete v2
	# cell_1 = cells[int(cell_ids[0])]
	# pos = np.where(cell_1.indices == i2)[0]
	# tmp_indices = np.delete(cell_1.indices, pos)
	# cell_1.set_indices(tmp_indices)

	# # Cell 2
	# # add v1 before v2
	# cell_2 = cells[int(cell_ids[1])]
	# pos = np.where(cell_2.indices == i2)[0]

	# # shift to correct positon
	# left = cell_2.indices[:pos]
	# right = cell_2.indices[pos:]
	# tmp_indices = np.concatenate((left, [i1], right))
	# cell_2.set_indices(tmp_indices)

	# # index of changing edge
	# e2 = pos - 1.
	# if e2 == -1.:
	# 	e2 = len(cell_2.indices) - 1
	# e2 = cell_2.indices[int(e2)]

	# # Cell 3
	# # delete v1
	# cell_3 = cells[int(cell_ids[2])]
	# pos = np.where(cell_3.indices == i1)[0]
	# tmp_indices = np.delete(cell_3.indices, pos)
	# cell_3.set_indices(tmp_indices)

	# # Cell 4
	# # insert V2 before V1
	# cell_4 = cells[int(cell_ids[3])]
	# pos = np.where(cell_4.indices == i1)[0]

	# # shift to correct position
	# left = cell_4.indices[:pos]
	# right = cell_4.indices[pos:]
	# tmp_indices = np.concatenate((left, [i2], right))
	# cell_4.set_indices(tmp_indices)

	# e4 = pos - 1. 
	# if e4 == -1.:
	# 	e4 = len(cell_4.indices) - 1
	# e4 = cell_4.indices[int(e4)]
	# cells[int(cell_ids[3])] = cell_4

	# # Adapt edges to new configuration
	# # V1 edges: add e2, subtract e4
	# for i,edge in enumerate(edges[i1]):
	# 	if edge == e4:
	# 		edges[i1][i] = e2
	# # V2 edges: add e4, subtract e2
	# for i,edge in enumerate(edges[i2]):
	# 	if edge == e2:
	# 		edges[i2][i] = e4
	# # e2 edges: add V1, subtract V2
	# for i,edge in enumerate(edges[e2]):
	# 	if edge == i2:
	# 		edges[e2][i] = i1
	# # e4 edges: add V2, subtract V1
	# for i,edge in enumerate(edges[e4]):
	# 	if edge == i1:
	# 		edges[e4][i] = i2









# Not necessary to move vertices

	# # # check lines are perpendicular
	# # print v1, v1_new, v2, v2_new 
	# plt.scatter(v1[0],v1[1], color="r")
	# plt.scatter(v2[0],v2[1], color="r")
	# plt.scatter(v1_new[0], v1_new[1], color="c")
	# plt.scatter(v2_new[0], v2_new[1], color="c")
	# plt.plot([v1[0],v2[0]], [v1[1],v2[1]], color="r")
	# plt.plot([v1_new[0], v2_new[0]], [v1_new[1], v2_new[1]], color="c")
	# plt.show()
	# print np.dot(v1 - v2, v1_new - v2_new)

		# # vertices too close together
	# v1 = vertices[i1]
	# vertex2 = vertices[i2]
	# v2 = v1 + periodic_diff(vertex2, v1, L)

	# # move vertices to perpendicular bisector
	# # get midpoint
	# midpoint = (v1 + v2) / 2. 

	# # perpendicular matrix
	# perp = np.zeros((2,2))
	# perp[0,1] = 1.
	# perp[1,0] = -1.

	# # Find perpendicular vector
	# v1_new = midpoint + np.dot(perp, v1 - v2)
	# v2_new = midpoint + np.dot(perp, v2 - v1)

	# rotate vertices
	# vertices[i1] = v1_new
	# vertices[i2] = v2_new



