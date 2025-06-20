import pytest
from src.exceptions import LogicError
from src.filter import apply_filter

sample = [
    {"name": "a", "value": "1.0"},
    {"name": "b", "value": "2.0"},
    {"name": "c", "value": "3.0"},
    {"name": "d", "value": "4.0"},
]


def test_apply_filter_success() -> None:
    result_rows = apply_filter(sample, ">", "2.0", "value")
    assert len(result_rows) == 2
    assert result_rows[-1]["value"] == "4.0"


def test_apply_filter_all_success() -> None:
    result_rows = apply_filter(sample, ">", "4.0", "value")
    assert len(result_rows) == 0


def test_apply_filter_eq_success() -> None:
    result_rows = apply_filter(sample, ">", "4.0", "value")
    assert len(result_rows) == 0


def test_apply_filter_op_fail() -> None:
    with pytest.raises(LogicError):
        apply_filter(sample, "!", "1.0", "value")


def test_apply_filter_column_name_fail() -> None:
    with pytest.raises(LogicError):
        apply_filter(sample, "=", "1.0", "wrong_column_name")
