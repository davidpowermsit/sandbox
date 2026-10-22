import pytest

from sandbox.calculator import find_operator


class TestFindOperator:
    def test_extract_first_second_values_and_operator(self) -> None:
        expected_first = 10
        expected_second = 20
        expected_operator = "+"

        actual_first, actual_second, actual_operator = find_operator(
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
            _, _, _ = find_operator(f"{expected_first}{expected_operator}{expected_second}")

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

        _, _, actual_operator = find_operator(test_calc)

        assert actual_operator == test_op
