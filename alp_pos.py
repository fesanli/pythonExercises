def alphabet_position(text):
    return ' '.join( [str(ord(letter.upper())-64) for letter in text if letter.isalpha()] )

print(alphabet_position(input()))
