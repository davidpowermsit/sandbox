OPERATORS = ["+", "-", "*", "/", "~"]


def parse_user_input(text: str) -> tuple[int, int, str]:
    for op in OPERATORS:
        left, found, right = text.partition(op)
        if found:
            return int(left), int(right), op
    raise ValueError(f"No operator found in {text!r}")


def calculate(val1: int, val2: int, opp: str) -> tuple[int | float, int | None]:

    match opp:
        case "+":
            return (val1 + val2, None)
        case "-":
            return (val1 - val2, None)
        case "*":
            return (val1 * val2, None)
        case "/":
            return (round(val1 / val2, 2), None)
        case "~":
            return (val1 // val2, val1 % val2)

    raise ValueError("No Opperator found in calculation")


def main() -> None:
    print("Welcome to the Python calculator!")

    times = int(input("How many calculations do you want to do? "))

    for _i in range(times):
        user_input = input("Enter a calculate: ")

        val1, val2, opp = parse_user_input(user_input)

        result, remainder = calculate(val1, val2, opp)

        if remainder is None:
            print(f"The answer is {result}")
        else:
            print(f"The answer is {result}, remainder {remainder}")


if __name__ == "__main__":
    main()
