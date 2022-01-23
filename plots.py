import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')
df = df.sort_values('max waga')


def save_plot(x, y1, y2, label1, label2, title, y_label,file_name):
    plt.plot(x,y1, label = label1)
    plt.plot(x,y2, label = label2)
    plt.legend()
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel('Rozmiar plecaka')
    plt.savefig(f"plots/{file_name}")
    plt.show()
    
save_plot(df['max waga'], df['zachlanny - ilosc'],  df['mrowkowy - ilosc'],'Ilość przedmiotów alg. zachłanny', 'Ilość przedmiotów alg. mrówkowy','Porównanie ilości włożonych do plecaka przedmiotów', 'Ilosc włożonych przedmiotów' ,'plot1.png' )
save_plot(df['max waga'], df['zachlanny - waga'],  df['mrowkowy - waga'],'Wagi rozwiązania alg. zachłanny', 'Wagi rozwiązania alg. mrówkowy','Porównanie wag znalezionych rozwiązań', 'Wagi znalezionych rozwiązań' ,'plot2.png' )
save_plot(df['max waga'], df['zachlanny - wartosc'],  df['mrowkowy - wartosc'],'Wartość przedmiotów alg. zachłanny', 'Wartość przedmiotów alg. mrówkowy','Porównanie wartości włożonych do plecaka przedmiotów', 'Wartości znalezionych rozwiązań', 'plot3.png' )
save_plot(df['max waga'], df['zachlanny - czas'],  df['mrowkowy - czas'],'Czas wykonania alg. zachłanny', 'Czas wykonania alg. mrówkowy','Porównanie czasu wykonania obu algorytmów', 'Czas wykonania algorytmu [s]', 'plot4.png' )
