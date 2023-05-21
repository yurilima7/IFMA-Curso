from graph_class import criar_grafo_mochila, mochila_gulosa, mochila


valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidade = 50

grafo = criar_grafo_mochila(valores, pesos)
itens_selecionados, valor_total = mochila_gulosa(grafo, capacidade)

mochila(itens_selecionados, valor_total)
