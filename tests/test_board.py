import pytest
from src.board import Board

def test_board_creation():  # ✅ positivo
    board = Board(5, 5, 5)
    assert len(board.grid) == 5
    assert len(board.grid[0]) == 5

def test_mine_count():  # ✅ positivo
    board = Board(4, 4, 4)
    mines = sum(cell.is_mine for row in board.grid for cell in row)
    assert mines == 4

def test_neighboring_mines_calculation():  # ✅ positivo
    board = Board(3, 3, 0)
    board.grid[1][1].place_mine()
    board._calculate_neighbors()
    assert board.grid[0][0].neighboring_mines == 1

def test_reveal_mine_returns_true():  # ✅ positivo
    board = Board(2, 2, 1)
    for r in range(2):
        for c in range(2):
            if board.grid[r][c].is_mine:
                assert board.reveal_cell(r, c) is True

def test_reveal_safe_cell_returns_false():  # ✅ positivo
    board = Board(2, 2, 1)
    for r in range(2):
        for c in range(2):
            if not board.grid[r][c].is_mine:
                assert board.reveal_cell(r, c) is False

def test_reveal_neighbors_propagates():  # ✅ positivo
    board = Board(3, 3, 0)
    board.reveal_cell(1, 1)
    revealed = sum(cell.is_revealed for row in board.grid for cell in row)
    assert revealed == 9

def test_invalid_reveal_out_of_bounds():  # ❌ negativo
    board = Board(3, 3, 0)
    with pytest.raises(IndexError):
        board.reveal_cell(5, 5)

def test_negative_board_size():  # ❌ negativo
    with pytest.raises(ValueError):
        Board(-3, -3, 1)

def test_more_mines_than_cells():  # ❌ negativo
    with pytest.raises(ValueError):
        Board(2, 2, 10)

def test_reveal_flagged_cell_does_not_explode():  # ❌ negativo
    board = Board(3, 3, 1)
    board.grid[0][0].toggle_flag()
    result = board.reveal_cell(0, 0)
    assert result is False  # não deve revelar mina nem explodir
    assert not board.grid[0][0].is_revealed
