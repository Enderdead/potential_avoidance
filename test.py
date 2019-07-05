import random

from deap import base
from deap import creator
from deap import tools


class Individu:

    def __init__(self, target_type, target_param, map_type, map_param, obstacle_type, obstacle_param):
        self.target_type = target_type
        self.target_param = target_param     
        self.map_type = map_type           
        self.obstacle_type = obstacle_type
        self.obstacle_param = obstacle_param


def initrandom

creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individu",Individu )

toolbox = base.Toolbox()
toolbox.register("init_random", random.random)