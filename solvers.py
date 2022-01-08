from timer import solver_timer
import aco

@solver_timer
def greedy_search(bag_size, items):
    sorted_items = {k: v for k,v in sorted(items.items(), key=lambda item: item[1]['value']/item[1]['weight'], reverse=True)}
    current_bag_size = 0
    taken_items = []

    for item in sorted_items.values():
        if item['weight'] + current_bag_size < bag_size:
            current_bag_size += item['weight']
            taken_items.append(item)
        else:
            break
    value = sum(item['value'] for item in taken_items)
    return current_bag_size, value, taken_items

@solver_timer
def ant_colony(bag_size, items):

    current_bag_size, value, taken_items = aco.func(bag_size, items)
    return current_bag_size, value, taken_items.values()
    