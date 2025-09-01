class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighboring_mines = 0

    def place_mine(self):
        self.is_mine = True

    def reveal(self):
        if not self.is_flagged:
            self.is_revealed = True
        return self.is_mine

    def toggle_flag(self):
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged
