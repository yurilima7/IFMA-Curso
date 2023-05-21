import sys
# Classe que representa uma aresta do grafo
class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso

# Função que encontra o vértice com a menor chave
def encontrar_min_chave(chaves, visitados):
    min_chave = sys.maxsize
    min_vertice = None
    
    for v in range(len(chaves)):
        if chaves[v] < min_chave and not visitados[v]:
            min_chave = chaves[v]
            min_vertice = v
    
    return min_vertice

# Função que encontra a AGM usando o algoritmo de Prim
def prim(graph):
    num_vertices = len(graph)
    chaves = [sys.maxsize] * num_vertices  # Chave para cada vértice
    pais = [None] * num_vertices  # Pai de cada vértice na AGM
    visitados = [False] * num_vertices  # Marca os vértices visitados
    
    # O primeiro vértice é escolhido como raiz
    chaves[0] = 0

    for _ in range(num_vertices):
        u = encontrar_min_chave(chaves, visitados)
        visitados[u] = True
        
        for aresta in graph[u]:
            v = aresta.destino
            peso = aresta.peso
            if not visitados[v] and peso < chaves[v]:
                chaves[v] = peso
                pais[v] = u
    
    agm = []  # Lista para armazenar as arestas da AGM
    
    for v in range(1, num_vertices):
        agm.append(Aresta(pais[v], v, chaves[v]))
    
    return agm

def agm(agm):
    print("AGM usando Prim:")
    for aresta in agm:
        print(aresta.origem, "->", aresta.destino, ":", aresta.peso)