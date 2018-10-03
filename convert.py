import sys 
from dataobj import *
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.mlab import griddata


def usage():
    print("python3 convert.py <plt filename>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        exit(0)

    d = DataObject(sys.argv[1])
    
    plt.pcolor(d.x, d.y, d.vorticity, vmin=0, vmax=1)
    plt.colorbar()
    plt.show()
