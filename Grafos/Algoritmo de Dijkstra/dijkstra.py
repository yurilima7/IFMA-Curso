# Importando classe
from graph_class import Graph

# Utilizando o algoritmo
def main():
    graph = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [('A', 'B', 4), ('A', 'C', 2), ('B', 'E', 3), ('C', 'D', 2), 
             ('C', 'F', 4), ('D', 'E', 3), ('D', 'F', 1), ('E', 'F', 1)]
    
    start = vertices[0]

    # adicionando os vertices
    for vertice in vertices:
        graph.add_vertice(vertice)

    # adicionando as aresta ao dicionário
    for edge in edges:
        graph.add_edge(*edge)

    distances, ways = graph.dijkstra(start)

    # apresentando os caminhos e suas respectivas distâncias
    for vertice, distance in distances.items():
        way = [] # lista com os caminho do vértice atual
        vertice_current = vertice # vertice que será apresentado atualmente

        # laço responsável por buscar os caminhos do vértice atual
        while vertice_current != start:
            way.insert(0, vertice_current)
            vertice_current = ways[vertice_current]

        way.insert(0, start)
        print("O menor caminho de {} para {} é {} e tem distância {}".format(start, vertice, way, distance))

main()