import random
from .cell import Cell

class Board:
    def __init__(self, rows: int, cols: int, mines: int):
        if rows <= 0 or cols <= 0:
            raise ValueError("Board dimensions must be positive.")
        if mines < 0 or mines >= rows * cols:
            raise ValueError("Invalid number of mines.")

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

    def _count_adjacent_mines(self, row: int, col: int) -> int:
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.grid[nr][nc].is_mine:
                        count += 1
        return count

    def reveal_cell(self, row: int, col: int) -> bool:
        cell = self.grid[row][col]

        # ❌ Se estiver marcada com bandeira, não revela
        if cell.is_flagged:
            return False

        if cell.reveal():  # retorna True se for mina
            return True

        if cell.neighboring_mines == 0:
            self._reveal_neighbors(row, col)

        return False

    def _reveal_neighbors(self, row: int, col: int):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbor = self.grid[nr][nc]

                    # ✅ ignora reveladas, minas e células com bandeira
                    if not neighbor.is_revealed and not neighbor.is_flagged and not neighbor.is_mine:
                        neighbor.reveal()
                        if neighbor.neighboring_mines == 0:
                            self._reveal_neighbors(nr, nc)
