def isbn_10(string):
    res = 0
    for i in range(9):
        res += int(string[i]) * (i + 1)
    return res % 11


def isbn_13(string):
    res = 0
    for i in range(12):
        res += int(string[i]) * (i + 1)
    return res % 11


def usps(string):
    return sum([int(i) for i in string]) % 9


def upc(string):
    res = 0
    for i in range(len(string)):
        res += int(string[i]) if i % 2 == 0 else int(string[i]) * 3


def issn(string):
    return sum([int(string[i]) * (i + 3) for i in range(len(string))]) % 11



def pseudorandom(x0, m, n, p):
    print(x0)
    for i in range(10):
        x0 = (m * x0 + n) % p
        print(x0)


# pseudorandom(1, 3, 2, 13)
# print(isbn_10('007119881'))
print(issn('6823791'))

