OPERATORS = ["+", "-", "*", "/", "~"]


def find_operator(text: str) -> tuple[int, int, str]:
    for op in OPERATORS:
        left, found, right = text.partition(op)
        if found:
            return int(left), int(right), op
    raise ValueError(f"No operator found in {text!r}")


def calculate(text_input: str) -> tuple[int | float, int | None]:

    val1, val2, opp = find_operator(text_input)

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

    user_input: str

    times = int(input("How many calculations do you want to do? "))

    for _i in range(times):
        user_input = input("Enter a calculate: ")

        result, remainder = calculate(user_input)
        if remainder is None:
            print(f"The answer is {result}")
        else:
            print(f"The answer is {result}, remainder {remainder}")


if __name__ == "__main__":
    main()
