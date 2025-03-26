import pytest
from src.encontrar_maximo import encontrar_maximo, encontrar_minimo, calcular_promedio

def test_encontrar_maximo():
    assert encontrar_maximo([3, 7, 2, 9]) == 9
    assert encontrar_maximo([-5, -1, -9]) == -1

def test_encontrar_minimo():
    assert encontrar_minimo([3, 7, 2, 9]) == 2
    assert encontrar_minimo([-5, -1, -9]) == -9

def test_calcular_promedio():
    assert calcular_promedio([10, 20, 30]) == 20
    assert calcular_promedio([4, 8, 6]) == 6

def test_lista_vacia():
    with pytest.raises(ValueError):
        encontrar_maximo([])
    with pytest.raises(ValueError):
        encontrar_minimo([])
    with pytest.raises(ValueError):
        calcular_promedio([])
