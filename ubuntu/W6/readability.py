import string
letters = 0
words = 0
sentences = 0
index = 0
L = 0
S = 0
Text = input("Text: ")
for pos, i in enumerate(Text):
    try:
        if i.isalpha():
            letters += 1
        if i in string.punctuation:
            sentences += 1
        if i.isspace():
            words += 1
        if i == '"' or i == ',' or i == '-' or i == ':':
            sentences -= 1
        if i in string.punctuation and Text[pos + 1].isalpha() and Text[pos - 1].isalpha():
            sentences -= 1
    except IndexError:
        pass
words += 1
L = (letters / words) * 100
S = (sentences / words) * 100
index = (0.0588 * L) - (0.296 * S) - 15.8

if index > 16:
    print("Grade 16+\n")
if index > 0 and index <= 16:
    print(f"Grade {round(index)}\n")
if index < 0:
    print("Before Grade 1\n")
