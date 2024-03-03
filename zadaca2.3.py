def change_to_lowercase(word):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase_letters = ''

    for char in word:
        if alphabet.index(char) > 25:
            lowercase_letters += alphabet[alphabet.index(char) - 26]

    return lowercase_letters


word = str(input("Upišite riječ: "))
print(change_to_lowercase(word=word))

# Results
# Enter a word: FERE
# fere
# Enter a word: PYTHONISFUN
# pythonisfun

# Results
# Enter a word: FERE
# fere
# Enter a word: PYTHONISFUN
# pythonisfun