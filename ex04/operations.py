import sys


def operate(a, b):
    print(f"Sum:        {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product:    {a * b}")
    if b != 0:
        print(f"Quotient:   {a / b}")
        print(f"Remainder:  {a % b}")
    else:
        print("Quotient:   ERROR (div by zero)}")
        print("Remainder:  ERROR (modulo by zero)")


def print_usage(filename):
    print(f"Usage: python {filename} <number1> <number2>",
          "Example:",
          f"   python {filename} 10 3", sep='\n')


if len(sys.argv) < 3:
    print("InputError: not enough arguments")
    print_usage(sys.argv[0])
elif len(sys.argv) > 3:
    print("InputError: too many arguments")
    print_usage(sys.argv[0])
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        operate(a, b)
    except ValueError:
        print("InputError: only numbers")
