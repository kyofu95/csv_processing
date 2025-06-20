from enum import StrEnum

from src.exceptions import LogicError
from src.utils import try_cast_to_float


class SortingOperation(StrEnum):
    ASC = "asc"
    DESC = "desc"


def apply_sorting(rows: list[dict[str, str]], column_name: str, operation: str) -> list[dict[str, str]]:
    try:
        sort_operation = SortingOperation(operation.lower())
    except ValueError as exc:
        raise LogicError("Неправильный аргумент сортировки") from exc

    reverse = False
    if sort_operation == SortingOperation.DESC:
        reverse = True

    try:
        return sorted(rows, key=lambda row: try_cast_to_float(row[column_name]), reverse=reverse)
    except KeyError as exc:
        raise LogicError(f"Колонка '{column_name}' не найдена в данных") from exc
