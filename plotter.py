import numpy as np
import matplotlib.pylab as plt

from simulator import FieldSimulator
from simulator import MtxType as MT


mtx = FieldSimulator(20, 10, 2, MT.RAD_GRAD_NOISE)

for row in range(mtx.m_size):
    for col in range(mtx.m_size):
        print(mtx.m_sim_mtx[row][col])
        
figure = plt.figure()
axis = figure.add_subplot(1, 1, 1)
axis.set_aspect('equal')

plt.imshow(mtx.m_sim_mtx, interpolation = 'nearest', cmap = plt.cm.plasma)
plt.colorbar()
plt.show()