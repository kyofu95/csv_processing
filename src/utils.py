import csv


def read_csv(file_name: str) -> list[dict[str, str]]:
    with open(file_name, newline="") as f:
        return list(csv.DictReader(f))
