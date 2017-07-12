import numpy as np
import dimen

class Chunk():
  def __init__(self, pos, size, cube):
    self.pos = pos
    self.size = size
    self.cube = cube

if __name__ == '__main__':
  pos = np.array([1, 2, 3], np.int64)
  size = np.array([4, 8, 4], np.int64)
  cube = np.zeros((size[dimen.X], size[dimen.Y], size[dimen.Z]), np.int64)

  chunk = Chunk(pos, size, cube)

  print(chunk.pos)
  print(chunk.size)
  print(chunk.cube)
