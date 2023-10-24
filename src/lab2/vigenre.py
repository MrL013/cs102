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
    caps_lang = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lang = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')

    ciphertext = ""

    for i in range(len(plaintext)):

        if len(keyword) == len(plaintext):
            if plaintext[i].isupper():
                n_p = caps_lang.index(plaintext[i])
                if keyword[i].isupper():
                    n_k = caps_lang.index(keyword[i])
                    ciphertext += caps_lang[n_k+n_p]
                else:
                    n_k = lang.index(keyword[i])
                    ciphertext += lang[n_k+n_p]
            else:
                n_p = lang.index(plaintext[i])
                if keyword[i].isupper():
                    n_k = caps_lang.index(keyword[i])
                    ciphertext += caps_lang[n_k+n_p]
                else:
                    n_k = lang.index(keyword[i])
                    ciphertext += lang[n_k+n_p]

        elif len(keyword) < len(plaintext):

            keywords = list(keyword)
            k = len(plaintext) - len(keyword)
            K = k // len(keyword)
            for _ in range(K):
                keywords.extend(keywords)
            n = k % len(keyword)
            if n != 0:
                keywords.extend(keywords[:n])

            if plaintext[i].isupper():
                n_p = caps_lang.index(plaintext[i])
                if keywords[i % len(keywords)].isupper():
                    n_k = caps_lang.index(keywords[i % len(keywords)])
                    ciphertext += caps_lang[n_k + n_p]
                else:
                    n_k = lang.index(keywords[i % len(keywords)])
                    ciphertext += lang[n_k + n_p]
            else:
                n_p = lang.index(plaintext[i])
                if keywords[i % len(keywords)].isupper():
                    n_k = caps_lang.index(keywords[i % len(keywords)])
                    ciphertext += caps_lang[n_k + n_p]
                else:
                    n_k = lang.index(keywords[i % len(keywords)])
                    ciphertext += lang[n_k + n_p]

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

    caps_lang = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lang = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
    
    plaintext = ""

    for i in range(len(ciphertext)):

        if len(keyword) == len(ciphertext):
            if ciphertext[i].isupper():
                n_c = caps_lang.index(ciphertext[i])
                if keyword[i].isupper():
                    n_k = caps_lang.index(keyword[i])
                    plaintext += caps_lang[n_c - n_k]
                else:
                    n_k = lang.index(keyword[i])
                    plaintext += lang[n_c - n_k]
            else:
                n_c = lang.index(ciphertext[i])
                if keyword[i].isupper():
                    n_k = caps_lang.index(keyword[i])
                    plaintext += caps_lang[n_c - n_k]
                else:
                    n_k = lang.index(keyword[i])
                    plaintext += lang[n_c - n_k]

        elif len(keyword) < len(ciphertext):
            keywords = list(keyword)
            k = len(ciphertext) - len(keyword)
            K = k // len(keyword)
            for _ in range(K):
                keywords.extend(keywords)
            n = k % len(keyword)
            if n != 0:
                keywords.extend(keywords[:n])

            if ciphertext[i].isupper():
                n_c = caps_lang.index(ciphertext[i])
                if keywords[i % len(keywords)].isupper():
                    n_k = caps_lang.index(keywords[i % len(keywords)])
                    plaintext += caps_lang[n_c - n_k]
                else:
                    n_k = lang.index(keywords[i % len(keywords)])
                    plaintext += lang[n_c - n_k]
            else:
                n_c = lang.index(ciphertext[i])
                if keywords[i % len(keywords)].isupper():
                    n_k = caps_lang.index(keywords[i % len(keywords)])
                    plaintext += caps_lang[n - n_k]
                else:
                    n_k = lang.index(keywords[i % len(keywords)])
                    plaintext += lang[n_c - n_k]

    return plaintext

