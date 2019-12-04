import numpy as np
from collections import Counter
 
def srednia(x):
    return sum(x)/len(x)
 
def mediana(x):
    x.sort()
    index = int(len(x)/2)
    if (len(x)%2 == 0):
        return (x[index-1]+x[index])/2
    else:
        return x[index]
   
def dominanta(x):
    c = Counter(x)
    return c.most_common(1)[0][0]
 
def wariancja(x):
    sr = srednia(x)
    suma = 0
    for i in range(len(x)-1):
        suma = suma + (x[i] - sr)**2
    return suma/len(x)
 
def odchylenie(x):
    return wariancja(x)**0.5
 
def skosnosc(x):
    sr = srednia(x)
    suma = 0
    for i in range(len(x)-1):
        suma = suma + (x[i] - sr)**3
    return (suma/len(x))/odchylenie(x)**3
 
def kurtoza(x):
    sr = srednia(x)
    suma = 0
    for i in range(len(x)-1):
        suma = suma + (x[i] - sr)**4
    return ((suma/len(x))/odchylenie(x)**4)-3