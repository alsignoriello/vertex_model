#!/usr/bin/python
import numpy as np
import os
import glob
from geometry import periodic_diff, euclidean_distance
import sys


def get_msd(x0,y0,x1,y1,L):
	v1 = np.array([x0,y0])
	v2 = np.array([x1,y1])
	diff = periodic_diff(v1, v2, L)
	return (diff[0]**2 + diff[1]**2)


# Side length of box in x direction
lx = 9 * (2 / (3 * (3**0.5)))**0.5

# Side length of box in y directions
ly = 4 * (2 / (3**0.5))**0.5

L = np.array([lx,ly])

noise = float(sys.argv[1])
folder = sys.argv[2]

os.chdir("./noise/%s" % folder)


vertex_matrix = np.zeros((48,2,100))

msd_array = np.zeros(99)

for file in glob.glob("*.txt"):
	i = int(file[:-4])
	vertices = np.loadtxt(file)
	vertex_matrix[:,:,i] = vertices 

for i in range(0,99):

	# compute mean squared displacement	
	for j in range(0,48):
		x0 = vertex_matrix[j,0,0]
		y0 = vertex_matrix[j,1,0]
		x1 = vertex_matrix[j,0,i]
		y1 = vertex_matrix[j,1,i]
		msd = get_msd(x0, y0, x1, y1, L)

		msd_array[i] += msd


print "noise = %f" % noise
print np.sum(msd_array) / 100.



