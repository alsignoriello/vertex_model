#!/usr/bin/python
import numpy as np
from math import sqrt

""" 

geometry.py - geometrical formulas 

author: Lexi Signoriello
date: 1/20/16

vertices - list of vertices
* Make sure passing the list of cell vertices (NOT global list of vertices)
(x0, y0), (x1, y1) ... (xN, yN)

"""




''' Geometric Center of Polygon '''
def center(vertices):
	n = len(vertices)
	sumX = 0
	sumY = 0
	# sum the vectors
	for i in range(0,n):
		x,y = vertices[i,:]
		sumX += x
		sumY += y

	# divide by number of sides
	cx = sumX / (n)
	cy = sumY / (n)

	return cx,cy


# http://stackoverflow.com/questions/451426/how-do-i-calculate-the-surface-area-of-a-2d-polygon
def area(vertices):
	edges = zip(vertices, vertices[1:] + [vertices[0]])
	cross_product = 0
	for ((x0, y0), (x1, y1)) in edges:
		cross_product += ((x0 * y1) - (x1 * y0))
	return 0.5 * abs(cross_product)


# this may need to be adapted for periodic boundary conditions
def perimeter(vertices):
	n = len(vertices)
	perimeter = 0.
	for i in range(0,n):
		x0,y0 = vertices[i]
		if i == n - 1:
			x1,y1 = vertices[0]
		if i != n - 1:
			x1,y1 = vertices[i+1]
		dist = euclidean_distance(x0, y0, x1, y1)
		perimeter += dist
	return perimeter


# compute euclidean distance between (x,y) coordinates
def euclidean_distance(x0, y0, x1, y1):
	return sqrt((x0 - x1)**2 + (y0 - y1)**2)
	

# Difference with respect to periodic boundaries
def periodic_diff(v1,v2,L):
	return ((v1 - v2 + L/2) % L) - L/2


# get unit vector
def unit_vector(v1,v2):
	vector = v1 - v2
	dist = euclidean_distance(v1[0], v1[1], v2[0],v2[1])
	uv = vector / dist
	return uv
