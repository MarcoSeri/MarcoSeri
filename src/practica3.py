def valida_nodo_en_grafo(grafo_lista, nodo):
    nodos = grafo_lista[0]
    
    for elem in nodos:
        if nodo == elem:
            return True

    return False
    
    '''
    Dado un grafo en representacion de lista, y un nodo, me devuelve True si el nodo está en el Grafo
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
	'F'
    Ejemplo formato salida: 
        False
    '''
    
def encuentra_vecinos(grafo, vertice):
    _, aristas = grafo
    vecinos = set()
    for (v1, v2) in aristas:
        if v1 == vertice:
            vecinos.add(v2)
        if v2 == vertice:
            vecinos.add(v1)

    if vertice in vecinos:
        vecinos.remove(vertice)
    return list(vecinos)


def vertices_en_camino(camino):
    return set(camino)

def encuentra_camino(grafo_lista, nodo_ini, nodo_fin):
    '''
    Dado un grafo en representacion de lista, el nodo inicial y final de un camino
    Me devuelve una lista con los vértices del camino, o vacio si no existe
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
  a
  b
    Ejemplo retorno: 
        ['a','b','d','c','e','d','b']
    '''

    vecinos = encuentra_vecinos(grafo_lista, nodo_ini)
    caminos = [nodo_ini]
    caminos_anteriores = []
    while vertices_en_camino(caminos) != vertices_en_camino(caminos_anteriores):
        caminos_anteriores = caminos
        caminos = []

        for camino in caminos_anteriores:
            nodo_actual = camino[-1]
            if (nodo_actual == nodo_fin):
                return list(camino)
            vecinos = encuentra_vecinos(grafo_lista, nodo_actual)
            for vecino in vecinos:
                caminos.append(camino + vecino)

    return []

def encuentra_camino_cerrado(grafo_lista, nodo):
    vertices, aristas = grafo_lista

    for inicio, fin in aristas:
        if nodo == inicio:
            return [nodo,fin,nodo]
        elif nodo == fin:
            return [nodo,inicio,nodo]
            
    return []

    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	a
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    pass

def encuentra_recorrido(grafo_lista, nodo_ini, nodo_fin):
    vertices, aristas = grafo_lista
    for x,y in aristas:
        if nodo_ini == x:
            aristas.remove((x,y))
            return [nodo_ini] + encuentra_camino((vertices,aristas), y, nodo_fin)
        elif nodo_ini == y:
            aristas.remove((x,y))
            return [nodo_ini] + encuentra_camino((vertices,aristas), x, nodo_fin)

    return []
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	b
	f
    Ejemplo retorno: 
        ['b','c','d','e','c','f']
    '''
    pass

def encuentra_circuito(grafo_lista, nodo):
    vertices, aristas = grafo_lista
    for x,y in aristas:
        if nodo == x:
            aristas.remove((x,y))
            return [nodo] + encuentra_camino((vertices,aristas), y, x)
        elif nodo == y:
            aristas.remove((x,y))
            return [nodo] + encuentra_camino((vertices,aristas), x, y)

    return []
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['d','a','b','d','c','e','d']
    '''
    pass 	 	

def encuentra_camino_simple(grafo_lista, nodo_ini, nodo_fin):
    vertices, aristas = grafo_lista

    def dfs(actual, objetivo, visitados, camino):
        if actual == objetivo:
            return camino + [actual]
        visitados.add(actual)
        camino.append(actual)

        for inicio, fin in aristas:
            if inicio == actual and fin not in visitados:
                resultado = dfs(fin, objetivo, visitados, camino)
                if resultado:
                    return resultado
            elif fin == actual and inicio not in visitados:
                resultado = dfs(inicio, objetivo, visitados, camino)
                if resultado:
                    return resultado

        camino.pop()
        return []

    return dfs(nodo_ini, nodo_fin, set(), [])
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d']
    '''
    pass

def encuentra_ciclo(grafo_lista, nodo):
    vertices, aristas = grafo_lista

    def dfs(actual, visitados, camino):
        visitados.add(actual)
        camino.append(actual)
        for inicio, fin in aristas:
            if  len(camino) >= 3 and inicio == actual:
                return camino + [fin]
            if  len(camino) >= 3 and fin == actual:
                return camino + [inicio]
            if inicio == actual and fin not in visitados:
                resultado = dfs(fin, visitados, camino)
                if resultado:
                    return resultado
            elif fin == actual and inicio not in visitados:
                resultado = dfs(inicio, visitados, camino)
                if resultado:
                    return resultado

        camino.pop()
        return []

    return dfs(nodo, set(), [])
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    pass

def determina_caminos(camino_lista):
    repV = 0
    repA = 0
    terM = 0
    
    a = camino_lista[0:len(camino_lista)-1][:]
    b = camino_lista[1:len(camino_lista)][:]
    aristas = zip(a,b)
    aristas = list(aristas)

    #Si es abierto o cerrado
    if camino_lista[0] == camino_lista[len(camino_lista)-1]:
        terM = 1
        camino_lista.pop()

    #Si tiene aristas repetidas
    for x,y in aristas:
        repA1 = 0
        for a,b in aristas:
            if (x,y) == (a,b) or (x,y) == (b,a):
                repA1 += 1
            if repA1 > 1:
                repA = 1

    #Si tiene vertices repetidos
    for nodo in camino_lista:
        repV1 = 0
        for nodex in camino_lista:
            if nodo == nodex:
                repV1 += 1
            if repV1 > 1:
                repV = 1

    if repV == 1 and repA == 1 and terM == 0:
        print("Es un camino")
    elif repV == 1 and repA == 1 and terM == 1:
        print("Es un camino cerrado")
    elif repV == 1 and repA == 0 and terM == 0:
        print("Es un recorrido")
    elif repV == 1 and repA == 0 and terM == 1:
        print("Es un circuito")    
    elif repV == 0 and repA == 0 and terM == 0:
        print("Es un camino simple")
    elif repV == 0 and repA == 0 and terM == 1 and len(camino_lista) >= 3:
        print("Es un ciclo")
    '''
    Dado una lista que representa un camino, camino cerrado, recorrido, circuito, camino simple o ciclo,
    me devuelva de qué se trata
    Ejemplo Entrada: 
        ['d','a','b','d','c','e','d']
    Ejemplo formato salida: 
        Circuito
    '''
