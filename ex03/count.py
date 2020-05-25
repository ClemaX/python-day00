import string


def text_analyzer(*args):
    if len(args) == 0:
        text = input("What is the text to analyse?\n")
    elif len(args) == 1:
        text = args[0]
    elif len(args) > 1:
        print("Error")
        return
    length = len(text)
    upper = len([c for c in text if c.isupper()])
    lower = len([c for c in text if c.islower()])
    punct = len([c for c in text if c in string.punctuation])
    spaces = len([c for c in text if c in string.whitespace])

    print(f"The text contains {length} characters:", end="\n\n")
    print(f"- {upper} upper letters", end="\n\n")
    print(f"- {lower} lower letters", end="\n\n")
    print(f"- {punct} punctuation mark", end="\n\n")
    print(f"- {spaces} spaces")
