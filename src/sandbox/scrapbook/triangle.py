def print_triangle(n: int) -> None:
    #   Guard clause
    if not (1 <= n <= 99 and n % 2 == 1):
        raise ValueError(f"value must be an odd number from 1-99, got {n!r}")

    line: list[str] = []
    numbers = list(range(1, n + 1))

    # build half the triangle
    for value in range(1, n + 1):
        line.append(f"{''.join(str(i) for i in numbers[:value]):<{n}}")

    # print the triangle in two halfs
    for li in line:
        print(li)
    for li in line[-2::-1]:
        print(li)


print_triangle(99)
