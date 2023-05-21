# Classe que representa uma aresta do grafo
class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso

# Função que encontra a AGM usando o algoritmo de Kruskal
def kruskal(graph):
    # Função auxiliar para encontrar o pai de um vértice
    def encontrar_pai(pais, i):
        if pais[i] == i:
            return i
        return encontrar_pai(pais, pais[i])
    

    num_vertices = len(graph)
    agm = []  # Lista para armazenar as arestas da AGM
    pais = list(range(num_vertices))  # Lista para armazenar o pai de cada vértice

    # Ordena as arestas em ordem crescente de peso
    arestas = sorted(graph, key=lambda aresta: aresta.peso)

    for aresta in arestas:
        pai_origem = encontrar_pai(pais, aresta.origem)
        pai_destino = encontrar_pai(pais, aresta.destino)
        
        # Se a inclusão da aresta não forma ciclo, adiciona à AGM
        if pai_origem != pai_destino:
            agm.append(aresta)
            pais[pai_origem] = pai_destino
    
    return agm

def agmKruskal(agm):
    print("AGM usando Kruskal:")
    for aresta in agm:
        print(aresta.origem, "->", aresta.destino, ":", aresta.peso)