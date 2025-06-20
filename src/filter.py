import operator
from collections.abc import Callable

from src.exceptions import LogicError
from src.utils import try_cast_to_float

TOperatorFunc = Callable[[float | str, float | str], float | str]
"""Принимает два аргумента типа str или float, возвращает str или float"""

FILTER_OPS: dict[str, TOperatorFunc] = {
    "=": operator.eq,
    ">": operator.gt,
    "<": operator.lt,
}


def apply_filter(
    rows: list[dict[str, str]], operation_filter: str, reference_value: str, column_name: str
) -> list[dict[str, str]]:
    op_func = FILTER_OPS.get(operation_filter)
    if not op_func:
        raise LogicError(f"Неправильный оператор '{operation_filter}'")

    try:
        # fmt: off
        return [
            row for row in rows
            if op_func(try_cast_to_float(row[column_name]), try_cast_to_float(reference_value))
        ]
        # fmt: on
    except KeyError as exc:
        raise LogicError(f"Колонка '{column_name}' не найдена в данных") from exc
    except TypeError as exc:
        # данная ошибка будет в результате сравнения str и float. либо ошибка в reference_value, либо в csv
        raise LogicError(f"Референсное значение {reference_value} неправильно задано, либо ошибка в данных") from exc
