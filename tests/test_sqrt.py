"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---

def test_sqrt_raiz_de_cero():
    assert sqrt(0) == 0.0


def test_sqrt_raiz_no_cuadrado_perfecto():
    assert sqrt(2) == pytest.approx(1.41421356237)
    assert sqrt(3) == pytest.approx(1.73205080757)


# ---------------------------
# TEST PARAMETRIZADO
# ---------------------------

@pytest.mark.parametrize(
    "valor, esperado",
    [
        (0, 0.0),
        (1, 1.0),
        (4, 2.0),
        (2, pytest.approx(1.41421356237)),
        (3, pytest.approx(1.73205080757)),
    ],
)
def test_sqrt_parametrizado_varios_casos(valor, esperado):
    assert sqrt(valor) == esperado


# ---------------------------
# TESTS DE EXCEPCIONES
# ---------------------------

def test_sqrt_lanza_value_error_con_negativo():
    with pytest.raises(ValueError):
        sqrt(-1)


def test_sqrt_lanza_type_error_con_string():
    with pytest.raises(TypeError):
        sqrt("4")


def test_sqrt_lanza_type_error_con_none():
    with pytest.raises(TypeError):
        sqrt(None)

# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0)
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)
#   - Raíz de un número negativo → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_sqrt_negativo():
#     with pytest.raises(ValueError):
#         sqrt(-4)
