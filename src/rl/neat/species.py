from collections import deque
import math
import random


class Species:
    def __init__(self, representative):
        self.representative = representative
        self.genomes = deque([representative])
        self.fitness = None

    
    def size(self):
        return len(self.genomes)


    def compatible(self, genome):
        return self.representative.distance(genome) <= self.representative.neat.genome_distance_threshold
    

    def add_genome(self, genome, check_compatibility=True):
        if check_compatibility and not self.compatible(genome):
            return False
        
        self.genomes.append(genome)
        return True
    

    def sort(self):
        self.genomes = sorted(self.genomes, key=lambda genome: genome.fitness, reverse=True)


    def kill(self, precentage, kill_in_neat=False):
        size = math.ceil(len(self.genomes) * precentage)

        if kill_in_neat:
            for idx in range(size):
                genome = self.genomes.pop()
                genome.neat.genomes.remove(genome)
            
            return
        
        for idx in range(size):
            genome = self.genomes.pop()
        

    def random_genome(self, fitness_prob=True):
        if not fitness_prob:
            return random.choice(self.genomes)

        return random.choices(self.genomes, weights=[genome.fitness for genome in self.genomes])[0]
    

    def breed(self):
        return self.random_genome().crossover(self.random_genome())

    
    def adjust_fitness(self, compute_fitness=False):
        species_size = self.size()

        for genome in self.genomes:
            genome.fitness /= species_size

        if compute_fitness:
            self.compute_fitness()
    

    def compute_fitness(self):
        self.fitness = 0

        for genome in self.genomes:
            self.fitness += genome.fitness