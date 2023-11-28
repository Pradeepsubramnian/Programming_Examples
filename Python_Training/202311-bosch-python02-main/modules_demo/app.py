### Main Application File
from libs.utils.console import read_int
import libs.utils.primes as p 
import libs.stats.frequency as f
#from libs.stats.histogram import * # NOT RECOMMENDED. PREFER NEXT LINE

from libs.stats.histogram import plot_histogram


def main():
    # let plot a histogram of all primes under 1000 ending with 1,3,5,7,9
    print('Prime Analysis Application')
    print('Select the range for primes')
    min=read_int('min? ')
    max=read_int('max? ')

    primes=[i%10 for i in p.prime_range(min,max)]

    frequency= f.create_freqency_table(primes)

    plot_histogram(frequency, design="❚")



if __name__ == '__main__':
    main()