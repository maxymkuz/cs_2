def leyland(n):
    """
    Returns a list of leyland numbers
    """
    return [i**j + j**i for i in range(int(10**n**0.5)+1)
            for j in range(int(10**n**0.5)+1) if len(str(i**j + j**i)) == n]


def main():
    leyland_numbers = list(leyland(5))
    res = [i*j for i in leyland_numbers for j in leyland_numbers if i != j]
    number = max(list(filter(lambda x: str(x) != str(x)[::-1], res)))
    good = [[i, number // i] for i in leyland_numbers
            if number % i == 0 and i <= number // i]
    print(number, list(good))


if __name__ == "__main__":
    main()
