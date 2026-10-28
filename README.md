**ФИО:** Гончарова Екатерина Ивановна
**Группа:** 221141
**Вариант:** 9  
**Лабораторная:** №8

## Задания и файлы

| Задание | Файл / Папка | Описание |
|---------|--------------|----------|
| Среднее 1 (9) | temperature.py | Класс с property |
| Среднее 2 (1) | pyproject.toml | Установка Poetry и создание проекта |
| Среднее 3 (6) | .flake8 | Настройка flake8 |
| Повышенное 1 (9) | pyproject.toml | Сборка пакета (`poetry build`) |
| Повышенное 2 (2) | .github/workflows/ci.yml | GitHub Actions (pytest + flake8) |

## Запуск

```bash
pip install poetry
poetry install
pytest
flake8 .
```