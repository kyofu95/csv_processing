from collections.abc import Callable

from src.exceptions import LogicError

TAggregateFunc = Callable[[list[float]], float]
"""Принимает список float, возвращает float"""

AGGREGATION_FUNCTIONS: dict[str, TAggregateFunc] = {
    "avg": lambda values: round(sum(values) / len(values), 2),  # округление для примера с картинки ТЗ
    "min": min,
    "max": max,
}


def apply_aggregation(rows: list[dict[str, str]], condition: str, column_name: str) -> list[dict[str, str]]:
    try:
        values = [float(row[column_name]) for row in rows]
    except ValueError as exc:
        # Если не можем кастануть, значит колонка неправильная
        msg = f"Колонка '{column_name}' не содержит численных данных"
        raise LogicError(msg) from exc

    if condition not in AGGREGATION_FUNCTIONS:
        raise LogicError(f"Неподдерживаемая операция '{condition}'")

    result = AGGREGATION_FUNCTIONS[condition](values)

    # NB: возвращаем список словарей
    return [{condition: str(result)}]
