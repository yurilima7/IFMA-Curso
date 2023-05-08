def change(coins, k, value):
    minimum_coins = 0 # Quantidade minima de moedas para o troco
    amount_coins_used = [] # Vetor com a quantidade de moedas
    coins_used = [] # Vetor das moedas utilizadas

    # Percorre cada moeda
    for i in range(k):
        # Divide o troco pelo valor atual da moeda
        amount_coins_used.append(value // coins[i]) 

        # Adiciona a moeda no vetor caso seja utilizada
        if amount_coins_used[i] > 0 : coins_used.append(coins[i])

        # Decrementa o valor do troco
        value -= (amount_coins_used[i] * coins[i])
        # Incrementa a quantidade de moedas utilizadas
        minimum_coins += amount_coins_used[i]

    print("Quantidade de moedas usadas: {}" .format(minimum_coins))
    print("Moedas Utilizadas: {}" .format(coins_used))

coins = [200, 100, 50, 20, 10, 5, 2]
change(coins, len(coins), 2350)