import csv
import re


def read_csv(file_name: str) -> list[dict[str, str]]:
    with open(file_name, newline="") as f:
        return list(csv.DictReader(f))

def parse_arg(arg: str) -> tuple[str, str, str]:
    match = re.search(r"^([^=]*)([=><])(.*)", arg)
    if not match:
        raise ValueError()
    return (match.group(1), match.group(2), match.group(3))