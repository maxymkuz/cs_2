def is_trymorf():
    """
    Returns a list of 5-digit trymorf numbers
    () -> list
    """
    return [i for i in range(10**4, 10**5) if str(i*i*i).endswith(str(i))]


def divisors(number):
    for i in range(int(number**0.5) + 1):
        b = 


def main():
    res = [i*j for i in is_trymorf() for j in is_trymorf() if i != j]
    num = max([i for i in res if all([str(i)[j] >= str(i)[j-1]
              for j in range(1, len(str(i)))])])
    print(num)
    divisors = [(i, j) for i in range(int(num**0.5) + 1)
                for j in range(i, int(num**0.5) + 1) if i**2 + j**2 == num]
    print(divisors)


if __name__ == "__main__":
    main()
