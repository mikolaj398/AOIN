def manual_input():
    bag_size = int(input('Podaj rozmiar plecaka: '))
    items_count = int(input('Podaj ilosc przedmitow: '))

    items_weights = []
    for item_index in range(items_count):
        items_weights.append(int(input(f'Waga {item_index + 1} przedmiotu: ')))

    return bag_size, items_weights

def file_input():
    """ Reads int values in file. First line is a bag size and the rest are item weights"""
    path = input('Podaj sciezke lub nazwe pliku: ')
    with open(path) as data_file:
        lines = data_file.readlines()
        bag_size = int(lines[0])

        items_weights = [] 
        for i in range(1, len(lines)):
            items_weights.append(int(lines[i]))

    return bag_size, items_weights