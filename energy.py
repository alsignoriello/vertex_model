#!/usr/bin/python
import numpy as np
from Cell import Cell
from geometry import periodic_diff, euclidean_distance

""" 

energy.py - contains components to compute the potential energy
in the current configuration of vertex model 


author: Lexi Signoriello
date: 1/20/16



"""


# Energy due to elasticity
def E_elasticity(vertices, cells, ka, L):
	e = 0.
	for cell in cells:
		a = cell.get_area(vertices, L)
		A0 = cell.A0
		e += (ka / 2.) * (a - A0)**2
	return e



def E_adhesion(vertices, edges, tau , L):
	e = 0.
	for i,neighbors in enumerate(edges):
		vertex = vertices[i]
		for j in neighbors:
			v2 = vertices[j]
			vertex2 = vertex + periodic_diff(v2, vertex, L)
			dist = euclidean_distance(vertex[0], vertex[1],
									vertex2[0], vertex2[1])
			e += tau * dist
	return e


def E_actin_myosin(vertices, cells, gamma, L):
	e = 0.
	for cell in cells:
		p = cell.get_perim(vertices, L)
		e += ((gamma / 2.) * (p**2))
	return e


# # combines linear + quadratic parameter for perimeter
# # Energy due to line tension & maintaing surface area
# def E_tension(vertices, cells, kp, L):
# 	e = 0.
# 	for cell in cells:
# 		p = cell.get_perim(vertices, L)
# 		P0 = cell.P0
# 		e += (kp / 2.) * (p - P0)**2
# 	return e
