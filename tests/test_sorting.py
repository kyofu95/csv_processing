import pytest
from src.exceptions import LogicError
from src.sorting import apply_sorting

sample = [
    {"name": "a", "value": "3.0"},
    {"name": "c", "value": "1.0"},
    {"name": "b", "value": "2.0"},
]


def test_apply_sorting_asc_success() -> None:
    rows = apply_sorting(sample, "name", "asc")

    assert isinstance(rows, list)
    assert len(rows) == len(sample)

    values = "".join([item["name"] for item in rows])
    assert values == "abc"


def test_apply_sorting_desc_success() -> None:
    rows = apply_sorting(sample, "name", "desc")

    assert isinstance(rows, list)
    assert len(rows) == len(sample)

    values = "".join([item["name"] for item in rows])
    assert values == "cba"


def test_apply_sorting_asc_numerical_success() -> None:
    rows = apply_sorting(sample, "value", "asc")

    assert isinstance(rows, list)
    assert len(rows) == len(sample)

    values = "".join([item["value"] for item in rows])
    assert values == "1.02.03.0"


def test_apply_sorting_desc_numerical_success() -> None:
    rows = apply_sorting(sample, "value", "desc")

    assert isinstance(rows, list)
    assert len(rows) == len(sample)

    values = "".join([item["value"] for item in rows])
    assert values == "3.02.01.0"


def test_apply_sorting_wrong_column() -> None:
    with pytest.raises(LogicError):
        apply_sorting(sample, "wrong_column_name", "desc")


def test_apply_sorting_wrong_sorting_func() -> None:
    with pytest.raises(LogicError):
        apply_sorting(sample, "value", "wrong_func")
