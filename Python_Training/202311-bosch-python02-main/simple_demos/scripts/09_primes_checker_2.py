from console import read_int, read_bool
import primeutils as p

def main():

    while True:
        number=read_int('number?')
        if p.is_prime(number):
            print(f'{number} is prime')
        else:
            print(f'{number} is not prime')

        if read_bool('continue [Y/n]?')==False:
            break

    print('Thanks for using the program')


main() # call manually