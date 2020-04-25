hlam = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
hohol = {hlam[i].upper(): i for i in range(len(hlam))}
hohol_back = {i: hlam[i].upper() for i in range(len(hlam))}


def cezar_ukr(string, p, m):
    res = ""
    for i in range(len(string)):
        l = (hohol[string[i].upper()] * p + m) % 26
        res += hohol_back[l]
    return res


def vigenere_encrypt_ukr(plaintext, key):
    key_length = len(key)
    key_as_int = [hohol[i] for i in key]
    plaintext_int = [hohol[i] for i in plaintext]
    print(key_as_int, plaintext_int)
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += hohol_back[value]
    return ciphertext


def vigenere_decrypt_ukr(ciphertext, key):
    key_length = len(key)
    key_as_int = [hohol[i] for i in key]
    ciphertext_int = [hohol[i] for i in ciphertext]
    print(key_as_int, ciphertext_int)
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 33
        plaintext += hohol_back[value]
    return plaintext


print(vigenere_encrypt_ukr("haveaniceweek".upper(), "online".upper()))
