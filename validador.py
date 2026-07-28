def es_password_valida(password: str) -> bool:

    tiene_longitud = len(password) >= 8

    tiene_numero = any(caracter.isdigit() for caracter in password)

    return tiene_longitud and tiene_numero