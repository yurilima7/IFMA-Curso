import networkx as nx

# Criar o grafo bipartido
grafo = nx.Graph()

# Adicionar os casais e os quartos como vértices
casais = ['A', 'B', 'C', 'D', 'E', 'F']
quartos = [1, 2, 3, 4, 5, 6]
grafo.add_nodes_from(casais, bipartite=0)
grafo.add_nodes_from(quartos, bipartite=1)

# Adicionar as arestas de acordo com as preferências
preferencias = {
    'A': [1, 2, 4],
    'B': [2, 6],
    'C': [2, 3],
    'D': [3, 5, 6],
    'E': [3, 4, 5, 6],
    'F': [2, 5]
}

for casal, quartos_pref in preferencias.items():
    for quarto in quartos_pref:
        grafo.add_edge(casal, quarto)

# Encontrar o emparelhamento máximo
emparelhamento = nx.bipartite.maximum_matching(grafo)

# Contar o número de pares de casais e quartos compatíveis
num_pares = len(emparelhamento) // 2

print("Número máximo:", num_pares // 2)
