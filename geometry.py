#!/usr/bin/python
import numpy as np
from math import sqrt, pi, sin, cos, acos, atan2, floor


""" 

geometry.py - geometry formulas 

author: Lexi Signoriello
date: 1/20/16

vertices - list of vertices  
(x0, y0), (x1, y1) ... (xN, yN)

"""


# Geometric center of a polygon
def center(vertices):
	n = len(vertices)
	sumX = 0
	sumY = 0
	# sum the vectors
	for i in range(0,n):
		x,y = vertices[i]
		sumX += x
		sumY += y

	# divide by number of sides
	cx = sumX / n
	cy = sumY / n

	return cx,cy


# Area of a polygon
def area(vertices):
	edges = zip(vertices, vertices[1:] + [vertices[0]])
	cross_product = 0
	for ((x0, y0), (x1, y1)) in edges:
		cross_product += ((x0 * y1) - (x1 * y0))
	return 0.5 * abs(cross_product)


# Perimeter of a polygon
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


# Euclidean distance between (x,y) coordinates
def euclidean_distance(x0, y0, x1, y1):
	return sqrt((x0 - x1)**2 + (y0 - y1)**2)
	

# Difference with respect to periodic boundaries
def periodic_diff(v1, v2, L):
	return ((v1 - v2 + L/2.) % L) - L/2.


# Unit vector
def unit_vector(v1, v2):
	vector = v1 - v2
	dist = euclidean_distance(v1[0], v1[1], v2[0],v2[1])
	uv = vector / dist
	return uv


# assumes 2D
def magnitude(v):
	return (v[0]**2 + v[1]**2)**(0.5)


# check if counter-clockwise
# change polygon data structure?
def check_counter_clockwise(polygon):
	sumEdges = 0
	for i,(x,y) in enumerate(polygon):
		if i == 0:
			x0 = x
			y0 = y
		if i + 1 != len(polygon):
			x2,y2 = polygon[i+1]
		if i+1 == len(polygon):
			x2 = x0
			y2 = y0	

		sumEdges += float(x2 - x) / float(y2 + y)

	if sumEdges > 0:
		return True
	else:
		return False





