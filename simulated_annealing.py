import math
import random


def objective_function(x, y):
    return math.sin(x) * math.cos(y)


def acceptance_probability(delta, temperature):
    if delta < 0:
        return 1.0
    else:
        return math.exp(-delta / temperature)


def simulated_annealing(objective_function, x_min, x_max, y_min, y_max, max_iter):
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    current_obj = objective_function(x, y)
    temperature = 1000.0
    cooling_rate = 0.03
    for i in range(max_iter):
        delta_x = random.uniform(-0.1, 0.1)
        delta_y = random.uniform(-0.1, 0.1)
        neighbor_x = x + delta_x
        neighbor_y = y + delta_y
        neighbor_obj = objective_function(neighbor_x, neighbor_y)
        delta_obj = neighbor_obj - current_obj
        if acceptance_probability(delta_obj, temperature) > random.random():
            x = neighbor_x
            y = neighbor_y
            current_obj = neighbor_obj
        temperature *= 1 - cooling_rate
    return (x, y)


solution = simulated_annealing(objective_function, -10, 10, -10, 10, 1000)
print("Solution: x = %.2f, y = %.2f, f(x,y) = %.2f" % (
    solution[0], solution[1], objective_function(solution[0], solution[1])))
