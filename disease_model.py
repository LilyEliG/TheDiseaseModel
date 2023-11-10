import random

def infect(infection_prob:float) -> bool:
    """Returns True or False indicating whether an infection has occured"""
    return random.uniform(0,1) < infection_prob

def recover(recovery_prob:float) -> bool:
    """Returns True or False indicating whether the person has recovered"""
    return random.uniform(0,1) < recovery_prob

def contact_indices(pop_size:int, source:int, contact_range:int) -> list:
    """Returns the list of indices of people who come into contact with an infected person"""
    indices_list = []
    for index in range(source - contact_range, source + contact_range + 1):
        if index >= 0 and index < pop_size:
            indices_list.append(index)
    return indices_list

def apply_recoveries(population:list, recovery_prob: float) -> None:
    """ Indicates whether a person recovers today or not"""
    for index in range(len(population)):
        if population[index] == 'I' and recover(recovery_prob):
            population[index] = 'R'

def contact(population:list, source:int, contact_range:int, infect_chance:float) -> None:
    """Simulates an infected coming into contact with other, possibly infecting them"""
    indices_list = contact_indices(len(population), source, contact_range)
    for index in indices_list:
        if population[index] == 'S' and infect(infect_chance):
            population[index] = 'I'

def apply_contacts(population:list, contact_range:int, infect_chance:float) -> None:
    """Simulates all the infected people in the population coming into contact with others, possibly infecting them"""
    infection_list = []
    for index in range(len(population)):
        if population[index] == 'I':
            infection_list.append(index)
    for index in infection_list:
        contact(population, index, contact_range, infect_chance)

def population_SIR_counts(population:list) -> dict:
    """Counts the number of people who are susceptible, infected adn recovered and returns the counts in a dictionary"""
    return {"susceptible":population.count('S'), "infected":population.count('I'), "recovered":population.count('R')}

def simulate_day(population:list, contact_range:int, infect_chance:float, recover_chance:float) -> None:
    """Simulates one day in the progression of disease"""
    apply_recoveries(population, recover_chance)
    apply_contacts(population, contact_range, infect_chance)

def initialize_population(pop_size:int) -> list:
    """Initializes the state of the population"""
    population = ['S'] * pop_size #On day 0, the entire population is susceptible except one person who happens to be infected
    population[0] = 'I' 
    return population

def simulate_disease(pop_size:int, contact_range:int, infect_chance:float, recover_chance:float) -> list:
    """Simulates the progression of the disease on each day"""
    population = initialize_population(pop_size)
    counts = population_SIR_counts(population)
    all_counts = [counts]
    while counts['infected'] > 0:
        simulate_day(population, contact_range, infect_chance, recover_chance)
        counts = population_SIR_counts(population)
        all_counts.append(counts)
    return all_counts

#Finds the highest number of infections on a given day
def peak_infections(all_counts:list) -> int:
    """Finds the peak of infections"""
    max_infections = 0
    for day in all_counts:
        if day['infected'] > max_infections:
            max_infections = day['infected']
    return max_infections

def display_results(all_counts:list) -> None:
    """Displays the progression of the disease on each day in the form of a table"""
    num_days = len(all_counts)
    #Prints information in a table format
    print("Day".rjust(12) + "Susceptible".rjust(12) + "Infected".rjust(12) + "Recovered".rjust(12)) 
    for day in range(num_days):
        line = str(day).rjust(12)
        line += str(all_counts[day]["susceptible"]).rjust(12)
        line += str(all_counts[day]["infected"]).rjust(12)
        line += str(all_counts[day]["recovered"]).rjust(12)
        print(line)
    print("\nPeak Infections: {}".format(peak_infections(all_counts)))


