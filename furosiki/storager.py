import numpy as np
import chunk as ck

class Storager():
  def save(self, chunk):
    pos = chunk.pos
    np.savez_compressed("%d_%d_%d.npz" % (pos.x, pos.y, pos.z), chunk.cube)

  def load(self, pos):
    pass

if __name__ == '__main__':

  chunk = ck.create(1, 2, 3)
  storager = Storager()
  storager.save(chunk)
