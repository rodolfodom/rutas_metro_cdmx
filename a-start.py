import graph
import coordinates_tuple
import math
import heapq

def heuristic(current_node, target_node):

    R = 6371000

    lat1, lng1 = coordinates_tuple.coordinates_tuple[current_node]
    lat2, lng2 = coordinates_tuple.coordinates_tuple[target_node]

    lat1 = math.radians(lat1)
    lng1 = math.radians(lng1)
    lat2 = math.radians(lat2)
    lng2 = math.radians(lng2)

    dlat = lat2 - lat1
    dlng = lng2 - lng1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance


def a_star(current_node, target_node):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, current_node))
    g_score = {nodo: float("inf") for nodo in graph.metro_graph}
    g_score[current_node] = 0
    f_score = {nodo: float("inf") for nodo in graph.metro_graph}
    f_score[current_node] = heuristic(current_node, target_node)
    came_from = {}

    while cola_prioridad:

        _, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == target_node:
            return reconstruir_ruta(came_from, current_node, target_node)
        
        for vecino, distancia in graph.metro_graph[nodo_actual]:
            tentative_g_score = g_score[nodo_actual] + distancia

            if tentative_g_score < g_score[vecino]:
                # Actualiza el camino más corto conocido
                came_from[vecino] = nodo_actual
                g_score[vecino] = tentative_g_score
                f_score[vecino] = g_score[vecino] + heuristic(vecino, target_node)
                # Agregar a la cola de prioridad si no está ya en ella
                if (f_score[vecino], vecino) not in cola_prioridad:
                    heapq.heappush(cola_prioridad, (f_score[vecino], vecino))
    return None
        


def reconstruir_ruta(came_from, current_node, target_node):
    ruta = [target_node]
    while ruta[-1] != current_node:
        ruta.append(came_from[ruta[-1]])
    ruta.reverse()
    return ruta


if __name__ == "__main__":
    origen = 'San Lázaro-1'
    destino = 'Aragón'
    print(a_star(origen, destino))

