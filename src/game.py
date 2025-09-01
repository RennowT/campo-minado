from .board import Board

class Game:
    def __init__(self, rows=8, cols=8, mines=10):
        self.board = Board(rows, cols, mines)
        self.is_over = False
        self.is_won = False

    def play_turn(self, row, col, action="reveal"):
        if self.is_over:
            return "Jogo já terminou!"

        if action == "reveal":
            if self.board.reveal_cell(row, col):
                self.is_over = True
                return "💥 Você perdeu! Acertou uma mina!"
        elif action == "flag":
            self.board.grid[row][col].toggle_flag()

        if self._check_win():
            self.is_over = True
            self.is_won = True
            return "🎉 Você venceu!"

        return "Continua jogando..."

    def _check_win(self):
        for row in self.board.grid:
            for cell in row:
                if not cell.is_mine and not cell.is_revealed:
                    return False
        return True

    def show(self):
        self.board.display()
