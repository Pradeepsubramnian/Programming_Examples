import scripts.primeutils as p

def test_2_is_prime():
    assert p.is_prime(2)==True


def test_12_is_not_prime():
    assert p.is_prime(12)==False


def test_there_are_25_primes_under_100():
    assert len(p.prime_range(0,100))==100