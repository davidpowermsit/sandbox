OPERATORS = ["+", "-", "*", "/", "~"]


def find_operator(text: str) -> tuple[int, int, str]:
    for op in OPERATORS:
        left, found, right = text.partition(op)
        if found:
            return int(left), int(right), op
    raise ValueError(f"No operator found in {text!r}")


def calculate(text_input: str) -> tuple[int, int]:

    val1, val2, opp = find_operator(text_input)

    match opp:
        case "+":
            return (val1 + val2, 0)
        case "-":
            return (val1 - val2, 0)
        case "*":
            return (val1 * val2, 0)
        case "/":
            return (val1 // val2, val1 % val2)
        case "~":
            return (val1 // val2, val1 % val2)

    raise ValueError("No Opperator found in calculation")


def main() -> None:
    print("Welcome to the Python calculator!")

    user_input = ""
    times = 0

    while True:
        times = int(input("How many calculations do you want to do? "))
        for _i in range(times):
            user_input = input("Type Exit or Enter a calculate? ")
            if user_input.lower() == "exit":
                break

            result, remainder = calculate(user_input)
            if remainder != 0:
                print(f"The answer is {result}")
                print(f"The remainder is {remainder}")
            else:
                print(f"The answer is {result}")


if __name__ == "__name__":
    main()
