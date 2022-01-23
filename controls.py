from data_input import *
from solvers import *
from tests import run_tests
from generate_data import *
def clear_console():
    for _ in range(100):
        print('\n')

def input_menu():
    option = -1
    while option != 5:
        if option == 1:
            bag_size, items = manual_input()
            solver_menu(bag_size, items)
        if option == 2:
            bag_size, items = file_input()
            solver_menu(bag_size, items)
        if option == 3:
            run_tests()
        if option == 4:
            print('Wpisz ile plików z instancja problemu utworzyc:')
            num_of_files = int(input())
            generate(num_of_files)

        # clear_console()
        print('1. Wpisz dane recznie')
        print('2. Wczytaj z pliku')
        print('3. Testuj')
        print('4. Generuj dane')
        print('5. Wyjscie')
        option = int(input())

def solver_menu(bag_size, items):
    option = -1
    while option != 4:
        if option == 1:
            solution_weight, value, taken_items, elapsed_time = greedy_search(bag_size, items)
            pretty_print_solution(solution_weight, value, taken_items, elapsed_time)
        if option == 2:
            solution_weight, value, taken_items, elapsed_time = ant_colony(bag_size, items)
            pretty_print_solution(solution_weight, value, taken_items, elapsed_time)
        if option == 3:
            print('============== Algorytm zachlanny ==============')
            solution_weight, value, taken_items, elapsed_time = greedy_search(bag_size, items)
            pretty_print_solution(solution_weight, value, taken_items, elapsed_time, list_items = False)
            
            print('============== Algorytm mrowkowy ==============')
            solution_weight, value, taken_items, elapsed_time = ant_colony(bag_size, items)
            pretty_print_solution(solution_weight, value, taken_items, elapsed_time, list_items = False)

        # clear_console()
        print('1. Algorytm zachlanny')
        print('2. Algorytm mrowkowy')
        print('3. Porownaj')
        print('4. Wroc')
        option = int(input())

def pretty_print_solution(bag_size, value, taken_items, elapsed_time, list_items = True):
    print(f'Rozwiązanie znaleziono w {elapsed_time} sekund')
    print(f'Waga znalezionego rozwiazania: {bag_size}')
    print(f'Wartosc znalezionego rozwiazania: {value}')
    if list_items:
        print('Zawartość plecaka:')
        for item in taken_items:
            print(f"Waga: {item['weight']}, Wartosc: {item['value']}")