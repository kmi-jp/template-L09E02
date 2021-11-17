import pytest
from typing  import Iterator

from passwords import password_generator


@pytest.mark.parametrize(
    "length, count",
    [
        (5, 8936928),
        (4, 677040)
    ],
)
def test_rows_even_numbers(length, count):
    iterator = password_generator(length)
    assert isinstance(iterator, Iterator)
    assert len(list(iterator)) == count


def test_docstring():
    assert password_generator.__doc__
