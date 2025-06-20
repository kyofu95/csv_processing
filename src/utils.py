import csv
import re
from pathlib import Path

from src.exceptions import LogicError


def read_csv(file_path: Path) -> list[dict[str, str]]:
    with open(file_path, newline="") as f:
        return list(csv.DictReader(f))


def parse_arg(arg: str) -> tuple[str, str, str]:
    match = re.search(r"^([^=]*)([=><])(.*)", arg)
    if not match:
        raise LogicError("Неправильное значение аргумента")
    return (match.group(1), match.group(2), match.group(3))


def try_cast_to_float(val: str) -> float | str:
    try:
        return float(val)
    except ValueError:
        return val