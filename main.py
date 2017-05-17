#!/usr/bin/env python3
import matplotlib.pyplot as plt
from rps import *

# Getting measurements
noise			= 0.1
gt_pos			= [[-2,-4],[-2,-3],[-2,-2],[-2,-1],[-2,0],[-2,1],[-2,2],[-2,3],[-2,4],[-1,0],[0,0],[1,0],[2,0]]
measured_dists	= gen_measurements(gt_pos,noise)

# Gradient descent parameters
gess_range		= 2			# Range for initial position guess (0 Gaussian stdev)
step_size		= 0.005		# Gradient descent step size
iterations		= 100		# Gradient descent number of iterations
verbose			= 1			# Verbose mode (printing distance matrices)

# Position estimation
est_pos = estimate_relative_pos(measured_dists,gess_range,step_size,iterations,verbose)

# Printing results
print_pos("Ground truth positions:",gt_pos)
print_pos("Final estimate positions:",est_pos)

# Scatter plot
gt_x = [row[0] for row in gt_pos]
gt_y = [row[1] for row in gt_pos]
est_x = [row[0] for row in est_pos]
est_y = [row[1] for row in est_pos]
plt.scatter(gt_x,gt_y,c='black')
plt.scatter(est_x,est_y,c='blue')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

