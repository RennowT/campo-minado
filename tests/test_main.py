from unittest.mock import patch
from src.main import main

def test_main_game_flow(capsys):
    # Simula entradas do usuário: reveal 0,0 e depois reveal 1,1
    user_inputs = ["reveal", "0", "0", "reveal", "1", "1"]
    with patch("builtins.input", side_effect=user_inputs):
        main()
    captured = capsys.readouterr()
    assert "Fim de jogo!" in captured.out