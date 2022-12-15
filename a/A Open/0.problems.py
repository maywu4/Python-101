
print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False


# RegEx
# Write a function, valid_zip_code that accepts a string and checks to see if it's a valid U.S. zip code. A valid U.S. zip code follows the following rules:

# Mandatory 5 digits
# Ranging from 0-9
# Optional 4 digits for area granularity
# Ranging from 0-9
# Mandatory 5 and optional 4 separated by a hyphen
# Hyphen not present if optional 4 isn't present If the zip code matches, return the zip code. If not, return an error text message.


def valid_zip_code(zip):
    pass

zip1 = '47243'
zip2 = '23128-'
zip3 = '01237-1238'
zip4 = '91374-31'
zip5 = '1321-9883'
zip6 = '6320'

print(valid_zip_code(zip1))     # '47243'
print(valid_zip_code(zip2))     # "The zip code you entered is invalid"
print(valid_zip_code(zip3))     # '01237-1238'
print(valid_zip_code(zip4))     # "The zip code you entered is invalid"
print(valid_zip_code(zip5))     # "The zip code you entered is invalid"
print(valid_zip_code(zip6))     # "The zip code you entered is invalid"



# Insertion Sort
# Create a function that uses the insertion sort algorithm to sort the list.

# Write your function, here.



print(insertion_sort([55, 21, 5, 3, 6, 95])) #> [3, 5, 6, 21, 55, 95]
print(insertion_sort([4, 1, 0, 3, 8, 9])) #> [0, 1, 3, 4, 8, 9]
print(insertion_sort([1, 4, 3, 0, 3, 0, 2, 8])) #> [0, 0, 1, 2, 3, 3, 4, 8]