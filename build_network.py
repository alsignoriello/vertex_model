#!/usr/bin/python
import numpy as np
import sys
from Network import Network

"""

build_network.py - initializes the vertex model

Builds Class Network to describe current configuration


author: Lexi Signoriello
date: 	1/20/16


"""


''' set initial parameters ''' 
# store parameters in dictionary
parameters = {}

# Side length of box in x direction
lx = 9 * (2 / (3 * (3**0.5)))**0.5
parameters['lx'] = lx

# Side length of box in y directions
ly = 4 * (2 / (3**0.5))**0.5
parameters['ly'] = ly

L = np.array([lx,ly])

# # K - elastic coefficient
k = 1.
parameters['k'] = k

# # A0 - prefferred area for cell
A0 = 1.
parameters['A0'] = A0

# gamma - contraction coefficient 
gamma = 1. 
parameters['gamma'] = gamma

# lambda - line tension between cells
# linear coefficient
Lambda = 1.
parameters['lambda'] = Lambda

# delta_t - time step 
delta_t = 0.05
parameters['delta_t'] = delta_t


# read in list of all vertices in network
vertex_file = "vertices.txt"
vertices = np.loadtxt(vertex_file)


print parameters

# network = Network(L, )







