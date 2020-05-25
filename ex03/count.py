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
    upper = lower = punct = space = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c in string.punctuation:
            punct += 1
        elif c in string.whitespace:
            space += 1

    print(f"The text contains {length} characters:", end="\n\n")
    print(f"- {upper} upper letters", end="\n\n")
    print(f"- {lower} lower letters", end="\n\n")
    print(f"- {punct} punctuation mark", end="\n\n")
    print(f"- {space} spaces")
