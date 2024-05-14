from queue import PriorityQueue

def best_first_search(graph, start, goal):
    # Creamos una cola de prioridad para almacenar los nodos a explorar
    frontier = PriorityQueue()
    # Agregamos el nodo inicial a la cola de prioridad con una prioridad de 0
    frontier.put((0, start))
    # Diccionario para almacenar el costo acumulado hasta cada nodo
    cost_so_far = {start: 0}
    # Diccionario para almacenar el nodo padre de cada nodo
    came_from = {start: None}

    # Mientras haya nodos por explorar en la cola de prioridad
    while not frontier.empty():
        # Obtenemos el nodo con la menor prioridad de la cola (el que tiene menor costo acumulado)
        current_cost, current_node = frontier.get()

        # Si llegamos al nodo objetivo, reconstruimos y devolvemos el camino
        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            return path
        #
        # Exploramos los nodos vecinos del nodo actual
        for next_node, cost in graph[current_node].items():
            new_cost = current_cost + cost
            # Si el nodo vecino no ha sido explorado o encontramos un camino más corto
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                frontier.put((priority, next_node))
                came_from[next_node] = current_node

    # Si no se encuentra un camino al objetivo
    return None

# Ejemplo de un grafo representado como un diccionario de diccionarios de adyacencia con costos
graph = {
    'B': {'B1': 3, 'B2': 5},
    'B1': {'B3': 4, 'B4': 7},
    'B2': {'B5': 8, 'B6': 2},
    'B3': {'B7': 1, 'B8': 6},
    'B4': {'B9': 3, 'B10': 8},
    'B5': {'B11': 1, 'B12': 9},
    'B6': {'B13': 13, 'B14': 15},
    'B7': {'B15': 5, 'B16': 2},
    'B8': {'B17': 9, 'B18': 6},
    'B9': {'B19': 12, 'B20': 16},
    'B10': {'B21': 6, 'B22': 2},
    'B11': {'B23': 7, 'B24': 9},
    'B12': {'B25': 8, 'B26': 3},
    'B13': {'B27': 3, 'B28': 5},
    'B14': {'B29': 10, 'B30': 9},
    'B15': {'B6': 4},
    'B16': {'B6': 1},
    'B17': {'B7': 3},
    'B18': {'B7': 4},
    'B19': {'B8': 6},
    'B20': {'B8': 9},
    'B21': {'B9': 3},
    'B22': {'B9': 2},
    'B23': {'B10': 5},
    'B24': {'B10': 6},
    'B25': {'B11': 3},
    'B26': {'B11': 4},
    'B27': {'B12': 7},
    'B28': {'B12': 9},
    'B29': {'B13': 3},
    'B30': {'B13': 1},

}

# Nodo de inicio y nodo objetivo para la búsqueda primero el mejor
start_node = 'B'
goal_node = 'B18'

# Ejecutamos el algoritmo de búsqueda primero el mejor
path = best_first_search(graph, start_node, goal_node)
if path:
    print("El camino encontrado es:", path)
else:
    print("No se encontró un camino al objetivo.")
