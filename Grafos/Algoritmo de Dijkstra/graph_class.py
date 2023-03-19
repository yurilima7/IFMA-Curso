# disponibiliza estruturas de dados implementadas
import heapq

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertice(self, vertice):
        self.vertices.add(vertice)
        self.edges[vertice] = {}

    def add_edge(self, origin, destiny, weight):
        self.edges[origin][destiny] = weight
        self.edges[destiny][origin] = weight

    def dijkstra(self, origin):
        # criando um dicionário de distâncias com todas definidas como infinitas
        distances = {vertice: float('inf') for vertice in self.vertices}
        # criando um dicionário com os caminhos da origem até o vértice
        ways = {vertice: None for vertice in self.vertices}
        # atribuindo distância 0 para a origem
        distances[origin] = 0
        # heap armazena os vértices não visitados
        heap = [(0, origin)]

        # loop executado quando existem vértices não visitados
        while heap:
            # retira o vértice de menor distância da heap
            (dist_vertice, vertice_current) = heapq.heappop(heap)

            if dist_vertice > distances[vertice_current]:
                continue

            for vertice_neighbor, weight_edge in self.edges[vertice_current].items():
                dist_total = dist_vertice + weight_edge

                if dist_total < distances[vertice_neighbor]:
                    distances[vertice_neighbor] = dist_total
                    ways[vertice_neighbor] = vertice_current
                    heapq.heappush(heap, (dist_total, vertice_neighbor))
        
        return distances, ways