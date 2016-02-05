#!/usr/bin/python
import numpy as np 
from Cell import Cell
from geometry import periodic_diff
import matplotlib.pyplot as plt



# T1 transiton
def T1(vertices, cells, edges, L, i1, i2):

	# vertices too close together
	v1 = vertices[i1]
	vertex2 = vertices[i2]
	v2 = v1 + periodic_diff(vertex2, v1, L)

	# move vertices to perpendicular bisector
	# get midpoint
	midpoint = (v1 + v2) / 2. #v1 + (v2 - v1) / 2.

	# perpendicular matrix
	perp = np.zeros((2,2))
	perp[0,1] = 1.
	perp[1,0] = -1.

	v1_new = midpoint + 0.5 * np.dot(perp, v1 - v2)
	v2_new = midpoint + 0.5 * np.dot(perp, v2 - v1)

	# check lines are perpendicular
	# # print v1, v1_new, v2, v2_new 
	# plt.scatter(v1[0],v1[1], color="r")
	# plt.scatter(v2[0],v2[1], color="r")
	# plt.scatter(v1_new[0], v1_new[1], color="c")
	# plt.scatter(v2_new[0], v2_new[1], color="c")
	# plt.plot([v1[0],v2[0]], [v1[1],v2[1]], color="r")
	# plt.plot([v1_new[0], v2_new[0]], [v1_new[1], v2_new[1]], color="c")
	# plt.show()
	# print np.dot(v1 - v2, v1_new - v2_new)

	# # rotate vertices
	vertices[i1] = v1_new
	vertices[i2] = v2_new


	# # find  cells involved with 2 vertices
	cell_ids = np.zeros(4)
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

	print cell_ids

	# Cell 1
	# Delete v2
	cell_1 = cells[int(cell_ids[0])]
	pos = np.where(cell_1.indices == i2)
	cell_1.indices = np.delete(cell_1.indices, pos)


	# Cell 2
	# add v1 before v2
	cell_2 = cells[int[cell_ids[1]]]
	pos = np.where(cell_4.indices == i2)
	# append i1

	# shift to correct positon


	# Cell 3
	# delete v1
	cell_3 = cells[int(cell_ids[2])]
	pos = np.where(cell_3.indices == i1)
	# print i1, i2, pos
	# print cell_3.indices
	cell_3.indices = np.delete(cell_3.indices, pos)
	# print cell_3.indices


	# Cell 4
	# insert V2 before V1
	cell_4 = cells[int(cell_ids[3])]
	pos = np.where(cell_4.indices == i1)
	# append i2

	# shift to correct position




	# Edges
	# Edge from V1 to V2 still exists

	# V1
	# delete edge from cell 4 to V1
	# replace with from V1 to cc index in Cell 1

	# V2
	# delete edge from Cell 1 from V2
	# replace with edge to V2 from cc index in Cell 3

	return vertices, cells, edges

