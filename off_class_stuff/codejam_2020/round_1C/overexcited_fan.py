def length(x, y):
    return abs(x) + abs(y)


add_dct = {'N': 1, 'S': -1, 'E': 1, 'W': -1}


def main(path, x, y, j):
    path_lst = []
    for i in range(len(path)):
        if path[i] in ('N', 'S'):
            y += add_dct[path[i]]
        else:
            x += add_dct[path[i]]
        path_lst.append([i + 1, length(x, y)])
        # print(x, y, 'len', length(x, y))

    # print(path_lst)
    for i in path_lst:
        if i[0] >= i[1]:
            # print('found', i, i[0])
            print('Case #{}: {}'.format(j+1, i[0]))
            return None
    print('Case #{}: IMPOSSIBLE'.format(j))


t = int(input())

for j in range(t):
    x, y, path = input().split()
    x, y = int(x), int(y)
    main(path, x, y, j)



