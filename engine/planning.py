import numpy as np
import logging
from numpy.random import randint
from random import random as rnd
from random import gauss, randrange

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
                prefered_employees = self.fitness_calculation.get_list_of_prefered_employees(x, shift)

                employee = None
                for prefered_employee in prefered_employees:
                    if not prefered_employee in shift:
                        employee = prefered_employee

                if not employee:
                    employee = randint(lower_limit,upper_limit + 1)
                    while employee in shift:
                        employee = randint(lower_limit,upper_limit + 1)

                shift.append(employee)
            gens.append(shift)

        logger.info('individual generator: %s', gens)  
        return gens

    def population(self, number_of_individuals,
                number_of_genes, number_of_shifts, upper_limit, lower_limit):
        return [self.individual(number_of_genes, number_of_shifts, upper_limit, lower_limit) 
            for x in range(number_of_individuals)]


    def roulette(self, cum_sum, chance):
        veriable = list(cum_sum.copy())
        veriable.append(chance)
        veriable = sorted(veriable)
        return veriable.index(chance)

    def selection(self, generation, method='Fittest Half'):
        generation['Normalized Fitness'] = \
            sorted([generation['Fitness'][x]/sum(generation['Fitness']) 
            for x in range(len(generation['Fitness']))], reverse = True)
        generation['Cumulative Sum'] = np.array(
            generation['Normalized Fitness']).cumsum()
        if method == 'Roulette Wheel':
            selected = []
            for x in range(len(generation['Individuals'])//2):
                selected.append(self.roulette(generation
                    ['Cumulative Sum'], rnd()))
                while len(set(selected)) != len(selected):
                    selected[x] = \
                        (self.roulette(generation['Cumulative Sum'], rnd()))
            selected = {'Individuals': 
                [generation['Individuals'][int(selected[x])]
                    for x in range(len(generation['Individuals'])//2)]
                    ,'Fitness': [generation['Fitness'][int(selected[x])]
                    for x in range(
                        len(generation['Individuals'])//2)]}
        elif method == 'Fittest Half':
            selected_individuals = [generation['Individuals'][-x-1]
                for x in range(int(len(generation['Individuals'])//2))]
            selected_fitnesses = [generation['Fitness'][-x-1]
                for x in range(int(len(generation['Individuals'])//2))]
            selected = {'Individuals': selected_individuals,
                        'Fitness': selected_fitnesses}
        elif method == 'Random':
            selected_individuals = \
                [generation['Individuals']
                    [randint(1,len(generation['Fitness']))]
                for x in range(int(len(generation['Individuals'])//2))]
            selected_fitnesses = [generation['Fitness'][-x-1]
                for x in range(int(len(generation['Individuals'])//2))]
            selected = {'Individuals': selected_individuals,
                        'Fitness': selected_fitnesses}
        return selected

    def pairing(self, elit, selected, method = 'Fittest'):
        individuals = [elit['Individuals']]+selected['Individuals']
        fitness = [elit['Fitness']]+selected['Fitness']
        if method == 'Fittest':
            parents = [[individuals[x],individuals[x+1]] 
                    for x in range(len(individuals)//2)]
        if method == 'Random':
            parents = []
            for x in range(len(individuals)//2):
                parents.append(
                    [individuals[randint(0,(len(individuals)-1))],
                    individuals[randint(0,(len(individuals)-1))]])
                while parents[x][0] == parents[x][1]:
                    parents[x][1] = individuals[
                        randint(0,(len(individuals)-1))]
        if method == 'Weighted Random':
            normalized_fitness = sorted(
                [fitness[x] /sum(fitness) 
                for x in range(len(individuals)//2)], reverse = True)
            cummulitive_sum = np.array(normalized_fitness).cumsum()
            parents = []
            for x in range(len(individuals)//2):
                parents.append(
                    [individuals[self.roulette(cummulitive_sum,rnd())],
                    individuals[self.roulette(cummulitive_sum,rnd())]])
                while parents[x][0] == parents[x][1]:
                    parents[x][1] = individuals[
                        self.roulette(cummulitive_sum,rnd())]
        return parents

    def mating(self, parents, method='Order'):
        if method == 'Order':
            offsprings = []

            shift = randint(0, len(parents[0]))

            length = len(parents[0][shift])

            high = max(1, length - 2)
            left_index = randint(0, high)
            high = max(left_index + 2, length - 1)
            right_index = randint(left_index + 1, high)

            section_to_insert_1 = parents[0][shift][left_index:right_index]
            section_to_insert_2 = parents[1][shift][left_index:right_index]

            mated_parnet_0 = parents[0].copy()
            mated_parent_1 = parents[1].copy()

            mated_parnet_0[shift] = self.order_crossover(parents[1][shift], section_to_insert_1, length, left_index)
            mated_parent_1[shift] = self.order_crossover(parents[0][shift], section_to_insert_2, length, left_index)

            offsprings.append(mated_parnet_0)
            offsprings.append(mated_parent_1)

        if method == 'Single Point':
            pivot_point = randint(1, len(parents[0]))
            offsprings = [parents[0] \
                [0:pivot_point]+parents[1][pivot_point:]]
            offsprings.append(parents[1]
                [0:pivot_point]+parents[0][pivot_point:])
        if method == 'Two Pionts':
            pivot_point_1 = randint(1, len(parents[0]-1))
            pivot_point_2 = randint(1, len(parents[0]))
            while pivot_point_2<pivot_point_1:
                pivot_point_2 = randint(1, len(parents[0]))
            offsprings = [parents[0][0:pivot_point_1]+
                parents[1][pivot_point_1:pivot_point_2]+
                [parents[0][pivot_point_2:]]]
            offsprings.append([parents[1][0:pivot_point_1]+
                parents[0][pivot_point_1:pivot_point_2]+
                [parents[1][pivot_point_2:]]])
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

    def mutation(self, individual, upper_limit, lower_limit, muatation_rate=2, 
        method='Replace', standard_deviation = 0.001):
        mutated_individual = individual.copy()
        if method == 'Gauss':
            for x in range(muatation_rate):
                mutated_individual[x] = \
                round(individual[x]+gauss(0, standard_deviation), 1)
        if method == 'Reset':
            for x in range(muatation_rate):
                mutated_individual[x] = round(rnd()* \
                    (upper_limit-lower_limit)+lower_limit,1)
        if method == 'Replace':

            for x in range(muatation_rate):
                new_gene = randint(lower_limit, upper_limit + 1)
                shift = randint(0, len(individual) - 1)
                position = randint(0, len(individual[shift]) - 1)
                
                if new_gene in individual[shift]:
                    gene_index = individual[shift].index(new_gene)
                    old_gene = mutated_individual[shift][position]
                    mutated_individual[shift][position] = new_gene
                    mutated_individual[shift][gene_index] = old_gene
                else:
                    mutated_individual[shift][position] = new_gene

        return mutated_individual

    def next_generation(self, gen, upper_limit, lower_limit):
        elit = {}
        next_gen = {}
        elit['Individuals'] = gen['Individuals'].pop(-2)
        elit['Fitness'] = gen['Fitness'].pop(-2)
        selected = self.selection(gen)
        parents = self.pairing(elit, selected)
        offsprings = [[[self.mating(parents[x])
                        for x in range(len(parents))]
                        [y][z] for z in range(2)] 
                        for y in range(len(parents))]
        offsprings1 = [offsprings[x][0]
                    for x in range(len(parents))]
        offsprings2 = [offsprings[x][1]
                    for x in range(len(parents))]
        unmutated = selected['Individuals']+offsprings1+offsprings2
        mutated = [self.mutation(unmutated[x], upper_limit, lower_limit) 
            for x in range(len(gen['Individuals']))]
        unsorted_individuals = mutated + [elit['Individuals']]
        unsorted_next_gen = \
            [self.fitness_calculation.calculate(mutated[x]) 
            for x in range(len(mutated))]
        unsorted_fitness = [unsorted_next_gen[x]
            for x in range(len(gen['Fitness']))] + [elit['Fitness']]
        sorted_next_gen = \
            sorted([[unsorted_individuals[x], unsorted_fitness[x]]
                for x in range(len(unsorted_individuals))], 
                    key=lambda x: x[1])
        next_gen['Individuals'] = [sorted_next_gen[x][0]
            for x in range(len(sorted_next_gen))]
        next_gen['Fitness'] = [sorted_next_gen[x][1]
            for x in range(len(sorted_next_gen))]
        gen['Individuals'].append(elit['Individuals'])
        gen['Fitness'].append(elit['Fitness'])
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
        fitness = [self.fitness_calculation.calculate(pop[x])
            for x in range(len(pop))]
        sorted_fitness = sorted([[pop[x], fitness[x]]
            for x in range(len(pop))], key=lambda x: x[1])
        population = [sorted_fitness[x][0] 
            for x in range(len(sorted_fitness))]
        fitness = [sorted_fitness[x][1] 
            for x in range(len(sorted_fitness))]
        return {'Individuals': population, 'Fitness': sorted(fitness)}

    def solve(self, number_of_individuals, number_of_genes, number_of_shifts, upper_limit, lower_limit):

        pop = self.population(number_of_individuals, number_of_genes, number_of_shifts, upper_limit, lower_limit)
        gen = []
        gen.append(self.first_generation(pop))
        fitness_avg = np.array([sum(gen[0]['Fitness'])/
                                len(gen[0]['Fitness'])])
        fitness_max = np.array([max(gen[0]['Fitness'])])

        finish = False
        while finish == False:
            if len(gen) > 10:
                print(fitness_max)
                break
            
            selection = 2
            if len(gen) < 2:
                selection = 1

            gen.append(self.next_generation(gen[-selection],upper_limit,lower_limit))
            fitness_avg = np.append(fitness_avg, sum(
                gen[-selection]['Fitness'])/len(gen[-selection]['Fitness']))
            fitness_max = np.append(fitness_max, max(gen[-selection]['Fitness']))

        return gen[-2]