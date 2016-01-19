#!usr/bin/bash

# # Run vertex model with N cells
# periodic boundary conditions
# author: Lexi Signoriello
# date: 1/19/16


# Number of cells
N=$1

# Side length of box in x direction
lx=$2

# Side length of box in y direction
ly=$3


# # Build Network

# python build_network.py
# vertices: contains x,y coordinates for all vertices in system
# edges: all edges in between vertices
# cell_vertices: contains list in counter-clockwise order of vertices surrounding cell
# cells: area, perimeter
# cells and cell_vertices map 1-1, id = line number (0 based)


# # Relax Energy in Network
# Network is "relaxed" when energy stays constant

# steepest descent


# conjugate gradient method



# # Plot Network
# python plot.py 









