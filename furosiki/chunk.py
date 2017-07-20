import numpy as np
import dimen as dm

class Chunk():
  def __init__(self, pos, size, cube):
    self.pos = pos
    self.size = size
    self.cube = cube

def create(x, y, z):
  pos = dm.point(x, y, z)
  size = dm.point(4, 8, 4)
  cube = dm.space(size)
  return Chunk(pos, size, cube)

if __name__ == '__main__':
  chunk = create(1, 2, 3)

  print(chunk.pos)
  print(chunk.size)
  print(chunk.cube)
