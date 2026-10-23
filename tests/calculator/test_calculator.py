import pytest

from sandbox.calculator.calculator import Result, calculate, main, parse_user_input


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

    # Example of how to use pytest.mark to mark behaviour that is missing
    # once implamented the test then fails and the mark can be removed
    # making the test a regular regression test
    #
    # pytest.param(
    #     "5*-3",
    #     (5, -3, "*"),
    #     id="negative_right_multiplication",
    #     marks=pytest.mark.xfail(strict=True, reason="parser matches '-' before '*'"),
    # ),

    @pytest.mark.parametrize(
        ("test_calc", "expected"),
        [
            pytest.param("-5+3", (-5, 3, "+"), id="negative_left_addition"),
            pytest.param("5+-3", (5, -3, "+"), id="negative_right_addition"),
            pytest.param("-5-3", (-5, 3, "-"), id="negative_left_subtraction"),
            pytest.param("5*-3", (5, -3, "*"), id="negative_right_multiplication"),
            pytest.param("-5*-3", (-5, -3, "*"), id="negative_left_and_negative_right_multiplication"),
            pytest.param("5--3", (5, -3, "-"), id="negative_right_subtraction"),
            pytest.param("-5--3", (-5, -3, "-"), id="negative_left_and_negative_right_subtraction"),
        ],
    )
    def test_handles_negative_operands(self, test_calc: str, expected: tuple[int, int, str]) -> None:
        assert parse_user_input(test_calc) == expected

    @pytest.mark.parametrize(
        ("test_input"),
        ["53", "-5"],
    )
    def test_raises_when_no_operator_found(self, test_input: str) -> None:
        with pytest.raises(ValueError, match="No operator found"):
            parse_user_input(test_input)

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
            pytest.param((10, "+", 10), (20, None), id="addition"),
            pytest.param((10, "-", 10), (0, None), id="subtraction"),
            pytest.param((10, "*", 10), (100, None), id="multiplication"),
            pytest.param((10, "/", 3), (3.3333333333333335, None), id="true_division"),
            pytest.param((5, "~", 3), (1, 2), id="floor_division_with_remainder"),
        ],
    )
    def test_all_supported_calculations(
        self, test_calc: tuple[int, str, int], expected_result: tuple[int, int | None]
    ) -> None:

        val1, op, val2 = test_calc
        expected_integer, expected_fractional = expected_result

        result = calculate(val1, val2, op)

        assert result.integer == expected_integer
        assert result.fractional == expected_fractional


class TestResult:
    @pytest.mark.parametrize(
        ("result", "expected_text"),
        [
            pytest.param(Result(20), "The answer is 20", id="whole_number"),
            pytest.param(Result(10 / 3), "The answer is 3.33", id="rounds_to_two_places"),
            pytest.param(Result(1, 2), "The answer is 1, remainder 2", id="with_remainder"),
        ],
    )
    def test_str_formats_answer(self, result: Result, expected_text: str) -> None:

        assert str(result) == expected_text


class TestMain:
    def test_runs_requested_number_of_calculations(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        inputs = iter(["2", "10+20", "5~3"])
        monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

        main()

        output = capsys.readouterr().out
        assert "The answer is 30" in output
        assert "The answer is 1, remainder 2" in output
