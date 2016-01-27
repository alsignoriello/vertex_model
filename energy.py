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
def E_elasticity(cells, A0, ka):
	e = 0.
	for cell in cells:
		e += ka * (cell.get_area() - A0)**2
	return e



# Energy due to line tension & maintaing surface area
def E_tension(cells, P0, kp):
	e = 0.
	for cell in cells:
		e += kp * (cell.get_perim() - P0)**2
	return e




# # adhesion - linear term, describes line tensions
# def E_adhesion(cells, gamma):
# 	e = 0
# 	for cell in cells:
# 		e += gamma * cell.perim
# 	return e


# def E_contraction(cells, k_p):
# 	e = 0
# 	for cell in cells:
# 		e += k_p * cell.perim**2
# 	return e



