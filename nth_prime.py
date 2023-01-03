def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')

    primes = []
    i = 2
    while len(primes) < number:
        # print(primes)
        # print(i)
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes[-1]

def is_prime(num):
    if (num < 2):
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True



def prime_range(num):
    primes = []
    i = 2
    while len(primes) < num:

        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

# print(prime(2))
# print(prime(6))
print(prime(10001))
# print(prime_range(20))