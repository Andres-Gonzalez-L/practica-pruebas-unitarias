import pytest
from validador import es_password_valida

def test_password_corta_devuelve_false():
    # Arrange
    password_corta = "abc"

    # Act
    resultado = es_password_valida(password_corta)

    # Assert
    assert resultado is False

def es_password_valida(password: str) -> bool:
    return len(password) >= 8

def test_password_sin_numero_devuelve_false():
    # Contraseña con 8+ caracteres pero sin números
    password_sin_num = "abcdefgh"

    resultado = es_password_valida(password_sin_num)

    assert resultado is False