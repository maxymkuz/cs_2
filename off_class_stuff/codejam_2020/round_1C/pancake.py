

def main(d, slices, k):
    if d == 2:
        if len(set(slices)) != len(slices):
            # print('zero')
            return 0
        else:
            # print('one')
            return 1
    elif d == 3:
        minimal = 2
        for i in slices:
            # print(int(i / 2) == i / 2, i)
            if slices.count(i) == 3:
                # print('Zero')
                return 0
            elif int(i / 2) == i / 2 and int(i / 2) in slices:
                # print('one')
                minimal = 1
            elif slices.count(i) == 2 and max(slices) > i:
                # print('one')
                minimal = 1

        return minimal


t = int(input())

for k in range(t):
    n, d = list(map(int, input().split()))
    slices = list(map(int, input().split()))
    miniimal = main(d, slices, k)
    print('Case #{}: {}'.format(k+1, miniimal))

# print(main(2, [1, 2, 3], 1))
