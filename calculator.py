"""Simple calculator script."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main() -> None:
    print("Simple Calculator")
    print("Select operation: +, -, *, /")
    operation = input("Operation: ").strip()
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
    except ValueError as exc:
        raise ValueError("Please enter valid numbers.") from exc

    if operation == "+":
        result = add(first, second)
    elif operation == "-":
        result = subtract(first, second)
    elif operation == "*":
        result = multiply(first, second)
    elif operation == "/":
        result = divide(first, second)
    else:
        raise ValueError("Unsupported operation.")

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
