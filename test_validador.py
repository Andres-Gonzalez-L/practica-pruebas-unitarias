import pytest
from validador import es_password_valida

def test_password_corta_devuelve_false():
    password_corta = "abc"
    resultado = es_password_valida(password_corta)
    assert resultado is False


def test_password_sin_numero_devuelve_false():
    password_sin_num = "abcdefgh"
    resultado = es_password_valida(password_sin_num)
    assert resultado is False

def test_password_sin_numero_devuelve_false():

    password_sin_num = "abcdefgh"

    resultado = es_password_valida(password_sin_num)

    assert resultado is False