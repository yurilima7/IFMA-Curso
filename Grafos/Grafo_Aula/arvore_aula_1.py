from Biblioteca.Grafo import GrafoListaAdj
from Biblioteca.CentroArvore import CentroArvore
import networkx as nx
import matplotlib.pyplot as plt

G = GrafoListaAdj(orientado = False)

Gn1 = nx.Graph()

G.DefinirN(4, VizinhancaDuplamenteLigada = True)

e = G.AdicionarAresta(1, 2)
e = G.AdicionarAresta(1, 3)
e = G.AdicionarAresta(1, 4)

for v in G.V():
    Gn1.add_node(v)

for v in G.V():
    for no in G.N(v, IterarSobreNo = True):
        u = no.Viz
        Gn1.add_edge(v, u)

pos = nx.circular_layout(Gn1)
labels = nx.get_edge_attributes(Gn1, 'weight')

nx.draw_networkx_edge_labels(Gn1, pos, edge_labels = labels)
nx.draw_networkx(Gn1, pos, with_labels = True)

C = CentroArvore(G)
print("Centro = {}".format(C))

plt.show()