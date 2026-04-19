"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
def test_add_suma_dos_numeros_negativos():
    assert add(-2, -3) == -5


def test_add_suma_numero_positivo_y_negativo():
    assert add(5, -2) == 3
    assert add(-2, 5) == 3


def test_add_suma_con_cero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0


def test_add_suma_dos_decimales():
    assert add(2.5, 3.5) == 6.0
    assert add(-1.5, 1.0) == -0.5


# ---------------------------
# TEST PARAMETRIZADO
# ---------------------------

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (-2, -3, -5),
        (-2, 5, 3),
        (0, 5, 5),
        (2.5, 3.5, 6.0),
    ],
)
def test_add_parametrizado_varios_casos(a, b, esperado):
    assert add(a, b) == esperado


# ---------------------------
# TESTS DE EXCEPCIONES
# ---------------------------

def test_add_lanza_type_error_con_string_y_entero():
    with pytest.raises(TypeError):
        add("2", 3)


def test_add_lanza_type_error_con_none():
    with pytest.raises(TypeError):
        add(None, 3)

# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected
