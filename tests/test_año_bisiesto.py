import pytest
from src.año_bisiesto import es_bisiesto

def test_es_bisiesto():
    assert es_bisiesto(2020) == True
    assert es_bisiesto(1900) == False
    assert es_bisiesto(2000) == True
    assert es_bisiesto(2023) == False
    assert es_bisiesto(2024) == True
