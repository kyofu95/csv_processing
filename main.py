import argparse

from src.utils import read_csv
from tabulate import tabulate


def main() -> None:
    parser = argparse.ArgumentParser(prog="CSV processor")

    parser.add_argument("--file", required=True)

    args = parser.parse_args()

    rows = read_csv(args.file)

    print(tabulate(rows, headers="keys"))


if __name__ == "__main__":
    main()
