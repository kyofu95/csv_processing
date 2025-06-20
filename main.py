import argparse
from pathlib import Path

from src.aggregate import apply_aggregation
from src.exceptions import LogicError
from src.filter import apply_filter
from src.sorting import apply_sorting
from src.utils import parse_arg, read_csv
from tabulate import tabulate


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="CSV processor", description="CSV процессор, поддерживающий фильтрацию, агрегацию и сортировку"
    )

    parser.add_argument("--file", required=True, help="Имя csv файла")
    parser.add_argument("--where", help="Фильтрация строк по заданному значению")
    parser.add_argument("--aggregate", help="Агрегация по заданной функции")
    parser.add_argument("--order-by", help="Сортировка")

    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"Файл {args.file} не существует. Проверьте имя файла или путь к нему.")
        return

    rows = read_csv(args.file)

    try:
        if args.where:
            column_name, op, reference_value = parse_arg(args.where)
            rows = apply_filter(rows, op, reference_value, column_name)

        if args.aggregate:
            column_name, _, condition = parse_arg(args.aggregate)
            rows = apply_aggregation(rows, condition, column_name)
        elif args.order_by:
            column_name, _, op = parse_arg(args.order_by)
            rows = apply_sorting(rows, column_name, op)
    except LogicError as exc:
        print(str(exc))
        return

    print(tabulate(rows, headers="keys"))


if __name__ == "__main__":
    main()
