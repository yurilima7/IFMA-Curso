from Biblioteca.grafo_impl import GrafoListaAdj
from Biblioteca.arvore_centro import arvoreCentro
import networkx as nx
import matplotlib.pyplot as plt

G = GrafoListaAdj(digrafo = False)

Gn1 = nx.Graph()

G.definirN(4, dupLigada = True)

e = G.addAresta(1, 2)
e = G.addAresta(1, 3)
e = G.addAresta(1, 4)

# removida a aresta (2, 3)

for v in G.vertices():
    Gn1.add_node(v)

for v in G.vertices():
    for no in G.N(v, iteraNo = True):
        u = no.viz
        Gn1.add_edge(v, u)

pos = nx.circular_layout(Gn1)
labels = nx.get_edge_attributes(Gn1, 'weight')

nx.draw_networkx_edge_labels(Gn1, pos, edge_labels = labels)
nx.draw_networkx(Gn1, pos, with_labels = True)

C = arvoreCentro(G)
print("Centro = {}".format(C))

plt.show()