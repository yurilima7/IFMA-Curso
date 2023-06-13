def mim(i, j, known):
    if known[i][j]:
        return known[i][j]
    
    known[i][j] = True
    
    for k in range(1, j+1):
        if not recwin(i - k, min(2*k, i - k), known):
            known[i][j] = True
            return True
    
    known[i][j] = False
    return False

def recwin(i, j, known):
    for k in range(1, j+1):
        if not recwin(i - k, min(2*k, i - k), known):
            return k
    
    return 0

n = 10  # Número total de fósforos
known = [[False] * (n+1) for _ in range(n+1)]  # Matriz de posições conhecidas

# Exemplo de uso:
i = 6 # 5 e 3 são perdedoras
j = 4
result = mim(i, j, known)
if result:
    print(f"A posição ({i}, {j}) é uma posição vencedora.")
else:
    print(f"A posição ({i}, {j}) é uma posição perdedora.")
