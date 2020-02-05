from math import sqrt


def kaprekar():
    """
    Returns list of kaplekar nums
    """
    res = []
    for i in range(10**3, 10**4):
        square = str(i**2)
        for j in range(1, len(str(i**2))):
            if i == int(str(i*i)[:j]) + int(str(i*i)[j:]):
                res.append(i)
    return res


if __name__ == "__main__":
    num = min(list(filter(lambda x: str(x) != str(x)[::-1],
                   [i*j for i in kaprekar() for j in kaprekar() if i != j])))
    divisors = [(i, j) for i in range(int(sqrt(num)) + 1)
                for j in range(int(sqrt(num)) + 1) if i**2 + j**2 == num]
    print(num, divisors)
