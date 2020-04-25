t, b = list(map(int, input().split()))

if b > 10:
    print('0'*b)


def get_array():
    res = []
    for j in range(b):
        print(j + 1)
        char = input()
        if char == 'N':
            return None
        res.append(char)
    return "".join(res)


for i in range(t):
    x = get_array()
    if x is None:
        break
    print(x)
    y = input()
    if y == 'Y':
        continue
    else:
        break
