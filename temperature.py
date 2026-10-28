"""Модуль с классом Temperature, использующим property."""


class Temperature:
    """Класс для работы с температурой."""

    def __init__(self, celsius: float = 0.0) -> None:
        """Инициализирует температуру по Цельсию."""
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        """Возвращает температуру в градусах Цельсия."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Устанавливает температуру с проверкой на абсолютный ноль."""
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Вычисляет температуру по Фаренгейту на основе Цельсия."""
        return self._celsius * 9 / 5 + 32


if __name__ == "__main__":
    t = Temperature(25)
    print(f"{t.celsius}°C = {t.fahrenheit}°F")
