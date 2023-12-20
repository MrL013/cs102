import unittest
import random
import string

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    caps_lang = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lang = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

    ciphertext = ""
    keyword = keyword.upper()

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = keyword[i % len(keyword)]
            if plaintext[i].isupper():
                n_p = caps_lang.index(plaintext[i])
                n_k = caps_lang.index(shift)
                ciphertext += caps_lang[(n_p + n_k) % 26]
            else:
                n_p = lang.index(plaintext[i])
                n_k = caps_lang.index(shift)
                ciphertext += lang[(n_p + n_k) % 26]
        else:
            ciphertext += plaintext[i]

    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    caps_lang = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lang = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

    plaintext = ""
    keyword = keyword.upper()

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = keyword[i % len(keyword)]
            if ciphertext[i].isupper():
                n_c = caps_lang.index(ciphertext[i])
                n_k = caps_lang.index(shift)
                plaintext += caps_lang[(n_c - n_k) % 26]
            else:
                n_c = lang.index(ciphertext[i])
                n_k = caps_lang.index(shift)
                plaintext += lang[(n_c - n_k) % 26]
        else:
            plaintext += ciphertext[i]

    return plaintext

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
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))

if __name__ == '__main__':
    unittest.main()
