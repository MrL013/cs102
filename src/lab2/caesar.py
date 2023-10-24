def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    k = shift % 26
    Z = 90
    z = 122
    
    for i in range(len(plaintext)):
        n = ord(plaintext[i])
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                if n + k <= Z:
                    ciphertext += chr(n+k)
                else:
                    x = n + k - Z
                    ciphertext += chr(64 + x)
            else:
                if n + k <= z:
                    ciphertext += chr(n+k)
                else:
                    x = n + k - z
                    ciphertext += chr(96 + x)

        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    k = shift % 26
    A = 65
    a = 97

    for i in range(len(ciphertext),):
        n = ord(ciphertext[i])
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                if n - k >= A:
                    plaintext += chr(n-k)
                else:
                    x = A - (n-k)
                    plaintext += chr(91 - x)
            else:
                if n - k >= a:
                    plaintext += chr(n-k)
                else:
                    x = a - (n-k)
                    plaintext += chr(123 - x)

        else:
            plaintext += ciphertext[i]
    
    return plaintext


