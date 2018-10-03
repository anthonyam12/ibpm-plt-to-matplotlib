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

        # TODO: read these from headers
        self.row = 199
        self.col = 199

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
            self.vorticity.append(float(parts[4]))

        self.x = np.asarray(self.x)
        self.y = np.asarray(self.y)
        self.u = np.asarray(self.u)
        self.v = np.asarray(self.v)
        self.vorticity = np.asarray(self.vorticity)


    def top(self, count):
        for i in range(count):
            print(self.rows[i])
