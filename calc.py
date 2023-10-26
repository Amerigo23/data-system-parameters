# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """Implement the calculator"""
    pass  # YOUR CODE HERE
    if len(sys.argv) != 4:
        print("Usage: python calc.py <number1> <operator> <number2>")
        sys.exit(1)
    num1, operator, num2 = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Please provide valid integers as numbers.")
        sys.exit(1)
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
        result = num1 / num2
    else:
        print("Unsupported operator. Supported operators are +, -, * and /.")
        return 1
    return result


if __name__ == "__main__":
    result = main()
    print(result)
