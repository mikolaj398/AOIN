import random


NUMBER_OF_ANTS = 100
NUMBER_OF_ITERATIONS = 150
INIT_PHEROMONES_VALUE = 100
EVAPORATE_RATE = 0.3
MIN_PHEROMONES_VALUE = 1
ALPHA = 3
BETA = 2

def calc_probabilities(current_items, pheromones, attractiveness):
    sum = 0
    for item_id in current_items.keys():
        sum += (pheromones[item_id]**ALPHA)*(attractiveness[item_id]**BETA)
    return { item_id: (pheromones[item_id]**ALPHA)*(attractiveness[item_id]**BETA)/sum for item_id in current_items.keys()}

def select_item(probabilities, available_items):
    choice = random.choices(list(available_items.keys()), weights=probabilities.values())[0]
    return choice

def remove_to_heavy_items(available_items, bag_size, probabilities):
    available_items = { k:v for k,v in available_items.items() if v['weight'] <= bag_size }
    probabilities = { k:v for k,v in probabilities.items() if k in available_items.keys() }
    return available_items, probabilities

def update_pheromones(all_ants_solutions, pheromones, best_profit):
    for key, ant_solution in all_ants_solutions.items():
        z = ant_solution['profit']
        delta = ( 1 / ( 1 + (( best_profit- z ) / best_profit )))
        for item_id in ant_solution['solution'].keys():
            pheromones[item_id] = max(MIN_PHEROMONES_VALUE, (pheromones[item_id] + delta)*EVAPORATE_RATE)

    return pheromones

def func(bag_size, items):
    pheromones = { key: INIT_PHEROMONES_VALUE for key in items.keys() }
    attractiveness = {key: proprties['value']/(proprties['weight']/bag_size) for key, proprties in items.items() }

    global_profit = 0
    global_solution = {}

    for _ in range(NUMBER_OF_ITERATIONS):
        probabilities = calc_probabilities(items, pheromones, attractiveness)        
        ant_profit = 0
        ant_solution = {}
        all_ants_solutions = {}

        for ant in range(NUMBER_OF_ANTS):
            local_profit = 0
            local_solution = {}
            current_capacity = bag_size
            available_items = items
            probabilities_for_ant = probabilities

            while current_capacity > 0:
                available_items, probabilities_for_ant = remove_to_heavy_items(available_items, current_capacity, probabilities_for_ant)
                if (len(available_items.keys()) == 0 or sum(probabilities_for_ant.values()) == 0):
                    break
                item_id = select_item(probabilities_for_ant, available_items)
                
                local_solution[item_id] = items[item_id]
                current_capacity -= items[item_id]['weight']
                local_profit += items[item_id]['value']

                del available_items[item_id]
                del probabilities_for_ant[item_id]
        
            if local_profit > ant_profit:
                ant_profit = local_profit
                ant_solution = local_solution
        
            all_ants_solutions[str(ant)] = {
                'profit': local_profit,
                'solution': local_solution,
            }
    
        if ant_profit > global_profit:
            global_profit = ant_profit
            global_solution = ant_solution
    
        pheromones = update_pheromones(all_ants_solutions, pheromones, global_profit)

    current_bag_size = 0
    for item in global_solution.values():
        current_bag_size += item['weight']

    return current_bag_size, global_profit, global_solution