from Biblioteca.Grafo import GrafoListaAdj
from Biblioteca.CentroArvore import CentroArvore
import networkx as nx
import matplotlib.pyplot as plt

G2 = GrafoListaAdj(orientado = False)

Gn1 = nx.Graph()

G2.DefinirN(4, VizinhancaDuplamenteLigada = True)

e2 = G2.AdicionarAresta(3, 2)
e2 = G2.AdicionarAresta(1, 3)
e2 = G2.AdicionarAresta(1, 4)

for v in G2.V():
    Gn1.add_node(v)

for v in G2.V():
    for no in G2.N(v, IterarSobreNo = True):
        u = no.Viz
        Gn1.add_edge(v, u)

pos = nx.circular_layout(Gn1)
labels = nx.get_edge_attributes(Gn1, 'weight')

nx.draw_networkx_edge_labels(Gn1, pos, edge_labels = labels)
nx.draw_networkx(Gn1, pos, with_labels = True)

C2 = CentroArvore(G2)
print("Centro = {}".format(C2))

plt.show()