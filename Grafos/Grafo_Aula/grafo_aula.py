from Biblioteca.Grafo import GrafoListaAdj
import networkx as nx
import matplotlib.pyplot as plt

G = GrafoListaAdj()

G.DefinirN(4)

e = G.AdicionarAresta(1, 2)
e.custo = 3
e = G.AdicionarAresta(1, 3)
e.custo = 1
e = G.AdicionarAresta(1, 4)
e.custo = 2
e = G.AdicionarAresta(2, 3)
e.custo = 4

Gnx = nx.Graph()

for v in G.V():
    Gnx.add_node(v)

for v in G.V():
    for no in G.N(v, IterarSobreNo = True):
        u = no.Viz
        print((v, u), no.e.custo)
        Gnx.add_edge(v, u, weight = no.e.custo)

pos = nx.circular_layout(Gnx)
labels = nx.get_edge_attributes(Gnx, 'weight')

nx.draw_networkx_edge_labels(Gnx, pos, edge_labels = labels)
nx.draw_networkx(Gnx, pos, with_labels = True)
plt.show()
