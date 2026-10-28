limit: int = 1000


def main() -> None:
    total: int = 0

    while total < limit:
        user_value = int(input("Please enter a value: ").strip())
        total += user_value

    print(f"The Total is: {total}")


if __name__ == "__main__":
    main()
