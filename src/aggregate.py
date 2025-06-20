from collections.abc import Callable

from src.exceptions import LogicError

TAggregateFunc = Callable[[list[float]], float]
"""Принимает список float, возвращает float"""

AGGREGATION_FUNCTIONS: dict[str, TAggregateFunc] = {
    "avg": lambda values: round(sum(values) / len(values), 2),  # округление для примера с картинки ТЗ
    "min": min,
    "max": max,
}


def apply_aggregation(rows: list[dict[str, str]], condition: str, column: str) -> list[dict[str, str]]:
    values = [float(row[column]) for row in rows]

    if condition not in AGGREGATION_FUNCTIONS:
        raise LogicError(f"Неподдерживаемая операция '{condition}'")

    result = AGGREGATION_FUNCTIONS[condition](values)

    # NB: возвращаем список словарей
    return [{condition: str(result)}]
