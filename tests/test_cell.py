import pytest
from src.cell import Cell

def test_cell_initial_state():  # ✅ positivo
    cell = Cell()
    assert not cell.is_mine
    assert not cell.is_revealed
    assert not cell.is_flagged

def test_place_mine():  # ✅ positivo
    cell = Cell()
    cell.place_mine()
    assert cell.is_mine

def test_reveal_empty_cell():  # ✅ positivo
    cell = Cell()
    assert cell.reveal() is False
    assert cell.is_revealed

def test_toggle_flag():  # ✅ positivo
    cell = Cell()
    cell.toggle_flag()
    assert cell.is_flagged
    cell.toggle_flag()
    assert not cell.is_flagged

def test_reveal_flagged_cell():  # ✅ negativo
    cell = Cell()
    cell.toggle_flag()
    result = cell.reveal()
    assert result is False
    assert not cell.is_revealed  # não deveria revelar

def test_toggle_flag_on_revealed_cell():  # ❌ negativo
    cell = Cell()
    cell.reveal()
    cell.toggle_flag()
    assert not cell.is_flagged  # flag não pode ser ativada em célula revelada

def test_double_reveal_cell():  # ❌ negativo
    cell = Cell()
    cell.reveal()
    already_revealed = cell.reveal()
    assert already_revealed is False  # não deve explodir nem alterar estado