import pytest
from src.validar_email import validar_email

def test_email_valido():
    assert validar_email("correo@example.com") is True
    assert validar_email("usuario123@mail.co") is True

def test_email_invalido():
    assert validar_email("correo@.com") is False
    assert validar_email("usuario@com") is False
    assert validar_email("sin_arroba.com") is False
