#!/usr/bin/python
import numpy as np 
from Cell import Cell
from geometry import periodic_diff
import matplotlib.pyplot as plt



# T1 transiton
def T1(cells, edges, L, i1, i2):


	# # find  cells involved with 2 vertices
	cell_ids = np.zeros(4)
	cell_ids.fill(-1)
	for cell in cells:

		# Cell 1 or Cell 3
		if i1 in cell.indices and i2 in cell.indices:

			pos1 = np.where(cell.indices == i1)
			pos2 = np.where(cell.indices == i2)

			if pos1 == len(cell.indices) - 1:
				pos1 = -1

			if pos2 == len(cell.indices) - 1:
				pos2 = -1

			# if Cell 1:
			if pos1 < pos2:
				cell_ids[0] = cell.id


			# if Cell 3:
			if pos2 < pos1:
				cell_ids[2] = cell.id

		
		# Cell 4
		if i1 in cell.indices and i2 not in cell.indices:
			cell_ids[3] = cell.id

		# Cell 2
		if i2 in cell.indices and i1 not in cell.indices:
			cell_ids[1] = cell.id

	# print cell_ids
	# Cell 1
	# Delete v2
	cell_1 = cells[int(cell_ids[0])]
	pos = np.where(cell_1.indices == i2)[0]
	tmp_indices = np.delete(cell_1.indices, pos)
	cell_1.set_indices(tmp_indices)

	# Cell 2
	# add v1 before v2
	cell_2 = cells[int(cell_ids[1])]
	pos = np.where(cell_2.indices == i2)[0]

	# shift to correct positon
	left = cell_2.indices[:pos]
	right = cell_2.indices[pos:]
	tmp_indices = np.concatenate((left, [i1], right))
	cell_2.set_indices(tmp_indices)

	# index of changing edge
	e2 = pos - 1.
	if e2 == -1.:
		e2 = len(cell_2.indices) - 1
	e2 = cell_2.indices[int(e2)]

	# Cell 3
	# delete v1
	cell_3 = cells[int(cell_ids[2])]
	pos = np.where(cell_3.indices == i1)[0]
	tmp_indices = np.delete(cell_3.indices, pos)
	cell_3.set_indices(tmp_indices)

	# Cell 4
	# insert V2 before V1
	cell_4 = cells[int(cell_ids[3])]
	pos = np.where(cell_4.indices == i1)[0]

	# shift to correct position
	left = cell_4.indices[:pos]
	right = cell_4.indices[pos:]
	tmp_indices = np.concatenate((left, [i2], right))
	cell_4.set_indices(tmp_indices)

	e4 = pos - 1. 
	if e4 == -1.:
		e4 = len(cell_4.indices) - 1
	e4 = cell_4.indices[int(e4)]
	cells[int(cell_ids[3])] = cell_4

	# Adapt edges to new configuration
	# V1 edges: add e2, subtract e4
	for i,edge in enumerate(edges[i1]):
		if edge == e4:
			edges[i1][i] = e2
	# V2 edges: add e4, subtract e2
	for i,edge in enumerate(edges[i2]):
		if edge == e2:
			edges[i2][i] = e4
	# e2 edges: add V1, subtract V2
	for i,edge in enumerate(edges[e2]):
		if edge == i2:
			edges[e2][i] = i1
	# e4 edges: add V2, subtract V1
	for i,edge in enumerate(edges[e4]):
		if edge == i1:
			edges[e4][i] = i2


	return cells, edges










































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



