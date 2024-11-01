import graph


def calcular_ruta_mas_corta(grafo, origen, destino):
    distancias = {estacion: float('inf') for estacion in grafo}
    distancias[origen] = 0
    predecesores = {}
    no_visitados = set(grafo.keys())

    while no_visitados:
        estacion_actual = min(
            (estacion for estacion in no_visitados),
            key=lambda estacion: distancias[estacion]
        )
        if distancias[estacion_actual] == float('inf'):
            break
        if estacion_actual == destino:
            break

        no_visitados.remove(estacion_actual)

        for vecino, peso in grafo[estacion_actual].items():
            distancia_total = distancias[estacion_actual] + peso
            if distancia_total < distancias.get(vecino, float('inf')):
                distancias[vecino] = distancia_total
                predecesores[vecino] = estacion_actual

    ruta = []
    estacion = destino
    while estacion != origen:
        ruta.insert(0, estacion)
        estacion = predecesores.get(estacion)
        if estacion is None:
            return None, float('inf')
    ruta.insert(0, origen)
    return ruta, distancias[destino]


if __name__ == "__main__":
    origen = 'Zapata-3'
    destino = 'La Paz'
    ruta, distancia_total = calcular_ruta_mas_corta(graph.metro_graph, origen, destino)
    print(f"La ruta más corta de {origen} a {destino} es:")
    print(" -> ".join(ruta))
    print(f"Distancia total: {distancia_total} metros")
