"""Тесты для класса Temperature."""
import pytest
from temperature import Temperature


def test_default_celsius() -> None:
    """Проверяет значение по умолчанию."""
    t = Temperature()
    assert t.celsius == 0.0


def test_fahrenheit_conversion() -> None:
    """Проверяет конвертацию в Фаренгейт."""
    t = Temperature(100)
    assert t.fahrenheit == 212.0


def test_below_absolute_zero() -> None:
    """Проверяет выброс исключения при абсолютном нуле."""
    t = Temperature()
    with pytest.raises(ValueError):
        t.celsius = -300.0
