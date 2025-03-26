import pytest
from src.conversor_monedas import convertir_a_pesos

def test_conversion_basica():
    assert convertir_a_pesos(10, 4000) == 40000
    assert convertir_a_pesos(5, 4500) == 22500

def test_conversion_negativa():
    with pytest.raises(ValueError):
        convertir_a_pesos(-3)
