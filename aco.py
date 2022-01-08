import random


NUMBER_OF_ANTS = 100
NUMBER_OF_ITERATIONS = 20
INIT_PHEROMONES_VALUE = 10
EVAPORATE_RATE = 0.9
MIN_PHEROMONES_VALUE = 1
ALPHA = 3
BETA = 2

def calc_probabilities(current_items, pheromones, attractiveness):
    sum = 0
    for item_id in current_items.keys():
        sum += (pheromones[item_id]**ALPHA)*(attractiveness[item_id]**BETA)
    return { item_id: (pheromones[item_id]**ALPHA)*(attractiveness[item_id]**BETA)/sum for item_id in current_items.keys()}

def select_item(probabilities, available_items):
    choice = '-1'
    while choice not in available_items.keys():
        choice = random.choices(list(probabilities.keys()), weights=probabilities.values())[0]
    return choice

def remove_to_heavy_items(available_items, bag_size):
    return { k:v for k,v in available_items.items() if v['weight'] <= bag_size }

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
        print(_)
        probabilities = calc_probabilities(items, pheromones, attractiveness)        
        ant_profit = 0
        ant_solution = {}
        all_ants_solutions = {}

        for ant in range(NUMBER_OF_ANTS):
            local_profit = 0
            local_solution = {}
            current_capacity = bag_size
            available_items = items

            while current_capacity > 0:
                available_items = remove_to_heavy_items(available_items, current_capacity)
                if (len(available_items.keys()) == 0):
                    break
                item_id = select_item(probabilities, available_items)
                
                local_solution[item_id] = items[item_id]
                current_capacity -= items[item_id]['weight']
                local_profit += items[item_id]['value']

                del available_items[item_id]
        
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