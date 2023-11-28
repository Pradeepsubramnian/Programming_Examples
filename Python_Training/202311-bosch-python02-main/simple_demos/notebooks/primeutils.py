def is_prime(number):
    
    test=2
    while test <number:
        if number%test == 0:
            return False
        test+=1

    return True