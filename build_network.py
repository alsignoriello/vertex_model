#!/usr/bin/python
import numpy as np
import sys
from Network import Network
from parser import *

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

# Side length of box in y directions
ly = 4 * (2 / (3**0.5))**0.5

L = np.array([lx,ly])

# # k_a - elastic area coefficient
k_a = 1.
parameters['k_a'] = k_a

# # A0 - prefferred area for cell
A0 = 1.
parameters['A0'] = A0

# k_p - elastic perimeter coefficient 
k_p = 1. 
parameters['k_p'] = k_p

# gamma - line tension between cells
# linear coefficient
gamma = 1.
parameters['gamma'] = gamma

# delta_t - time step 
delta_t = 0.05
parameters['delta_t'] = delta_t

# read in list of all vertices in network
network_vertex_file = "network_vertices.txt"
network_vertices = read_network_vertices(network_vertex_file)

# read in cells
cell_index_file = "cell_indices.txt"
cells = build_cells(network_vertex_file, cell_index_file)

print parameters

network = Network(L, network_vertices, cells, parameters)

print network.get_energy_elasticity()


# write network




