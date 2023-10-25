import unittest
from src.lab2.vigenere import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):

    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = vigenere.encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, vigenere.decrypt_vigenere(ciphertext, keyword))

if __name__ == '__main__':
    unittest.main()