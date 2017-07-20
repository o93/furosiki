import numpy as np

X = 0
Y = 1
Z = 2

def point(x, y, z):
  return np.array([x, y, z], np.int64)

def space(size):
  return np.zeros((size[X], size[Y], size[Z]), np.int64)
