#!usr/bin/bash

# # Run Vertex Model Simulation
# author: Lexi Signoriello
# date: 1/19/16

# # Number of cells
# N=$1

# # Side length of box in x direction
# lx=$2

# # Side length of box in y directions
# ly=$3

# # # Parameters
# # K_alpha - elastic coefficient
# K_alpha=$4

# # A0 - prefferred area for cell
# A0=$5

# # gamma - contraction coefficient 
# gamma=$6

# # lambda - line tension between cells
# lambda=$7

# # delta_t - change in time
# delta_t=$8

# # Build Network

# python build_network.py [vertex file] [cell file] [network connections]
# vertices: contains x,y coordinates for all vertices in system
# edges: all edges in between vertices
# cell_vertices: contains list in counter-clockwise order of vertices surrounding cell
# cells: area, perimeter
# cells and cell_vertices map 1-1, id = line number (0 based)


# read in vertices
# store in global vertex list
# read in cell indices
# build class cell 
# read in network connections
# make an edge list to store in 

# Calculate Energy 



# Calculate Forces




# Move Vertices


# # Relax Energy in Network
# Network is "relaxed" when energy stays constant

# steepest descent


# conjugate gradient method



# # Plot Network
# python plot.py 









