from unittest.mock import MagicMock, mock_open, patch

from src.utils import read_csv

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
