def is_lishrel(n):
    """
    Returns True if num is lishel
    """
    for i in range(10):
        next_num = n + int(str(n)[::-1])
        if next_num == int(str(next_num)[::-1]):
            return False
        n = next_num
    return True


def main():
    """
    Main section
    """
    found = False
    while not found:
        res = [i for i in range(10**5, 10**6) if str(i*i).endswith(str(i))]
        for i in res:
            for j in res:
                if i == j:
                    continue
                if not is_lishrel(i*j):
                    print(i*j)
                    found = True
                    for k in res:
                        for l in res:
                            if k != l and k * l == i*j:
                                print(k, l)
                    break
            if found:
                break


if __name__ == "__main__":
    main()
