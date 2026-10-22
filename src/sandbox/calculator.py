from dataclasses import dataclass

OPERATORS = ["+", "-", "*", "/", "~"]


def parse_user_input(text: str) -> tuple[int, int, str]:
    for op in OPERATORS:
        left, found, right = text.partition(op)
        if found:
            return int(left), int(right), op
    raise ValueError(f"No operator found in {text!r}")


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
