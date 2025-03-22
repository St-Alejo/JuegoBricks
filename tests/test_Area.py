import pytest
from src.area import area_cuadrado

def test_area_cuadrado():
    assert area_cuadrado(4) == 16
    assert area_cuadrado(0) == 0
    assert area_cuadrado(5) == 25
