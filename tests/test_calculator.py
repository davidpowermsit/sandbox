import pytest

from sandbox.calculator import calculate, parse_user_input


class TestParseUserInput:
    def test_extract_first_second_values_and_operator(self) -> None:
        expected_first = 10
        expected_second = 20
        expected_operator = "+"

        actual_first, actual_second, actual_operator = parse_user_input(
            f"{expected_first}{expected_operator}{expected_second}"
        )

        assert actual_first == expected_first
        assert actual_second == expected_second
        assert actual_operator == expected_operator

    def test_raise_error_for_unsupported_operator(self) -> None:
        expected_first = 10
        expected_second = 20
        expected_operator = ">"

        with pytest.raises(ValueError):
            _, _, _ = parse_user_input(f"{expected_first}{expected_operator}{expected_second}")

    @pytest.mark.parametrize(
        ("test_calc", "test_op"),
        [
            ("10+10", "+"),
            ("10-10", "-"),
            ("10*10", "*"),
            ("10/10", "/"),
            ("10~10", "~"),
        ],
    )
    def test_finds_all_supported_operators(self, test_calc: str, test_op: str) -> None:

        _, _, actual_operator = parse_user_input(test_calc)

        assert actual_operator == test_op


class TestCalculate:
    @pytest.mark.parametrize(
        ("test_calc", "expected_result"),
        [
            ((10, "+", 10), (20, None)),
            ((10, "-", 10), (0, None)),
            ((10, "*", 10), (100, None)),
            ((10, "/", 3), (3.33, None)),
            ((5, "~", 3), (1, 2)),
        ],
    )
    def test_all_supported_calculations(
        self, test_calc: tuple[int, str, int], expected_result: tuple[int, int | None]
    ) -> None:

        val1, op, val2 = test_calc
        expected_integer, expected_fractional = expected_result

        integer, fractional = calculate(val1, val2, op)

        assert integer == expected_integer
        assert fractional == expected_fractional
