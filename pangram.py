def is_pangram(sentence):
    ALPHA = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    chars = [char for char in sentence]

    for letter in ALPHA:
        if (letter.lower() not in chars) and (letter not in chars):
            return False

    return True
    


print(is_pangram("the quick brown fox jumps over the lazy dog"))