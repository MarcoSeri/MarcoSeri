#! /usr/bin/python

# 1ra Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys

from practica2 import componentes_conexas, cuenta_grado, es_conexo, vertice_aislado
from practica3 import *
def lee_grafo_stdin(grafo):

    lista = []
    count = int(grafo[0])
    lista = grafo[1:count+1]    

    listarecorridos = []
    for element in grafo:
        if ' ' in element:
            vertices = element.split(' ')
            listarecorridos.append((vertices[0],vertices[1]))

    print(lista,listarecorridos)

    pass
"""
    Recibe como argumento un grafo representado como una lista de tipo:
    Ejemplo Entrada: 
       ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    
    donde el 1er elemento se corresponde a la cantidad de vertices,
    y por ultimo las aristas existentes.

    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    """

def lee_grafo_archivo(file_path):
    archivo = open(file_path)
    num = int(archivo.readline())
    
    listanum = []
    listarecorridos = []

    for i in range(num):
        linea = archivo.readline(i)
        listanum.append(linea.strip())

    for linea in archivo:
        nodos_arista = linea.strip().split()
        if len(nodos_arista) == 2:
            arista = (nodos_arista[0], nodos_arista[1])
            listarecorridos.append(arista)

    return listanum, listarecorridos
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    pass

def imprime_grafo_lista(grafo):
    lista = []
    count = int(grafo[0])
    lista = grafo[1:count+1]
    return lista
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    pass

#################### FIN EJERCICIO PRACTICA ####################
def lee_entrada_1():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    '''
    data_input = []
    
    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            data_input.append(line.strip())
            
    return data_input

    
def lee_entrada_2():
    count = 0
    try:
        while True:
            line = input()
            count = count + 1
            print ('Linea: [{0}]').format(line)
    except EOFError:
        pass
    
    print ('leidas {0} lineas').format(count)

