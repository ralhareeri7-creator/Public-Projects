VOWELS = "aeiou"
word = str(input(":~Enter a word ('quit' to quit)~:")).lower()

while word != "quit":
    if word == "":
        print("Can't convert an empty string. Try again.")
    elif word [0] in VOWELS:
        print( word + "way")
    else:
        i = 0
        while i < len(word) and word[i] not in VOWELS:
            i += 1
        print( word[i:] + word[:i] + "ay")

    word = str(input(":~Enter a word ('quit' to quit)~:")).lower()



