from dataclasses import dataclass


def parse_user_input(text: str) -> tuple[int, int, str]:
    """Finds the operator from the user input which may have negitive values e.g. -1-1 or 1--1. Once found return two values and opperator"""

    for i in range(len(text)):
        if is_operator(text[i]) and has_previous_char(i) and is_previous_char_a_digit(text, i):
            val1 = int(text[:i])
            val2 = int(text[i + 1 :])
            op = text[i]
            return val1, val2, op

    raise ValueError(f"No operator found in {text!r}")


def is_operator(char: str) -> bool:
    return char in ["+", "-", "*", "/", "~"]


def has_previous_char(index: int) -> bool:
    return index > 0


def is_previous_char_a_digit(text: str, index: int) -> bool:
    return text[index - 1].isdigit()


@dataclass(frozen=True)
class Result:
    integer: float
    fractional: int | None = None

    def __str__(self) -> str:
        if self.fractional is None:
            return f"The answer is {round(self.integer, 2)}"
        else:
            return f"The answer is {self.integer}, remainder {self.fractional}"


def calculate(val1: int, val2: int, opp: str) -> Result:

    match opp:
        case "+":
            return Result(val1 + val2, None)
        case "-":
            return Result(val1 - val2, None)
        case "*":
            return Result(val1 * val2, None)
        case "/":
            return Result(val1 / val2, None)
        case "~":
            return Result(val1 // val2, val1 % val2)

    raise ValueError("No Opperator found in calculation")


def main() -> None:
    print("Welcome to the Python calculator!")

    times = int(input("How many calculations do you want to do? "))

    for _i in range(times):
        user_input = input("Enter a calculate: ")

        val1, val2, opp = parse_user_input(user_input)

        result = calculate(val1, val2, opp)

        print(result)


if __name__ == "__main__":
    main()
