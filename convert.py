import sys
from dataobj import *
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.mlab import griddata
import numpy as np


def usage():
    print("python3 convert.py <plt filename>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        exit(0)

    d = DataObject(sys.argv[1])

    idx = d.row + 1
    dy = abs(d.y[0] - d.y[idx])
    dx = abs(d.x[1] - d.x[0])
    y, x = np.mgrid[slice(d.y.min(), d.y.max() + dy, dy),
                    slice(d.x.min(), d.x.max() + dx, dx)]
    c = np.ones((d.row, d.col))
    for i in range(d.row):
        for j in range(d.col):
            c[i,j] = d.vorticity[(i * d.col) + j]
    plt.pcolor(x, y, c)
    #plt.pcolormesh(x, y, z)
    #print(d.vorticity)
    plt.colorbar()
    plt.show()
