from calc import Calculator


def main():
    a = 3
    b = 5
    calc = Calculator(a, b)
    print(calc)
    expected_str = f"{a = }, {b = }"
    print(expected_str)


if __name__ == "__main__":
    main()
