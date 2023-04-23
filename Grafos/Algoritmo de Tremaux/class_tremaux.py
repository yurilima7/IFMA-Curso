class MazeSolver:
    def __init__(self, maze, initialX, initialY):
        # Matriz de 0s e 1s que representa um labirinto
        self.maze = maze
        # Variável responsável pelo armazenamento da largura do labirinto
        self.width = len(maze[0])
        # Variável responsável pelo armazenamento da altura do labirinto
        self.height = len(maze)
        # Matriz que armazena as coordenadas visitadas (células) inicializado em 0
        self.visited = [[0] * self.width for i in range(self.height)]
        # Lista que armazena o caminho encontrado
        self.pathFound = []
        # Chamada do método solve com as coordenadas iniciais em (0, 0)
        self.solve(initialX, initialY)

    def returnPathFound(self):
        # revertendo a lista
        self.pathFound.reverse()

        # Caso a lista esteja vazia não existe um caminho
        if not self.pathFound:
            return print('Não existe um caminho válido para saída')
        
        print("Caminho para saída do labirinto: ", end = " ")
        for i in self.pathFound:
            print('-> {}'.format(i), end = " ")

    def solve(self, x, y):
        # Verificando se as coordenadas atuais representam a saída do labirinto
        if x == self.width - 1 and y == self.height - 1:
            # Adiciona as coordenadas de saída na lista
            self.pathFound.append((y, x))
            return True
        
        # Retorna false no caso dessas coordenadas já tiverem sido visitadas
        if self.visited[y][x]:
            return False
        
        # Caso contrário é feita a marcação de visitada
        self.visited[y][x] = 1

        # Verificando se cada coordenada vizinha pode ser visitada
        # Parede esquerda
        if x != 0 and not self.maze[y][x - 1]:
            if self.solve(x - 1, y):
                # se o retorno da chamada recusiva for true, adicionando caminho na lista
                self.pathFound.append((y, x))
                return True
            
        # Parede direita  
        if x != self.width - 1 and not self.maze[y][x + 1]:
            if self.solve(x + 1, y):
                self.pathFound.append((y, x))
                return True

        # Parede superior    
        if y != 0 and not self.maze[y - 1][x]:
            if self.solve(x, y - 1):
                self.pathFound.append((y, x))
                return True

        # Parede inferior   
        if y != self.height - 1 and not self.maze[y + 1][x]:
            if self.solve(x, y +1 ):
                self.pathFound.append((y, x))
                return True
        
        # Se nenhuma vizinha pode ser visitada o retorno é false
        return False