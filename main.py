import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from itertools import combinations

# How large to make the x and y axis
FIG_RANGE = 10

# How many circles to generate
CIRCLE_NO = 7

# How many times to try the gradient descent
# Lowest cost among all iterations will be selected
ITER_NO = 10


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
    centers = np.array(list(zip(xs[::2], xs[1::2])))

    # Return the total cost
    return distance_cost(centers) + overlap_cost(centers)


# The best solution, the iteration during which it was found, and its cost
xs_min, it_min, cost_min = None, None, FIG_RANGE ** 2

for it in range(ITER_NO):
    # Start with random circles
    init = (np.random.rand(1, 2 * CIRCLE_NO) * FIG_RANGE - (FIG_RANGE / 2)).flatten()
    # Minimize with gradient descent
    result = minimize(cost, init, method="BFGS", options={"disp": False})
    # Check against the best result
    if result.fun < cost_min:
        xs_min, iter_min, cost_min = result.x, it, result.fun


# Show the final result
print(f"Found best solution:\n{xs_min}")
print(f"Iteration: {iter_min}/{ITER_NO}, cost = {cost_min}")

# Create a plot
fig, ax = plt.subplots()
ax.set_xlim(-FIG_RANGE, FIG_RANGE)
ax.set_ylim(-FIG_RANGE, FIG_RANGE)

# Sets the aspect ratio to 1:1
# Otherwise, the circles will look like ellipses
ax.set_box_aspect(1)

# Make the grid visible
ax.set_xticks([x - FIG_RANGE for x in range(0, 2 * FIG_RANGE + 1)])
ax.set_yticks([y - FIG_RANGE for y in range(0, 2 * FIG_RANGE + 1)])
ax.grid(visible=True, alpha=0.15, zorder=0.5)

# Add the surrounding circles
for center in zip(xs_min[::2], xs_min[1::2]):
    x, y = center[0], center[1]
    cir = plt.Circle((x, y), 1, fill=False, color="blue", zorder=1)
    ax.add_patch(cir)

# Add the center circle
circle = plt.Circle((0, 0), 1, fill=False, color="black", zorder=1, lw=1.5)
ax.add_patch(circle)

# Show the figure
plt.show()