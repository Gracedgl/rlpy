#!/usr/bin/env python

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
__author__ = "William Dabney"

from rlpy.Domains import GridWorld
from rlpy.MDPSolvers import ValueIteration
from rlpy.Representations import Tabular
from rlpy.Policies import GibbsPolicy
from rlpy.Experiments import MDPSolverExperiment
import os


def make_experiment(exp_id=1, path="./Results/Temp", show=False):
    """
    Each file specifying an experimental setup should contain a
    make_experiment function which returns an instance of the Experiment
    class with everything set up.

    @param id: number used to seed the random number generators
    @param path: output directory where logs and results are stored
    """

    # Domain:
    # MAZE                = '/Domains/GridWorldMaps/1x3.txt'
    maze = os.path.join(GridWorld.default_map_dir, '4x5.txt')
    domain = GridWorld(maze, noise=0.3)

    # Representation
    representation = Tabular(domain, discretization=20)

    # Agent
    agent = ValueIteration(
        exp_id,
        representation,
        domain,
        project_path=path,
        show=show)

    return MDPSolverExperiment(agent, domain)

if __name__ == '__main__':
    path = "./Results/Temp/gridworld/ValueIteration/Tabular/"
    experiment = make_experiment(1, path=path)
    experiment.run()
