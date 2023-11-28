#!/usr/bin/env python

# ---- MODULE DOCSTRING

__doc__ = """

(C) Hive, Romain Wuilbercq, 2017
     _
    /_/_      .'''.
 =O(_)))) ...'     `.
    \_\              `.    .'''X
                       `..'
.---.  .---..-./`) ,---.  ,---.   .-''-.
|   |  |_ _|\ .-.')|   /  |   | .'_ _   \
|   |  ( ' )/ `-' \|  |   |  .'/ ( ` )   '
|   '-(_{;}_)`-'`"`|  | _ |  |. (_ o _)  |
|      (_,_) .---. |  _( )_  ||  (_,_)___|
| _ _--.   | |   | \ (_ o._) /'  \   .---.
|( ' ) |   | |   |  \ (_,_) /  \  `-'    /
(_{;}_)|   | |   |   \     /    \       /
'(_,_) '---' '---'    `---`      `'-..-'

The Artificial Bee Colony (ABC) algorithm is based on the
intelligent foraging behaviour of honey bee swarm, and was first proposed
by Karaboga in 2005.

"""

# ---- IMPORT MODULES

import math

try:
    import numpy as np
except:
    raise ImportError("Numpy module not installed.")

from Hive import Utilities
from Hive import Hive


# ---- CREATE TEST CASE

def rosenbrock(vector, a=1, b=100):
    """

    The Rosenbrock function is a non-convex function used as a performance test
    problem for optimization algorithms introduced by Howard H. Rosenbrock in
    1960. It is also known as Rosenbrock's valley or Rosenbrock's banana
    function.

    The function is defined by

                        f(x, y) = (a-x)^2 + b(y-x^2)^2

    It has a global minimum at (x, y) = (a, a**2), where f(x, y) = 0.

    """

    vector = np.array(vector)

    return (a - vector[0])**2 + b * (vector[1] - vector[0]**2)**2
    
def rastrigin(vector):
    """
    A n-dimensional Rastrigin's function is defined as:

                            n
            f(x) = 10*n + Sigma { x_i^2 - 10*cos(2*PI*x_i) }
                           i=1

    where  -5.12 <= x_i <= 5.12.

    Thus the global minima of the function being f(x) = 0 at all x_i = 0.

    """

    vector = np.array(vector)

    return 10 * vector.size + sum(vector*vector - 10 * np.cos(2 * np.pi * vector))

def ackley(vector):
    
    vector = np.array(vector)
    
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (vector[0]**2 + vector[1]**2))) - np.exp(0.5 * (np.cos(2 * np.pi * vector[0]) + np.cos(2 * np.pi * vector[1]))) + np.e + 20

def sphere(vector):
    
    vector = np.array(vector)
    
    return np.sum(np.square(vector[0]))


# ---- SOLVE TEST CASE WITH ARTIFICIAL BEE COLONY ALGORITHM
#Media + desvio padrao | 30 experiencias. tabela com resultados

def run():
 
    for item in range(30):
        
        # creates model
        ndim = int(2)
        model = Hive.BeeHive(lower     = [-2.048] *ndim ,
                             upper     = [2.048] *ndim   ,
                             fun       = rosenbrock          ,
                             numb_bees =  100           ,
                             max_itrs  =  100            ,
                             verbose   = False            ,)
    
        # runs model
        cost = model.run()
    
        # plots convergence
        Utilities.ConvergencePlot(cost)
    
        # prints out best solution
        print("{0}".format(model.best))

if __name__ == "__main__":
    run()


# ---- END
