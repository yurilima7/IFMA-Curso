from collections import defaultdict

def mochila_gulosa(grafo, capacidade):
    # Inicializa a mochila vazia e o valor total como 0
    itens_selecionados = []
    valor_total = 0
    capacidade_restante = capacidade

    # Ordena os vértices do grafo em ordem decrescente de valor-peso
    vertices_ordenados = sorted(grafo.keys(), key=lambda v: grafo[v]['valor_por_peso'], reverse=True)

    # Itera sobre os vértices e adiciona-os à mochila, desde que a capacidade permita
    for vertice in vertices_ordenados:
        peso = grafo[vertice]['peso']
        if capacidade_restante >= peso:
            itens_selecionados.append(vertice)
            valor_total += grafo[vertice]['valor']
            capacidade_restante -= peso

    return itens_selecionados, valor_total

def criar_grafo_mochila(valores, pesos):
    grafo = defaultdict(dict)
    num_itens = len(valores)
    for i in range(num_itens):
        vertice = 'Item{}'.format(i + 1)
        grafo[vertice]['valor'] = valores[i]
        grafo[vertice]['peso'] = pesos[i]
        grafo[vertice]['valor_por_peso'] = valores[i] / pesos[i]
    return grafo

def mochila(itens, valor_total):
    print("Itens selecionados:")
    for item in itens:
        print(item)

    print("Valor total:", valor_total)
