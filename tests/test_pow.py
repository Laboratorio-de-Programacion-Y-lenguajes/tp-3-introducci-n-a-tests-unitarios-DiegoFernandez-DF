"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
def test_pow_numero_elevado_a_cero():
    assert pow_(5, 0) == 1
    assert pow_(10, 0) == 1


def test_pow_numero_elevado_a_uno():
    assert pow_(5, 1) == 5
    assert pow_(-3, 1) == -3


def test_pow_base_negativa_exponente_par():
    assert pow_(-2, 2) == 4
    assert pow_(-3, 4) == 81


def test_pow_exponente_decimal_raiz_cuadrada():
    assert pow_(9, 0.5) == 3.0
    assert pow_(16, 0.5) == 4.0


# ---------------------------
# TEST PARAMETRIZADO
# ---------------------------

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (5, 0, 1),
        (10, 0, 1),
        (5, 1, 5),
        (-3, 1, -3),
        (-2, 2, 4),
        (-3, 4, 81),
        (9, 0.5, 3.0),
        (16, 0.5, 4.0),
    ],
)
def test_pow_parametrizado_varios_casos(a, b, esperado):
    assert pow_(a, b) == esperado


# ---------------------------
# TESTS DE EXCEPCIONES
# ---------------------------

def test_pow_lanza_type_error_con_string():
    with pytest.raises(TypeError):
        pow_("2", 3)


def test_pow_lanza_type_error_con_none():
    with pytest.raises(TypeError):
        pow_(None, 2)

# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
