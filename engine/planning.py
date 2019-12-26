import numpy as np
import logging
from numpy.random import randint
from random import random as rnd
from random import gauss, randrange
from .individual import Individual

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info('welcome to planning')

class GAPlanning:

    def __init__(self, fitness_calculation):
        self.fitness_calculation = fitness_calculation

    def individual(self, number_of_genes, number_of_shifts, upper_limit, lower_limit):
        gens=[]

        for s in range(number_of_shifts):
            shift = []
            for x in range(number_of_genes):
                
                employee = randint(lower_limit,upper_limit + 1)
                while employee in shift:
                    employee = randint(lower_limit,upper_limit + 1)

                shift.append(employee)
            gens.append(shift)

        logger.info('individual generator: %s', gens)  
        return gens

    def greedy(self, number_of_genes, number_of_shifts, upper_limit):

        solution = []
        forbidden_employees = []

        for s in range(number_of_shifts):
            shift = []
            for x in range(number_of_genes):

                if len(forbidden_employees) == upper_limit:
                    forbidden_employees = []
                
                employee_list = self.fitness_calculation.get_list_of_prefered_employees(x)
                count = -1
                employee = employee_list[count]['id']
                while employee in shift or employee in forbidden_employees:
                    count = count - 1
                    employee = employee_list[count]['id']

                forbidden_employees.append(employee)
                shift.append(employee)

            solution.append(shift)

        logging.info('Greedy Solution: %s', solution)
        return solution

    def population(self, number_of_individuals,
                number_of_genes, number_of_shifts, upper_limit, lower_limit):
        population = [self.individual(number_of_genes, number_of_shifts, upper_limit, lower_limit) 
            for x in range(number_of_individuals - 1)]

        population.append(self.greedy(number_of_genes, number_of_shifts, upper_limit))

        return population

    def selection(self, generation, method='Fittest Half'):
        fittest_half = int(len(generation)) // 2
        selected = generation[-fittest_half:].copy()

        return selected

    def pairing(self, elit, selected, method = 'Fittest'):
        individuals = [elit].copy() +selected
        if method == 'Fittest':
            parents = [[individuals[x],individuals[x+1]] 
                    for x in range(len(individuals)//2)]

        return parents

    def mating(self, parents, method='Order'):
        if method == 'Order':
            offsprings = []

            shift = randint(0, len(parents[0].genstring))

            length = len(parents[0].genstring[shift])

            high = max(1, length - 2)
            left_index = randint(0, high)
            high = max(left_index + 2, length - 1)
            right_index = randint(left_index + 1, high)

            section_to_insert_1 = parents[0].genstring[shift][left_index:right_index]
            section_to_insert_2 = parents[1].genstring[shift][left_index:right_index]

            mated_parnet_0 = parents[0].copy()
            mated_parent_1 = parents[1].copy()

            mated_parnet_0.genstring[shift] = self.order_crossover(parents[1].genstring[shift], section_to_insert_1, length, left_index)
            mated_parent_1.genstring[shift] = self.order_crossover(parents[0].genstring[shift], section_to_insert_2, length, left_index)

       
            mated_parnet_0.fitness = self.fitness_calculation.calculate(mated_parnet_0.genstring)
            mated_parent_1.fitness = self.fitness_calculation.calculate(mated_parent_1.genstring)
            
            offsprings.append(mated_parnet_0)
            offsprings.append(mated_parent_1)

        return offsprings

    def order_crossover(self, parent, section_to_insert, length, left_index):
        offspring = []

        i = 0
        j = 0

        while i < left_index :
            if not parent[j] in section_to_insert:
                offspring.append(parent[j])
                i = i + 1

            j = j + 1

        for to_insert in section_to_insert:
            offspring.append(to_insert)

        i = i + len(section_to_insert)

        while i < length:
            if not parent[j] in section_to_insert:
                offspring.append(parent[j])
                i = i + 1

            j = j + 1
        
        return offspring

    def mutation(self, individual, upper_limit, lower_limit, muatation_rate=4, 
        method='Replace', standard_deviation = 0.001):

        if method == 'Replace':

            for x in range(muatation_rate):
                new_gene = randint(lower_limit, upper_limit + 1)
                shift = randint(0, len(individual.genstring))
                position = randint(0, len(individual.genstring[shift]) - 1)
                
                if new_gene in individual.genstring[shift]:
                    gene_index = individual.genstring[shift].index(new_gene)
                    old_gene = individual.genstring[shift][position]
                    individual.genstring[shift][position] = new_gene
                    individual.genstring[shift][gene_index] = old_gene
                else:
                    individual.genstring[shift][position] = new_gene

        return individual

    def next_generation(self, generation, upper_limit, lower_limit):
        elit = {}
        next_gen = {}

        elit = generation.pop(-1)
        elit_copy = Individual(elit.genstring.copy(), elit.fitness)
        selected = self.selection(generation)
        parents = self.pairing(elit, selected)

        offsprings = [[[self.mating(parents[x])
                        for x in range(len(parents))]
                        [y][z] for z in range(2)] 
                        for y in range(len(parents))]
        offsprings1 = [offsprings[x][0]
                    for x in range(len(parents))]
        offsprings2 = [offsprings[x][1]
                    for x in range(len(parents))]
                    
        unmutated = selected + offsprings1+offsprings2

        mutated = [self.mutation(unmutated[x], upper_limit, lower_limit) 
            for x in range(len(generation))]

        for individual in mutated:
            new_fitness = self.fitness_calculation.calculate(individual.genstring)
            individual.fitness = new_fitness

        unsorted_individuals = mutated + [elit_copy]

        next_gen = sorted(unsorted_individuals, key=lambda individual: individual.fitness)

        generation.append(elit_copy)
        return next_gen

    def fitness_similarity_chech(self, max_fitness, number_of_similarity):
        result = False
        similarity = 0
        for n in range(len(max_fitness)-1):
            if max_fitness[n] == max_fitness[n+1]:
                similarity += 1
            else:
                similarity = 0
        if similarity == number_of_similarity-1:
            result = True
        return result

    def first_generation(self, pop):

        individuals = []
        for individual in pop:
            individuals.append(Individual(individual, self.fitness_calculation.calculate(individual)))

        sorted_individuals = sorted(individuals, key=lambda individual: individual.fitness)

        return sorted_individuals

    def solve(self, number_of_individuals, number_of_genes, number_of_shifts, upper_limit, lower_limit):

        pop = self.population(number_of_individuals, number_of_genes, number_of_shifts, upper_limit, lower_limit)
        gen = []
        gen.append(self.first_generation(pop))

        fitness_max = np.array(max(individual.fitness for individual in (gen[0])))

        finish = False
        while finish == False:
            if len(gen) > 20:
                print(fitness_max)
                break
        

            if len(gen) > 10:
                count = -10

                last_element_euqal = True

                while last_element_euqal and count < -1:
                    last_element_euqal = fitness_max[count] == fitness_max[count + 1]

                    if not last_element_euqal:
                        break
                    count = count + 1

                if last_element_euqal:
                    print(fitness_max)
                    break

            selection = 1

            gen.append(self.next_generation(gen[-selection],upper_limit,lower_limit))
           
            fitness_max = np.append(fitness_max, max(individual.fitness for individual in (gen[-selection])))

        return gen[-2]