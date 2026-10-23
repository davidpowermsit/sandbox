import datetime as dt

import pytest

from sandbox.scrapbook.scrapbook import all_or_nothing, average, grade_range, parse_timestamp, remove_ends, top_fruits


class TestTopFruits:
    def test_contains_ten_fruits(self) -> None:
        assert len(top_fruits) == 10

    def test_most_loved_is_first(self) -> None:
        assert top_fruits[0] == "apple"

    def test_least_loved_is_last(self) -> None:
        assert top_fruits[-1] == "lemon"


class TestAllOrNothing:
    def test_empty_list_returns_empty_list(self) -> None:
        assert all_or_nothing([]) == []

    def test_non_empty_list_is_doubled(self) -> None:
        assert all_or_nothing(["cat", "dog", "fish"]) == [
            "cat",
            "dog",
            "fish",
            "cat",
            "dog",
            "fish",
        ]

    def test_single_item_is_doubled(self) -> None:
        assert all_or_nothing(["cat"]) == ["cat", "cat"]


class TestRemoveEnds:
    def test_three_strings(self) -> None:
        assert remove_ends(["Jack", "Rose", "Cal"]) == ["Rose"]

    def test_five_ints(self) -> None:
        assert remove_ends([12, 50, 651, 64, 23]) == [50, 651, 64]

    def test_two_items_returns_empty_list(self) -> None:
        assert remove_ends([1, 2]) == []

    def test_does_not_mutate_input(self) -> None:
        original = [1, 2, 3, 4]
        remove_ends(original)
        assert original == [1, 2, 3, 4]


class TestGradeRange:
    @pytest.mark.parametrize(
        ("grades", "expected"),
        [
            ([85, 92, 70, 100, 64], 36),
            ([75, 75, 1, 100], 99),
            ([50, 50, 50], 0),
        ],
    )
    def test_range(self, grades: list[int], expected: int) -> None:
        assert grade_range(grades) == expected


class TestAverage:
    @pytest.mark.parametrize(
        ("grades", "expected"),
        [
            ([85, 92, 70, 100, 64], 82.2),
            ([75, 75, 1, 100], 62.75),
            ([50], 50.0),
        ],
    )
    def test_average(self, grades: list[int], expected: float) -> None:
        assert average(grades) == expected

    def test_rounds_to_two_decimals(self) -> None:
        assert average([1, 1, 2]) == 1.33

    def test_empty_list_raises(self) -> None:
        with pytest.raises(ZeroDivisionError):
            average([])


# test_scrapbook.py
class TestParseTimestamp:
    def test_parses_day_first_format(self) -> None:
        assert parse_timestamp("31/01/22 23:59:59.999999") == dt.datetime(2022, 1, 31, 23, 59, 59, 999999)

    def test_rejects_month_first_input(self) -> None:
        with pytest.raises(ValueError):
            parse_timestamp("01/31/22 23:59:59.999999")  # 31 can't be a month

    def test_rejects_missing_microseconds(self) -> None:
        with pytest.raises(ValueError):
            parse_timestamp("31/01/22 23:59:59")
