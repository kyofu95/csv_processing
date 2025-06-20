import pytest
from src.aggregate import apply_aggregation
from src.exceptions import LogicError

sample = [
    {"name": "a", "value": "1.0"},
    {"name": "b", "value": "2.0"},
]


@pytest.mark.parametrize("func_name, result", [("avg", "1.5"), ("min", "1.0"), ("max", "2.0")])
def test_apply_aggregation_func_success(func_name: str, result: str) -> None:
    rows = apply_aggregation(sample, func_name, "value")

    assert isinstance(rows, list)
    assert len(rows) == 1
    assert rows[0][func_name] == result


def test_apply_aggregation_wrong_func() -> None:
    with pytest.raises(LogicError):
        apply_aggregation(sample, "wrong_function_name", "value")
