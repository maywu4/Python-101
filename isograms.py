# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

# Examples of isograms:

# lumberjacks
# background
# downstream
# six-year-old
# The word isograms, however, is not an isogram, because the s repeats.

def is_isogram(string):
    string = string.lower()
    for char in string:
        if (string.count(char) > 1) and (char != '-') and (char != ' '):
            return False

    return True

    
print(is_isogram('isograms'))
print(is_isogram('downstream'))