#! /usr/bin/env python3

#Before running this script, make sure you're logged in with x-forwarding enabled, then run the next two lines in your terminal window before running this script:
#module load anaconda
#conda activate /panfs/pfs.local/work/eeb/biocs/conda/biocs

import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes instance
fig, ax = plt.subplots()

# Generate list of coordinates on a line, and a manual list
coords = range(0, 200, 10)
x = [20, 50, 160]
y = [170, 12, 37]

# Draw coords of increasing size using a colormap (store instance for color bar
sp = ax.scatter(coords, coords, c=coords, s=coords, cmap="rainbow")

# Draw manual coordinates all in red
ax.scatter(x, y, c="red")

#Add a colorbar to the figure using the scale/colors from the first scatter
fig.colorbar(sp)

plt.show()

