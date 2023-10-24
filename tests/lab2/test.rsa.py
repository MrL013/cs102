import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt

class TestRSAFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(8))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_generate_keypair(self):
        public, private = generate_keypair(17, 19)
        # Add assertions for public and private keys

    def test_encrypt_decrypt(self):
        public, private = generate_keypair(17, 19)
        message = "test"
        encrypted_msg = encrypt(private, message)
        decrypted_msg = decrypt(public, encrypted_msg)
        self.assertEqual(message, decrypted_msg)

if __name__ == '__main__':
    unittest.main()