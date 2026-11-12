# Run the program and note the exception type. What type is it? - TypeError
# Try to make the program crash-proof using conditionals (if/else statements).
# Try to make the program crash-proof using try/except/finally (Don't use the generic Exception).
# Which of the two methods do you prefer and why?


# def is_divisible_by(number: int, divisor: int) -> bool:
#     if type(number) is int and type(divisor) is int:
#         return number % divisor == 0
#     return False


def is_divisible_by(number: int, divisor: int) -> bool:
    try:
        return number % divisor == 0
    except (ValueError, TypeError):
        return False


print(is_divisible_by(10, 2))
# print(is_divisible_by(10, "2"))  # Causes an exception
print()

# -------------------------------------------------------------


def add_percentage(price: int, percentage: float) -> float:
    return price + (percentage * price)


print(add_percentage(100, 0.1))
# print(add_percentage(100, "0.05"))  # Causes an exception
print()
