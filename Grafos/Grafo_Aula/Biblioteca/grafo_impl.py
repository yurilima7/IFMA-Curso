class GrafoImpl(object):
    # classe com as funções em comum de ListasAdj e MatrizAdj
    def __init__(self, digrafo = False):
        self.n, self.m, self.digrafo = None, None, digrafo

    # função que define o número de vértices.
    def definirN(self, n):
        self.n, self.m = n, 0

    # retorna o lista de vértices do grafo
    def vertices(self):

        for i in range(1, self.n + 1):
            yield i
    
    # retorna a lista de arestas uv do grafo
    def arestas(self, iteraNo = False):
        # u é inteiro
        # v é inteiro se for MatrizAdj, caso contrário é GrafoListaAdj.NoAresta

        # percorrendo cada vértice existente no grafo
        for v in self.vertices():
            # N produz todos os vérices adj ao vértice v
            # Tipo caso seja digrafo é definido como "+" (aresta de saída) retornando somente os vértices que têm uma aresta saindo de v
            # Tipo não sendo digrafo é definido como qualquer, retornando os adj de v
            # Se iteraNo for verdadeiro, retorna o GrafoListaAdj.NoAresta para cada v
            for w in self.N(v, tipo = "+" if self.digrafo else "*", iteraNo = iteraNo):
                enumerar = True

                if not self.digrafo:
                    # armazena w.Viz se w == GrafoListaAdj.NoAresta
                    numVertice = w if isinstance(w, int) else w.viz
                    enumerar = v < numVertice

                if enumerar:
                    yield (v, w)

class GrafoListaAdj(GrafoImpl):
    # Nó da lista de adjacência
    class NoAresta(object):

        def __init__(self) :
            self.viz = None
            self.aresta = None
            self.proximo = None

    # Classe que representa uma aresta
    class Aresta(object):
        # v1, no1 = um vértice da aresta e seu nó, ex: v1 == no1.viz
        # v2, no2 = mesma definição

        def __init__(self):
            self.v1, self.no1 = None, None
            self.v2, self.no2 = None, None

    # função que define o número de vértices.
    def definirN(self, n, dupLigada = False):
        # se duplamente ligada (dupLigada = True) a lista de vizinhos, permite a remoção de arestas em tempo constante

        super(GrafoListaAdj, self).definirN(n)
        # lista de adjacências de cada nó
        self.L = [None] * (self.n + 1)
        
        # percorre cada nó e inicializa uma lista de adjacência para eles
        for i in range(1, self.n + 1):
            self.L[i] = GrafoListaAdj.NoAresta()

        self.dupLigada = dupLigada

    # funcão que adiciona arestas uv ao grafo
    def addAresta(self, u, v):
        def addLista(u, v, e, tipo):
            no = GrafoListaAdj.NoAresta()

            no.viz = v
            no.aresta = e 
            no.proximo = self.L[u].proximo
            self.L[u].proximo = no

            # atualização dos nós para manter a lista de adjacências apontando aos vértices próximo e anterior
            if self.dupLigada:
                self.L[u].proximo.anterior = self.L[u]

                if self.L[u].proximo.proximo != None:
                    self.L[u].proximo.proximo.anterior = self.L[u].proximo

            if self.digrafo:
                no.tipo = tipo

            return no
            
        e = GrafoListaAdj.Aresta()
        e.v1, e.v2 = u, v
        e.no1 = addLista(u, v, e, "+")
        e.no2 = addLista(v, u, e, "-")

        self.m = self.m + 1

        return e
    
    # função que remove a aresta uv do grafo
    def delAresta(self, uv):
        def delLista(no):
            no.anterior.proximo = no.proximo

            if no.proximo != None:
                no.proximo.anterior = no.anterior

        delLista(uv.no1)
        delLista(uv.no2)

    # verifica se uv é uma aresta
    def saoAdj(self, u, v):
        tipo = "+" if self.digrafo else "*"

        for w in self.N(u, tipo):
            if w == v:
                return True
            
        return False
    
    # retorna a lista de grafo.NoAresta
    def N(self, v, tipo = "*", fechada = False, iteraNo = False):
        # se fechada inclui v na lista
        # * lista todas as arestas incidentes em v, caso seja digrafo
        # + lista apenas as arestas de saída, ou entrada no caso de -

        if fechada:
            no = GrafoListaAdj.NoAresta()
            no.viz = v
            no.aresta = None
            no.proximo = None

            yield no if iteraNo else no.viz
        
        w = self.L[v].proximo

        while w != None:
            if tipo == "*" or w.tipo == tipo:
                yield w if iteraNo else w.viz

            w = w.proximo