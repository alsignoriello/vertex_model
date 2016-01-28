#!/usr/bin/python
import numpy as np
from Cell import Cell

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
		# print cell.indices
		a = cell.get_area(vertices, L)
		A0 = cell.A0
		e += ka * (a - A0)**2
	return e



# Energy due to line tension & maintaing surface area
def E_tension(vertices, cells, kp, L):
	e = 0.
	for cell in cells:
		p = cell.get_perim(vertices, L)
		P0 = cell.P0
		e += kp * (p - P0)**2
	return e

