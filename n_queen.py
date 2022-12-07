import random

class Chromosome:
    def __init__(self, gens):
        self.n = len(gens)
        self.gens = gens
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        fitness = 0

        collision_shibs = [-1, 0, 1]

        for i in range(self.n):
            for j in range(i + 1, self.n):
                shib = (self.gens[i] - self.gens[j]) / (i - j)
                if shib in collision_shibs:
                    fitness += 1

        return fitness

    def print_chromosome(self):
        print("Chromosome = {},  Fitness = {}"
            .format(str(self.gens), self.fitness))

    def show(self):
        print()
        print("_" * 30)
        for i in range(self.n):
            for j in range(self.n):
                if self.gens[i] == (j + 1):
                    print('Q', end='')
                else:
                    print('X', end='')
            print()
        print("-" * 30)
        print()

def create_random_chromosome(n) -> Chromosome:
    return Chromosome([random.randint(1, n) for _ in range(n)])
        
def cross_over(first_chrom : Chromosome, second_chrom : Chromosome) -> Chromosome:
    n = first_chrom.n
    ind = random.randint(0, n - 1)
    return Chromosome(first_chrom.gens[0 : ind] + second_chrom.gens[ind : n])

def mutate(chrom : Chromosome) -> Chromosome:
    n = chrom.n
    ind = random.randint(0, n - 1)
    new_val = random.randint(1, n)
    return Chromosome(chrom.gens[0 : ind] + [new_val] + chrom.gens[ind + 1 : n])

def genetic_queen(population):
    mutation_probability = 0.3

    for _ in range(len(population)):
        x = random.choice(population)
        y = random.choice(population)        
        child = cross_over(x, y)
        if random.random() < mutation_probability:
            child = mutate(child)
        population.append(child)
        if child.fitness == 0:
            break

    random.shuffle(population)
    population.sort(key=lambda chrom : chrom.fitness)
    population = population[0 : 1000]
    return population

if __name__ == "__main__":
    n = int(input("Enter Number of Queens: "))
    population = [create_random_chromosome(n) for _ in range(1000)]
    population.sort(key=lambda chrom : chrom.fitness)

    generation = 1

    while not 0 in [chrom.fitness for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population)
        print("")
        print("Minimum Fitness:", min([chrom.fitness for chrom in population]))
        print("Maximum Fitness:", max([chrom.fitness for chrom in population]))
        generation += 1

    print("Solved in Generation {}!".format(generation-1))
    for chrom in population:
        if chrom.fitness == 0:
            chrom.print_chromosome()
            chrom.show()
            break