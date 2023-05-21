# Grafo de exemplo
from graph_class import Aresta, prim, agm

# Grafo de exemplo
graph = [
    [Aresta(0, 1, 4), Aresta(0, 2, 1)],              # Adjacências do vértice 0
    [Aresta(1, 0, 4), Aresta(1, 3, 2)],              # Adjacências do vértice 1
    [Aresta(2, 0, 1), Aresta(2, 3, 9), Aresta(2, 4, 5)],  # Adjacências do vértice 2
    [Aresta(3, 1, 2), Aresta(3, 2, 9), Aresta(3, 4, 3)],  # Adjacências do vértice 3
    [Aresta(4, 2, 5), Aresta(4, 3, 3)],              # Adjacências do vértice 4
]

# Teste do algoritmo de Prim
agm_prim = prim(graph)
agm(agm_prim)