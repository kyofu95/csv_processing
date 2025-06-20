import argparse

from src.filter import apply_filter
from src.utils import parse_arg, read_csv
from tabulate import tabulate


def main() -> None:
    parser = argparse.ArgumentParser(prog="CSV processor")

    parser.add_argument("--file", required=True)
    parser.add_argument("--where")

    args = parser.parse_args()

    rows = read_csv(args.file)

    if args.where:
        column_name, op, reference_value = parse_arg(args.where)
        rows = apply_filter(rows, op, reference_value, column_name)

    print(tabulate(rows, headers="keys"))


if __name__ == "__main__":
    main()
