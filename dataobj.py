import numpy as np


class DataObject(object):
    def __init__(self, filename):
        self.rows = []
        self.vars = []
        self.i = 0
        self.j = 0
        self.k = 0

        self.x = []
        self.y = []
        self.u = []
        self.v = []
        self.vorticity = []

        self.setDataFromFile(filename)


    def setDataFromFile(self, filename):
        with open(filename, 'r') as f:
            self.rows = f.readlines()

        # header lines, ditch em since this is for a specific format
        self.rows = self.rows[6:]
        for row in self.rows:
            parts = row.split(' ')
            self.x.append(float(parts[0]))
            self.y.append(float(parts[1]))
            self.u.append(float(parts[2]))
            self.v.append(float(parts[3]))
            self.vorticity.append(.7)#float(parts[4]))

        self.x = np.atleast_2d(self.x)
        self.y = np.atleast_2d(self.y)
        self.u = np.atleast_2d(self.u)
        self.v = np.atleast_2d(self.v)
        self.vorticity = np.atleast_2d(self.vorticity)


    def top(self, count):
        for i in range(count):
            print(self.rows[i])
