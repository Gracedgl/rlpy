from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import rlpy.Tools.results as rt

paths = {"RBFs": "./Results/Tutorial/InfTrackCartPole/RBFs",
         "Tabular": "./Results/Tutorial/InfTrackCartPole/Tabular"}

merger = rt.MultiExperimentResults(paths)
fig = merger.plot_avg_sem("learning_steps", "return")
rt.save_figure(fig, "./Results/Tutorial/plot.pdf")
