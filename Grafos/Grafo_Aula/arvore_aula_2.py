from Biblioteca.grafo_impl import GrafoListaAdj
from Biblioteca.arvore_centro import arvoreCentro
import networkx as nx
import matplotlib.pyplot as plt

G2 = GrafoListaAdj(digrafo = False)

Gn1 = nx.Graph()

G2.definirN(4, dupLigada = True)

e2 = G2.addAresta(3, 2)
e2 = G2.addAresta(1, 3)
e2 = G2.addAresta(1, 4)

# removendo aresta (1, 2)

for v in G2.vertices():
    Gn1.add_node(v)

for v in G2.vertices():
    for no in G2.N(v, iteraNo = True):
        u = no.viz
        Gn1.add_edge(v, u)

pos = nx.circular_layout(Gn1)
labels = nx.get_edge_attributes(Gn1, 'weight')

nx.draw_networkx_edge_labels(Gn1, pos, edge_labels = labels)
nx.draw_networkx(Gn1, pos, with_labels = True)

C2 = arvoreCentro(G2)
print("Centro = {}".format(C2))

plt.show()