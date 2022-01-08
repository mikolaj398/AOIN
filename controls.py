from data_input import *
from solvers import *
def clear_console():
    for _ in range(100):
        print('\n')

def input_menu():
    option = -1
    while option != 3:
        if option == 1:
            bag_size, items = manual_input()
            solver_menu(bag_size, items)
        if option == 2:
            bag_size, items = file_input()
            solver_menu(bag_size, items)

        # clear_console()
        print('1. Wpisz dane recznie')
        print('2. Wczytaj z pliku')
        print('3. Wyjscie')
        option = int(input())

def solver_menu(bag_size, items):
    option = -1
    while option != 3:
        if option == 1:
            solution_weight, value, taken_items, elapsed_time = greedy_search(bag_size, items)
            pretty_print_solution(solution_weight, value, taken_items, elapsed_time)
        if option == 2:
            solution_weight, value, taken_items, elapsed_time = ant_colony(bag_size, items)
            pretty_print_solution(solution_weight, value, taken_items, elapsed_time)

        # clear_console()
        print('1. Algorytm zachlanny')
        print('2. Algorytm mrowkowy')
        print('3. Wroc')
        option = int(input())

def pretty_print_solution(bag_size, value, taken_items, elapsed_time):
    print(f'Rozwiązanie znaleziono w {elapsed_time} sekund')
    print(f'Waga znalezionego rozwiazania: {bag_size}')
    print(f'Wartosc znalezionego rozwiazania: {value}')
    print('Zawartość plecaka:')
    for item in taken_items:
        print(f"Waga: {item['weight']}, Wartosc: {item['value']}")