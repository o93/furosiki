import os
import numpy as np
import dimen as dm
import chunk as ck

class Storager():
  def save(self, dir_path, chunk):
    if not os.path.isdir(dir_path):
      os.makedirs(dir_path)

    pos = chunk.pos
    path = dir_path + "/%d_%d_%d.npz" % (pos[dm.X], pos[dm.Y], pos[dm.Z])

    np.savez_compressed(path, chunk.cube)

  def load(self, path, pos):
    pass

if __name__ == '__main__':

  chunk = ck.create(1, 2, 3)
  storager = Storager()
  storager.save("test_data", chunk)
