def is_prime(number):
    if number<2:
        return False
    test=2
    while test <number:
        if number%test == 0:
            return False
        test+=1

    return True


def prime_range(min,max):
    primes=[]
    for n in range(min,max):
        if is_prime(n):
            primes.append(n)
    return primes