def is_sum_of_two_primes(number: int) -> bool:
    # Guard for even numbers
    if number % 2 == 1:
        return False

    for candidate_prime in range(2, number):
        if _is_prime(candidate_prime):
            candidate_partner = number - candidate_prime
            if candidate_partner >= 2 and _is_prime(candidate_partner):
                print(f"The number {number} equals to the sum of {candidate_prime} and {candidate_partner}")
                return True

    return False


def _is_prime(candidate_int: int) -> bool:
    """check if candidate_int is a prime"""
    starting_number = 2
    while starting_number < candidate_int:
        if candidate_int % starting_number == 0:
            return False
        starting_number += 1
    return True


def _get_number() -> int:
    while True:
        user_input = input("Enter a number: ")
        try:
            return int(user_input)
        except ValueError:
            print(f"'{user_input}' is not a valid integer. Please try again.")


number = _get_number()
is_sum_of_two_primes(number)
