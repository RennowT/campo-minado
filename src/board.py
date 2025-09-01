import random
from .cell import Cell

class Board:
    def __init__(self, rows: int, cols: int, mines: int):
        # Validações
        if rows <= 0 or cols <= 0:
            raise ValueError("Número de linhas e colunas deve ser positivo")
        if mines < 0:
            raise ValueError("Número de minas não pode ser negativo")
        if mines > rows * cols:
            raise ValueError("Número de minas não pode exceder número de células")

        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self._place_mines()
        self._calculate_neighbors()

    def _place_mines(self):
        positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in positions:
            r, c = divmod(pos, self.cols)
            self.grid[r][c].place_mine()

    def _calculate_neighbors(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.grid[r][c].is_mine:
                    self.grid[r][c].neighboring_mines = self._count_adjacent_mines(r, c)

    def _count_adjacent_mines(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.grid[nr][nc].is_mine:
                        count += 1
        return count

    def reveal_cell(self, row, col):
        cell = self.grid[row][col]
        if cell.reveal():
            return True  # Explodiu mina
        if cell.neighboring_mines == 0:
            self._reveal_neighbors(row, col)
        return False

    def _reveal_neighbors(self, row, col):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbor = self.grid[nr][nc]
                    if not neighbor.is_revealed and not neighbor.is_mine:
                        neighbor.reveal()
                        if neighbor.neighboring_mines == 0:
                            self._reveal_neighbors(nr, nc)

    def display(self):
        for r in range(self.rows):
            row_display = ""
            for c in range(self.cols):
                cell = self.grid[r][c]
                if cell.is_flagged:
                    row_display += " F "
                elif not cell.is_revealed:
                    row_display += " ? "
                elif cell.is_mine:
                    row_display += " * "
                else:
                    row_display += f" {cell.neighboring_mines} "
            print(row_display)
