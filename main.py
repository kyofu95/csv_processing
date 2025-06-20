import argparse

from src.aggregate import apply_aggregation
from src.filter import apply_filter
from src.sorting import apply_sorting
from src.utils import parse_arg, read_csv
from tabulate import tabulate


def main() -> None:
    parser = argparse.ArgumentParser(prog="CSV processor")

    parser.add_argument("--file", required=True)
    parser.add_argument("--where")
    parser.add_argument("--aggregate")
    parser.add_argument("--order-by", help="Сортировка")

    args = parser.parse_args()

    rows = read_csv(args.file)

    if args.where:
        column_name, op, reference_value = parse_arg(args.where)
        rows = apply_filter(rows, op, reference_value, column_name)

    if args.aggregate:
        column_name, _, condition = parse_arg(args.aggregate)
        rows = apply_aggregation(rows, condition, column_name)
    elif args.order_by:
        column_name, _, op = parse_arg(args.order_by)
        rows = apply_sorting(rows, column_name, op)

    print(tabulate(rows, headers="keys"))


if __name__ == "__main__":
    main()
