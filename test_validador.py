import pytest
from validador import es_password_valida

def test_password_corta_devuelve_false():
    # Arrange
    password_corta = "abc"

    # Act
    resultado = es_password_valida(password_corta)

    # Assert
    assert resultado is False