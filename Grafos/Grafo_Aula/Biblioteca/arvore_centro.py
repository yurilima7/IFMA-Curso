from Biblioteca.grafo_impl import GrafoListaAdj

def arvoreCentro(T):
    # se existe somente um vértice este é o centro
    if T.n == 1:
        return [1]
    
    # lista de graus inicializada em 0
    lg = [0] * (T.n + 1)

    # inicializando quantidade de vértices na árvore
    qtdVertice = T.n

    # calculando o grau de cada vértice da árvore
    for (u, v) in T.arestas():
        lg[u] += 1
        lg[v] += 1

    # lista com todos os vértices de grau 1 (folhas)
    F = [v for v in T.vertices() if lg[v] == 1]

    while qtdVertice > 2:
        Flin = []

        # selecionando todas as folhas
        for f in F:
            # obtendo o nó que contém a conexão
            vNo = next(T.N(f, iteraNo = True))

            v = vNo.viz

            # removendo e atualizando o grau do vértice pai
            lg[v] -= 1
            qtdVertice -= 1
            T.delAresta(vNo.aresta)

            # se grau = 1, é adicionado a nova lista de folha
            if lg[v] == 1:
                Flin.append(v)

        # atualiza a lista com todos os vértices de grau 1 (folhas)
        F = Flin

	# retorna as folhas (centro)
    return F 