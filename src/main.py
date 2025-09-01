from .game import Game

def main():
    game = Game(rows=5, cols=5, mines=5)

    while not game.is_over:
        game.show()
        action = input("Ação (reveal/flag): ")
        row = int(input("Linha: "))
        col = int(input("Coluna: "))
        msg = game.play_turn(row, col, action)
        print(msg)

    print("\nFim de jogo!")
    game.show()

if __name__ == "__main__":
    main()
