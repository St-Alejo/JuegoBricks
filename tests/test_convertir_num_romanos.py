import pytest
from src.convertir_num_romanos import romano_a_entero

def test_romano_a_entero():
    assert romano_a_entero("III") == 3
    assert romano_a_entero("IV") == 4
    assert romano_a_entero("IX") == 9
    assert romano_a_entero("XL") == 40
    assert romano_a_entero("MCMXCIV") == 1994
