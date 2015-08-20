__author__ = 'solomina'
#*******************************
# Function should print prime numbers until user stops it
def prime_numbers():
    yield 2
    num = 3
    primes = []
    while True:
        for divider in primes:
            if num % divider == 0: break
        else:
            primes.append(num)
            yield num
        num += 2


if __name__ == '__main__':
    for i in prime_numbers():
        print i
