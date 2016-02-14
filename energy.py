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


def E_elasticity(vertices, cells, ka, L):
	e = 0.
	for cell in cells:
		a = cell.get_area(vertices, L)
		A0 = cell.A0
		e += (ka / 2.) * (a - A0)**2
	return e



def E_adhesion(vertices, edges, tau , L):
	e = 0.
	for edge in edges:
		i1 = edge[0]
		i2 = edge[1]
		v1 = vertices[i1]
		vertex2 = vertices[i2]
		v2 = vertex2 + periodic_diff(vertex2, v1, L)
		dist = euclidean_distance(v1[0], v1[1], v2[0], v2[1])
		e += tau * dist
	return e


def E_actin_myosin(vertices, cells, gamma, L):
	e = 0.
	for cell in cells:
		p = cell.get_perim(vertices, L)
		e += ((gamma / 2.) * (p**2))
	return e


