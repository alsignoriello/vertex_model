import matplotlib.pyplot as plt
import numpy as np 
from transition import T1
from Cell import Cell

def build_cells(cell_indices, A0, P0):
	cells = []
	for i,indices in enumerate(cell_indices):
		cell = Cell(i, indices, A0, P0)
		cells.append(cell)
	return cells

vertices = np.loadtxt("vertices.txt")
edges = np.loadtxt("edges.txt").astype(int)

for x,y in vertices:
	plt.scatter(x,y)

for i,edge in enumerate(edges):
	for e in edge:
		if e != 16:
			x1 = vertices[i][0]
			y1 = vertices[i][1]
			x2 = vertices[e][0]
			y2 = vertices[e][1]
			plt.plot([x1,x2],[y1,y2],color="k")


plt.savefig("original.jpg")
plt.cla()

i1 = 6
i2 = 7
L = 5

cell_indices = np.loadtxt("cell_indices.txt").astype(int)
cells = build_cells(cell_indices, 1, 1)

cells, edges = T1(cells, edges, L, i1, i2) 

# for x,y in vertices:
# 	plt.scatter(x,y)

for i,edge in enumerate(edges):
	for e in edge:
		if e != 16:
			x1 = vertices[i][0]
			y1 = vertices[i][1]
			x2 = vertices[e][0]
			y2 = vertices[e][1]
			plt.plot([x1,x2],[y1,y2],color="k")

plt.savefig("T1.jpg")
plt.cla()
np.savetxt("edges2.txt", edges, fmt="%d")

f = open("cell_indices2.txt","w+")
for cell in cells:
	for i in cell.indices:
		f.write("%d\t" % i)
	f.write("\n")
f.close()

# for cell in cells:
# 	for i1, i2 in zip(cell.indices, np.concatenate((cell.indices[1:],[cell.indices[0]]))):
# 		print i1, i2
# 		plt.plot([vertices[i1][0],vertices[i2][0]], [vertices[i1][1], vertices[i2][1]],color="k")
# 	plt.axis([0,10,0,10])
# 	plt.show()

