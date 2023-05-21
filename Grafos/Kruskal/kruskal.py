from graph_class import Aresta, agmKruskal, kruskal

# Grafo de exemplo
graph = [
    Aresta(0, 1, 4),
    Aresta(0, 2, 1),
    Aresta(1, 0, 4),
    Aresta(1, 3, 2),
    Aresta(2, 0, 1),
    Aresta(2, 3, 9),
    Aresta(2, 4, 5),
    Aresta(3, 1, 2),
    Aresta(3, 2, 9),
    Aresta(3, 4, 3),
    Aresta(4, 2, 5),
    Aresta(4, 3, 3)
]

# Teste do algoritmo de Kruskal
agm_kruskal = kruskal(graph)
agmKruskal(agm_kruskal)
