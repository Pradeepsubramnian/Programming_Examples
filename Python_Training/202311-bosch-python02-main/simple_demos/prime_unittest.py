import unittest
import scripts.primeutils as p

class IsPrimeTests(unittest.TestCase):
    def test_2_is_prime(self):
        self.assertTrue(p.is_prime(2))

    def test_12_is_not_prime(self):
        self.assertFalse(p.is_prime(12))

    def test_total_primes_under_10_is_4(self):
        primes=p.prime_range(0,10)
        self.assertEqual(4,len(primes))



if __name__ == "__main__":
    unittest.main()