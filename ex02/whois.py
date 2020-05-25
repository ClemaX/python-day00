import sys

if len(sys.argv) > 2:
    print("Error")
if len(sys.argv) == 2:
    try:
        value = int(sys.argv[1])
        print("I'm Odd." if value % 2 else "I'm Even.")
    except ValueError:
        print("Error")
