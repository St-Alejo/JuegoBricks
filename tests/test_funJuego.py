import pytest
from src.funJuego import iniciar_juego, mover_personaje, finalizar_juego

def test_iniciar_juego(capsys):
    iniciar_juego()
    captured = capsys.readouterr()
    assert captured.out.strip() == "¡Iniciando juego!!!"

def test_mover_personaje(capsys):
    mover_personaje("izquierda")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Moviendo personaje hacia izquierda"

def test_finalizar_juego(capsys):
    finalizar_juego()
    captured = capsys.readouterr()
    assert captured.out.strip() == "¡Fin del juego!!"
