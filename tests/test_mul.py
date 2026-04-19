"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_multiplicar_por_cero():
    assert mul(5, 0) == 0
    assert mul(0, 5) == 0


def test_mul_multiplicar_dos_numeros_negativos():
    assert mul(-2, -3) == 6


def test_mul_multiplicar_positivo_y_negativo():
    assert mul(5, -2) == -10
    assert mul(-2, 5) == -10


def test_mul_multiplicar_por_uno():
    assert mul(5, 1) == 5
    assert mul(1, 5) == 5


def test_mul_multiplicar_dos_decimales():
    assert mul(2.5, 2.0) == 5.0
    assert mul(-1.5, 2.0) == -3.0


# ---------------------------
# TEST PARAMETRIZADO
# ---------------------------

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (5, 0, 0),
        (0, 5, 0),
        (-2, -3, 6),
        (5, -2, -10),
        (1, 5, 5),
        (2.5, 2.0, 5.0),
    ],
)
def test_mul_parametrizado_varios_casos(a, b, esperado):
    assert mul(a, b) == esperado


# ---------------------------
# TESTS DE EXCEPCIONES
# ---------------------------

def test_mul_lanza_type_error_con_dos_strings():
    with pytest.raises(TypeError):
        mul("5", "2")


def test_mul_lanza_type_error_con_none():
    with pytest.raises(TypeError):
        mul(None, 2)

# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
