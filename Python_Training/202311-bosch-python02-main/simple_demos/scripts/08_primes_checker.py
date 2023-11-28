import console
import primeutils as p



while True:
    number=console.read_int('number?')
    if p.is_prime(number):
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')

    if console.read_bool('continue [Y/n]?')==False:
        break

print('Thanks for using the program')