from unittest.mock import MagicMock, mock_open, patch

import pytest
from src.utils import parse_arg, read_csv

std = """
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
"""


@patch("builtins.open", new_callable=mock_open, read_data=std)
def test_read_csv_success(mock_file: MagicMock) -> None:
    filename = "test.csv"

    rows = read_csv(filename)

    mock_file.assert_called_with(filename, newline="")

    assert len(rows) == 3


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_csv_empty(mock_file: MagicMock) -> None:
    filename = "test.csv"

    rows = read_csv(filename)

    mock_file.assert_called_with(filename, newline="")

    assert len(rows) == 0


@patch("builtins.open", new_callable=mock_open, read_data="name,brand,price,rating")
def test_read_csv_only_headers(mock_file: MagicMock) -> None:
    filename = "test.csv"

    rows = read_csv(filename)

    mock_file.assert_called_with(filename, newline="")

    assert len(rows) == 0


def test_parse_args_success() -> None:
    test_arg = "key=value"

    a, op, b = parse_arg(test_arg)

    assert a == "key"
    assert b == "value"
    assert op == "="


@pytest.mark.parametrize("arg", [("key=value"), ("key>value"), ("key<value")])
def test_parse_args_ops_success(arg: str) -> None:
    _, op, _ = parse_arg(arg)

    assert op in "=><"


def test_parse_args_ops_failure() -> None:
    with pytest.raises(ValueError):
        parse_arg("key_value")


def test_parse_args_failure() -> None:
    test_arg = "keyvalue"

    with pytest.raises(ValueError):
        parse_arg(test_arg)
