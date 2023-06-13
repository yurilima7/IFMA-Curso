import networkx as nx

# Criando o grafo bipartido
G = nx.Graph()

# Adicionando os vértices ônibus
onibus = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(onibus, bipartite=0)

# Adicionando os vértices vagas
vagas = [1, 2, 3, 4, 5, 6]
G.add_nodes_from(vagas, bipartite=1)

# Adicionando as arestas
arestas = [
    ('A', 1), ('A', 2), ('A', 4), ('A', 5),
    ('B', 2), ('B', 3),
    ('C', 3),
    ('D', 2), ('D', 3),
    ('E', 4), ('E', 5), ('E', 6)
]
G.add_edges_from(arestas)

# Verificando se é possível encontrar um emparelhamento perfeito
if len(nx.bipartite.maximum_matching(G)) == len(onibus):
    print("É possível estacionar os cinco ônibus simultaneamente nas seis vagas disponíveis.")
else:
    print("Não é possível estacionar os cinco ônibus simultaneamente nas seis vagas disponíveis.")
