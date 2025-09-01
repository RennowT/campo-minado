import pytest
from src.game import Game

def test_start_game_not_over():  # ✅ positivo
    game = Game(5, 5, 3)
    assert not game.is_over

def test_flag_cell():  # ✅ positivo
    game = Game(3, 3, 1)
    game.play_turn(0, 0, "flag")
    assert game.board.grid[0][0].is_flagged

def test_win_condition():  # ✅ positivo
    game = Game(2, 2, 1)
    # Revela todas as células que não são minas
    for r in range(2):
        for c in range(2):
            if not game.board.grid[r][c].is_mine:
                game.play_turn(r, c, "reveal")
    assert game.is_won

def test_invalid_action():  # ❌ negativo
    game = Game(2, 2, 1)
    result = game.play_turn(0, 0, "dance")
    assert "Continua" in result  # ação inválida ignorada

def test_play_after_game_over():  # ❌ negativo
    game = Game(2, 2, 1)
    # Força derrota
    for r in range(2):
        for c in range(2):
            if game.board.grid[r][c].is_mine:
                game.play_turn(r, c, "reveal")
    result = game.play_turn(0, 0, "reveal")
    assert "Jogo já terminou" in result

def test_play_turn_out_of_bounds():  # ❌ negativo
    game = Game(3, 3, 1)
    with pytest.raises(IndexError):
        game.play_turn(10, 10, "reveal")

def test_play_with_invalid_type_inputs():  # ❌ negativo
    game = Game(3, 3, 1)
    with pytest.raises(TypeError):
        game.play_turn("linha", "coluna", "reveal")