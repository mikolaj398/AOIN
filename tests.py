
import os
import csv
from data_input import *
from solvers import *

DATA_PATH = 'data/'
CSV_HEADER = [
    'max waga', 
    'zachlanny - czas', 
    'zachlanny - wartosc', 
    'zachlanny - waga', 
    'zachlanny - ilosc', 
    'mrowkowy - czas', 
    'mrowkowy - wartosc', 
    'mrowkowy - waga', 
    'mrowkowy - ilosc', 
    'lepszy'
]
def run_tests():
    with open('results.csv', 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)
        for file in os.listdir(DATA_PATH):
            print(file)
            bag_size, items = file_input(DATA_PATH + file)

            bag_size_greedy, value_greedy, items_greedy, elapsed_time_greedy = greedy_search(bag_size, items)
            bag_size_aco, value_aco, items_aoc, elapsed_time_aoc = ant_colony(bag_size, items)
            result = [
                bag_size, 
                elapsed_time_greedy, 
                value_greedy,
                bag_size_greedy,
                len(items_greedy), 
                elapsed_time_aoc, 
                value_aco, 
                bag_size_aco,
                len(items_aoc),
            ]

            if value_greedy > value_aco:
                result.append('zachlanny')
            else:
                result.append('mrowkowy')

            writer.writerow(result)
