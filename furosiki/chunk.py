import numpy as np

class Chunk():
  X = 0
  Y = 1
  Z = 2

  def __init__(self, pos, size):
    self.pos = pos
    self.size = size

    self.cube = np.zeros((size[Chunk.Y], size[Chunk.Z], size[Chunk.X]))

if __name__ == '__main__':
  chunk = Chunk(np.array([1, 2, 3]), np.array([2, 4, 2]))
  print(chunk.pos)
  print(chunk.size)
  print(chunk.cube)
