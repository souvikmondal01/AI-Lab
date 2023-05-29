import random


def fitness_function(chromosome):
    return sum(chromosome)


def genetic_algorithm(population_size, chromosome_length, fitness_function, mutation_probability=0.1):
    population = [[random.randint(0, 1) for j in range(chromosome_length)] for i in range(population_size)]
    while True:
        fitness_values = [fitness_function(chromosome) for chromosome in population]
        parents = [population[i] for i in range(population_size) if fitness_values[i] == max(fitness_values)]
        next_generation = []
        while len(next_generation) < population_size:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            crossover_point = random.randint(1, chromosome_length - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            for i in range(chromosome_length):
                if random.random() < mutation_probability:
                    child[i] = 1 - child[i]
            next_generation.append(child)
        population = next_generation
        if max(fitness_values) == chromosome_length:
            return parents[0]


chromosome_length = 10
population_size = 50
solution = genetic_algorithm(population_size, chromosome_length, fitness_function)
print("Solution found:", solution)
