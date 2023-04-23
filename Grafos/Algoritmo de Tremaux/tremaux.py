import class_tremaux

def main():
    # 0 é visitável e 1 representa uma parede
    maze = [
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
    ]

    solver = class_tremaux.MazeSolver(maze, 0, 0)

    solver.returnPathFound()

main()