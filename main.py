from src.practica1 import *
from practica1 import *
from practica2 import *
from practica3 import *

def main():
    grafo = ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    grafo1 = (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    grafo2 = (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
    
    file_path = 'grafos.txt'
    
    print(encuentra_camino(grafo2,"a","c"))
if __name__ == '__main__':
    main()
