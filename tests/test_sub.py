"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
def test_sub_resta_resultado_negativo():
    assert sub(2, 5) == -3


def test_sub_resta_con_cero():
    assert sub(5, 0) == 5
    assert sub(0, 5) == -5


def test_sub_resta_dos_numeros_negativos():
    assert sub(-5, -2) == -3


def test_sub_resta_dos_decimales():
    assert sub(5.5, 2.5) == 3.0
    assert sub(-1.5, -1.0) == -0.5


# ---------------------------
# TEST PARAMETRIZADO
# ---------------------------

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (5, 2, 3),
        (2, 5, -3),
        (5, 0, 5),
        (-5, -2, -3),
        (5.5, 2.5, 3.0),
    ],
)
def test_sub_parametrizado_varios_casos(a, b, esperado):
    assert sub(a, b) == esperado


# ---------------------------
# TESTS DE EXCEPCIONES
# ---------------------------

def test_sub_lanza_type_error_con_string_y_entero():
    with pytest.raises(TypeError):
        sub("5", 2)


def test_sub_lanza_type_error_con_none():
    with pytest.raises(TypeError):
        sub(None, 2)

# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
