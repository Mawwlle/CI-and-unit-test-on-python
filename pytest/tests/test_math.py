import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 4, 0), (1, 2, 2), (3, 3, 9)]
)
def test_mul(a, b, expected):
    assert a * b == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        example = 1 / 0

@pytest.mark.parametrize(
    "a,b",
    [("test", 4), (1.2, "3"), ((1, 2), 9.)]
)
def test_type_errors(a, b):
    with pytest.raises(TypeError):
        example = a / b
        example = a + b