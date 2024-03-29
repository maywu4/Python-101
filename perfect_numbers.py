# Instructions
# Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.

# The Greek mathematician Nicomachus devised a classification scheme for positive integers, identifying each as belonging uniquely to the categories of perfect, abundant, or deficient based on their aliquot sum. The aliquot sum is defined as the sum of the factors of a number not including the number itself. For example, the aliquot sum of 15 is (1 + 3 + 5) = 9

# Perfect: aliquot sum = number
# 6 is a perfect number because (1 + 2 + 3) = 6
# 28 is a perfect number because (1 + 2 + 4 + 7 + 14) = 28
# Abundant: aliquot sum > number
# 12 is an abundant number because (1 + 2 + 3 + 4 + 6) = 16
# 24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36
# Deficient: aliquot sum < number
# 8 is a deficient number because (1 + 2 + 4) = 7
# Prime numbers are deficient
# Implement a way to determine whether a given number is perfect. Depending on your language track, you may also need to implement a way to determine whether a given number is abundant or deficient.

# Exception messages
# Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

# This particular exercise requires that you use the raise statement to "throw" a ValueError if the classify() function is passed a number that is not a positive integer. The tests will only pass if you both raise the exception and include a message with it.

# To raise a ValueError with a message, write the message as an argument to the exception type:

# # if a number to be classified is less than 1.
# raise ValueError("Classification is only possible for positive integers.")

def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    sum = 0
    i = 1
    while i < number:
        if number % i == 0:
            sum += i

        i += 1

    if sum == number:
        return 'perfect'
    elif sum > number:
        return 'abundant'
    else:
        return 'deficient'

print(classify(6))