import random


def objective_function(x):
    return x ** 2


def hill_climbing(objective_function, x_min, x_max, max_iter):
    x = random.uniform(x_min, x_max)
    for i in range(max_iter):
        current_obj = objective_function(x)
        delta = random.uniform(-0.1, 0.1)
        neighbor = x + delta
        neighbor_obj = objective_function(neighbor)
        if neighbor_obj < current_obj:
            x = neighbor
        else:
            return x
    return x


solution = hill_climbing(objective_function, -100, 100, 100)
print("Solution: x = %.2f, f(x) = %.2f" % (solution, objective_function(solution)))
