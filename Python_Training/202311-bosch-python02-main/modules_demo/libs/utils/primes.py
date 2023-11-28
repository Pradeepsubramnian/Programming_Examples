
def is_prime(number):
    for test in range(2,number):
        if number%test==0:
            return False
    return True


def prime_range(min=2,max=None):
    if max is None:
        min,max=2,min

    primes=[]
    for number in range(min,max):
        if is_prime(number):
            primes.append(number)

    return primes


def is_prime_tests():
    test_data= {2:True, -2:False, 15:False, 31:True, 37:True, 81:False}
    failed=0
    passed=0
    for number,expected in test_data.items():
        actual = is_prime(number)
        
        if actual!=expected:
            print(f'FAILED for {number}\n\texpected: {expected}\tactual: {actual}')
            failed+=1
        else:
            print(f'PASSED for {number}')
            passed+=1

    print(f'{passed} of {len(test_data)} tests passed\n')


def prime_range_tests():
    test_data= [(2,10,4),(0,50,15),(50,100,15),(0,100,25)]

    for min,max,count in test_data:
        result=prime_range(min,max)
        if count!=len(result):
            print(f'FAILED FOR {min}-{max}\texpected={count}\tfound={len(result)}')
        else:
            print(f'PASSED for {min}-{max}')


print(f'Loading Mdoule {__name__}')

if __name__=='__main__':
    is_prime_tests()
    prime_range_tests()



    