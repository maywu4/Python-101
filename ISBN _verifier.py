# ISBN
# The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

# (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
# If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

# Let's take the ISBN-10 3-598-21508-8. We plug it in to the formula, and get:

# (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
# Since the result is 0, this proves that our ISBN is valid.

def is_valid(isbn):
    nums = list(range( 1, 11))
    nums.sort(reverse=True) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    hyphen = '-'
    sum = 0
    lst = [char for char in isbn if char != hyphen] #['3', '5', '9', '8', '2', '1', '5', '0', '8', '8']

    if len(lst) != 10:
        return False
    
    for i in range(len(lst)):
        
        if (lst[i] != 'X') and (int(lst[i]) not in (nums + [0])):
            return False
        elif lst[i] == 'X':
            sum += 10 * nums[i]
            
        elif int(lst[i]) in (nums + [0]):
            sum += int(lst[i]) * nums[i]

        else:
            return False
            

    if sum % 11 == 0:
        return True
    else: 
        return False


print(is_valid("3-598-21508-8")) #True
print(is_valid("3-598-21507-X")) #True
print(is_valid("3598215088")) #True
print(is_valid("359821507X")) #True