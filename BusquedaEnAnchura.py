from collections import deque

def bfs(graph, start, objetivo):
    # Lista para almacenar los nodos visitados
    visited = set()
    # Deque para almacenar los nodos por visitar
    queue = deque([(start, [start])])

    # Mientras haya nodos por visitar en la cola
    while queue:
        # Sacamos el primer nodo de la cola
        node, path = queue.popleft()
        # Si el nodo no ha sido visitado
        if node not in visited:
            if node == objetivo:
                print("La pieza se encuentra en la posicion indicada", objetivo)
                print("Camino recorrido: ", path)
                return path
            # Lo marcamos como visitado
            visited.add(node)
            # Añadimos los vecinos no visitados del nodo a la cola
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    print("No se encuentra la poscion indicada")
    return None

# Ejemplo de un grafo representado como un diccionario de listas de adyacencia
graph = {
    'B': ['B1', 'B2'],
    'B1': ['B', 'B3', 'B4'],
    'B2': ['B', 'B5', 'B6'],
    'B3': ['B1', 'B7', 'B8'],
    'B4': ['B1', 'B9', 'B10'],
    'B5': ['B2', 'B11', 'B12'],
    'B6': ['B2', 'B13', 'B14'],
    'B7': ['B3', 'B15', 'B16'],
    'B8': ['B3', 'B17', 'B18'],
    'B9': ['B4', 'B19', 'B20'],
    'B10': ['B4', 'B21', 'B22'],
    'B11': ['B5', 'B23', 'B24'],
    'B12': ['B5', 'B25', 'B26'],
    'B13': ['B6', 'B27', 'B28'],
    'B14': ['B6', 'B29', 'B30'],
    'B15': ['B6'],
    'B16': ['B6'],
    'B17': ['B7'],
    'B18': ['B7'],
    'B19': ['B8'],
    'B20': ['B8'],
    'B21': ['B9'],
    'B22': ['B9'],
    'B23': ['B10'],
    'B24': ['B10'],
    'B25': ['B11'],
    'B26': ['B11'],
    'B27': ['B12'],
    'B28': ['B12'],
    'B29': ['B13'],
    'B30': ['B13'],

}

# Nodo de inicio para la búsqueda en anchura
start_node = 'B'

objective = 'B25'

# Ejecutamos el algoritmo BFS
bfs(graph, start_node, objective)
