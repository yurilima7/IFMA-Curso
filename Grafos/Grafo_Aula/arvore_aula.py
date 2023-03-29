from Biblioteca.Grafo import GrafoListaAdj
from Biblioteca.CentroArvore import CentroArvore

G = GrafoListaAdj(orientado = False)
G2 = GrafoListaAdj(orientado = False)

G.DefinirN(4, VizinhancaDuplamenteLigada = True)
G2.DefinirN(4, VizinhancaDuplamenteLigada = True)

e = G.AdicionarAresta(1, 2)
e = G.AdicionarAresta(1, 3)
e = G.AdicionarAresta(1, 4)

e2 = G2.AdicionarAresta(3, 2)
e2 = G2.AdicionarAresta(1, 3)
e2 = G2.AdicionarAresta(1, 4)

C = CentroArvore(G)
C2 = CentroArvore(G2)

print(C)
print(C2)