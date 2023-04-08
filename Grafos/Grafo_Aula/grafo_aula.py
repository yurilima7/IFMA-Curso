from Biblioteca.grafo_impl import GrafoListaAdj
import networkx as nx
import matplotlib.pyplot as plt

G = GrafoListaAdj()

G.definirN(4)

e = G.addAresta(1, 2)
e.custo = 3
e = G.addAresta(1, 3)
e.custo = 1
e = G.addAresta(1, 4)
e.custo = 2
e = G.addAresta(2, 3)
e.custo = 4

Gnx = nx.Graph()

for v in G.vertices():
    Gnx.add_node(v)

for v in G.vertices():
    for no in G.N(v, iteraNo = True):
        u = no.viz
        print((v, u), no.aresta.custo)
        Gnx.add_edge(v, u, weight = no.aresta.custo) # add pesos

pos = nx.circular_layout(Gnx) # pos dos nós
labels = nx.get_edge_attributes(Gnx, 'weight') # add as etiquetas de peso

nx.draw_networkx_edge_labels(Gnx, pos, edge_labels = labels) # desenha as etiquetas
nx.draw_networkx(Gnx, pos, with_labels = True) # desenha o gráfo
plt.show()
