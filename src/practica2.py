from os import remove


def cuenta_grado(grafo_lista):
    vertices = grafo_lista[0]
    caminos = grafo_lista[1]
    grados = [0] * len(vertices)

    for i, vertice in enumerate(vertices):
        for camino in caminos:
            if vertice == camino[0] or vertice == camino[1]:
                grados[i] += 1

    resultado = {vertice: grados[i] for i, vertice in enumerate(vertices)}

    return resultado
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    pass


def vertice_aislado(grafo_lista):
    vertices = grafo_lista[0]
    caminos = grafo_lista[1]
    aislados = vertices.copy()

    for vertice in vertices:
        for camino in caminos:
            if vertice == camino[0] or vertice == camino[1]:
                aislados.remove(vertice)
                break

    return aislados
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    pass

def componentes_conexas(grafo_lista):
        #[A,B] B C

        aristas = grafo_lista[1]
        if aristas == []:
            return []
        conexos = []
        for (x, y) in aristas:
            flag = 0  #flag para saber si esta en una lista conexa
            aux = [] 
            indice = -1
            indices = []
            for listaconexa in conexos:
                indice = indice + 1
                for elemento in listaconexa:
                    if x == elemento:
                        flag = 1
                        flag1 = 0
                        for elemento2 in listaconexa:
                            if y == elemento2:
                                flag1 = 1
                                break
                        if flag1 == 0:
                            aux.append(listaconexa[:])
                            indices.append(indice)
                            listaconexa.append(y)
                    if y == elemento:
                        flag = 1
                        flag1 = 0
                        for elemento2 in listaconexa:
                            if x == elemento2:
                                flag1 = 1
                                break
                        if flag1 == 0:
                            aux.append(listaconexa[:])
                            indices.append(indice)
                            listaconexa.append(x)
            if flag == 0:
                conexos.append([x, y])
            elif len(aux) == 2:
                conexos.pop(indices[1])
                conexos.pop(indices[0])
                conexos.append(aux[0] + aux[1])

        return conexos

def es_conexo(grafo_lista):
    return len(componentes_conexas(grafo_lista)) == 1
        
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    pass
