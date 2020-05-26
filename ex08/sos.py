import sys

morse = {
    'A': '.-',      'B': '-...',    'C': '-.-.',
    'D': '-..',     'E': '.',       'F': '..-.',
    'G': '--.',     'H': '....',    'I': '..',
    'J': '.---',    'K': '-.-',     'L': '.-..',
    'M': '--',      'N': '-.',      'O': '---',
    'P': '.--.',    'Q': '--.-',    'R': '.-.',
    'S': '...',     'T': '-',       'U': '..-',
    'V': '...-',    'W': '.--',     'X': '-..-',
    'Y': '-.--',    'Z': '--..',

    '1': '.----',   '2': '..---',   '3': '...--',
    '4': '....-',   '5': '.....',   '6': '-....',
    '7': '--...',   '8': '---..',   '9': '----.',
    '0': '-----',

    ' ': '/'
}


def translate(text):
    translated = []
    for c in text:
        morse_c = morse.get(c)
        if not morse_c:
            return None
        translated.append(morse_c)
    return (translated)


if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
    translated = translate(text.upper())
    if not translated:
        print("ERROR")
        exit(1)
    print(*translated, sep=" ")
