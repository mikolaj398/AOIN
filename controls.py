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
            greedy_search(bag_size, items)
            print('no fajny referencyjny')
        if option == 2:
            print('no fajny mrowkowy')

        # clear_console()
        print('1. Algorytm zachlanny')
        print('2. Algorytm mrowkowy')
        print('3. Wroc')
        option = int(input())
