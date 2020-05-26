import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
    exit(1)

try:
    min_len = int(sys.argv[2])
except ValueError:
    print("ERROR")
    exit(1)

del_punct = sys.argv[1].maketrans('', '', string.punctuation)
text = sys.argv[1].translate(del_punct)

words = text.split(' ')
for word in words:
    if not word.isalpha():
        print("ERROR")
        exit(1)

filtered = [word for word in words if len(word) > min_len]

print(filtered)
