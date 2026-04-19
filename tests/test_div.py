"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
def test_div_division_basica_enteros():
    assert div(6, 2) == 3


def test_div_division_resultado_decimal():
    assert div(5, 2) == 2.5
    assert div(1, 4) == 0.25


def test_div_division_con_numeros_negativos():
    assert div(-6, 2) == -3
    assert div(6, -2) == -3
    assert div(-6, -2) == 3


# ---------------------------
# TEST PARAMETRIZADO
# ---------------------------

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (6, 2, 3),
        (5, 2, 2.5),
        (1, 4, 0.25),
        (-6, 2, -3),
        (6, -2, -3),
        (-6, -2, 3),
    ],
)
def test_div_parametrizado_varios_casos(a, b, esperado):
    assert div(a, b) == esperado


# ---------------------------
# TESTS DE EXCEPCIONES
# ---------------------------

def test_div_lanza_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)


def test_div_lanza_type_error_con_string():
    with pytest.raises(TypeError):
        div("10", 2)


def test_div_lanza_type_error_con_none():
    with pytest.raises(TypeError):
        div(None, 2)

# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)
