def manual_input():
    """ 
    Read user input to make items list.
    """
    bag_size = int(input('Podaj rozmiar plecaka: '))
    items_count = int(input('Podaj ilosc przedmitow: '))

    items = []
    for item_index in range(items_count):
        item = {}
        item['weight'] = (int(input(f'Waga {item_index + 1} przedmiotu: ')))
        item['value'] = (int(input(f'Wartosc {item_index + 1} przedmiotu: ')))
        items.append(item)

    return bag_size, items

def file_input():
    """ 
    Reads int values in file. First line is a bag size and the rest are item weight and item value
    separated by coma.
    """
    path = input('Podaj sciezke lub nazwe pliku: ')
    with open(path) as data_file:
        lines = data_file.readlines()
        bag_size = int(lines[0])

        items = []
        for i in range(1, len(lines)):
            item = {}
            item['weight'] = (int(lines[i].split(',')[0]))
            item['value'] = (int(lines[i].split(',')[1]))
            items.append(item)

    return bag_size, items