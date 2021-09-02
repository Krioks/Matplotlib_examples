from prepare_graph import PrepareSimpleGraph, PreparePolarGraph

from simple_examples import *
from polar_examples import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

x = np.linspace(1, 10, 1000)
t = np.linspace(-160 * np.pi, 160 * np.pi, 10000)


# with PrepareSimpleGraph('Presentation/Files/tangent.pdf') as psg:
#     graph, text,  = tangent(x)
#     psg.ax.plot(x, graph,  label=text)
#     # pg.ax.plot(x, hyperbola(x),label=rf'$y = \dfrac{{1}}{{x}}$')
#     # pg.ax.plot(x, np.sin(x*4), label=rf'$y = \sin(x)$')
#     psg.ax.legend(loc=1)

# with PreparePolarGraph('Presentation/Files/rose5.pdf') as ppg:
#     graph, text, = rose(t, 1, 5, 9)
#
#     ppg.ax.plot(t, graph, label=text)
#     # ppg.ax.plot(t, np.sin((3/5)*t), label=rf'$ \rho = \phi$')
#     ppg.ax.legend(loc=1)

