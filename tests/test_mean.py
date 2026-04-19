"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
def test_mean_lista_un_solo_elemento():
    assert mean([5]) == 5
    assert mean([-3]) == -3


def test_mean_lista_numeros_negativos():
    assert mean([-2, -4, -6]) == -4


def test_mean_lista_numeros_decimales():
    assert mean([1.5, 2.5, 3.5]) == 2.5
    assert mean([0.1, 0.2, 0.3]) == pytest.approx(0.2)


# ---------------------------
# TEST PARAMETRIZADO
# ---------------------------

@pytest.mark.parametrize(
    "valores, esperado",
    [
        ([5], 5),
        ([-2, -4, -6], -4),
        ([1.5, 2.5, 3.5], 2.5),
        ([0.1, 0.2, 0.3], pytest.approx(0.2)),
    ],
)
def test_mean_parametrizado_varios_casos(valores, esperado):
    assert mean(valores) == esperado


# ---------------------------
# TESTS DE EXCEPCIONES
# ---------------------------

def test_mean_lanza_value_error_lista_vacia():
    with pytest.raises(ValueError):
        mean([])


def test_mean_lanza_type_error_con_elementos_invalidos():
    with pytest.raises(TypeError):
        mean([1, "2", 3])


def test_mean_lanza_value_error_con_none():
    with pytest.raises(ValueError):
        mean(None)

# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])
