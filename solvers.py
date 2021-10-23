def greedy_search(bag_size, items):
    sorted_items = sorted(items, key=lambda item: item['value']/item['weight'], reverse=True)
    current_bag_size = 0
    taken_items = []

    for item in sorted_items:
        if item['weight'] + current_bag_size < bag_size:
            current_bag_size += item['weight']
            taken_items.append(item)
        else:
            break
    value = sum(taken_items['value'] for item in taken_items])
    return current_bag_size, value, taken_items