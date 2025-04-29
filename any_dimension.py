import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from itertools import combinations

# How large to make the axes
FIG_RANGE = 10

# How many circles to generate
CIRCLE_NO = 13

# How many times to try the gradient descent
# Lowest cost among all iterations will be selected
ITER_NO = 10

# In what dimension to solve the problem
DIMENSION = 3


# Cost function
def cost(xs):
    # Punish for being away from the center circle
    # Greater distance => greater loss
    def distance_cost(cs):
        total = 0
        for center in cs:
            dist = np.linalg.norm(center) - 2
            total += np.abs(dist)
        return total
    
    # Punish for overlapping with another circle
    # Greater overlap => greater loss
    def overlap_cost(cs):
        total = 0
        for pair in combinations(cs, 2):
            c1, c2 = pair[0], pair[1]
            dist = np.linalg.norm(c1 - c2)
            # Only punish overlapping circles
            if dist < 2:
                total += (2 - dist) ** 2

        return total
    
    # Pack the array into an array of circle centers
    centers = np.array(list(zip(*[xs[i::DIMENSION] for i in range(DIMENSION)])))

    # Return the total cost
    return distance_cost(centers) + overlap_cost(centers)


# The best solution, the iteration during which it was found, and its cost
xs_min, it_min, cost_min = None, None, FIG_RANGE ** 2

for it in range(ITER_NO):
    # Start with random circles
    init = (np.random.rand(1, DIMENSION * CIRCLE_NO) * FIG_RANGE - (FIG_RANGE / 2)).flatten()
    # Minimize with gradient descent
    result = minimize(cost, init, method="BFGS", options={"disp": False})
    # Check against the best result
    if result.fun < cost_min:
        xs_min, iter_min, cost_min = result.x, it, result.fun


# Show the final result
print(f"Found best solution:\n{xs_min}")
print(f"Iteration: {iter_min}/{ITER_NO}, cost = {cost_min}")