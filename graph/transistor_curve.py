import matplotlib.pyplot as plt

import matplotlib.font_manager as fm

import numpy as np


y1 = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3,3]

x1 = [0, 319.4e-3, 1.09, 2.301, 3.29, 4.281, 5.27, 6.26, 7.24, 8.23,9.23]


y2 = [0, 4, 9, 13, 13, 13, 14, 14, 14, 15, 16]

x2 = [0, 66.7e-3, 109.6e-3, 206.7e-3, 1.176, 2.098,3.028, 3.958, 4.909, 5.855,6.83]


y3 = [0, 4, 9, 14, 19, 23, 23, 24, 25, 26, 27]

x3 = [0, 49.1e-3, 76.1e-3, 102.2e-3, 138.1e-3, 432.3e-3, 1.314, 2.176, 3.025, 3.862, 4.682]


y4 = [0, 4, 9, 14, 19, 24, 29, 33, 34, 35, 36]

x4 = [0, 39.5e-3, 61.9e-3, 81.7e-3, 104e-3, 120.3e-3, 159.3e-3, 327.7e-3, 1.208, 1.826, 2.741]


y5 = [0, 5, 9, 14, 19, 24, 29, 34, 39, 44, 45]

x5 = [0, 33.3e-3, 52.9e-3, 69.2e-3, 84.6e-3, 100.6e-3, 118.8e-3, 143.3e-3, 190.4e-3, 530e-3, 1.250]


plt.figure(figsize=(10, 6))


plt.plot(x1, y1, 'o-', label='V1 = 1V, Ib = 18.18 uA')

plt.plot(x2, y2, 's--', label='V1 = 2V, Ib = 60.43 uA')

plt.plot(x3, y3, '^-', label='V1 = 3V, Ib = 103.4 uA')

plt.plot(x4, y4, 'x--', label='V1 = 4V, Ib = 146.7 uA')

plt.plot(x5, y5, 'v-', label='V1 = 5V, Ib = 190.2 uA')


plt.xlabel('Vce (V)')

plt.ylabel('Ic (mA)')


plt.grid(True)

plt.legend()


plt.savefig('transistor_graph.png') 