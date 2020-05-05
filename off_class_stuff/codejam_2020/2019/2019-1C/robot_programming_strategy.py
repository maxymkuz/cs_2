import math

dct = {'R': 'P', 'P': 'S', 'S': 'R'}
lens = [24, 6, ]

def main(moves, a):
    res = ''
    for r in range(int(math.log2(a+1)) + 1):
        x = set()
        for p in range(len(moves)):
            x.add(moves[p][r % len(moves[p])])

        # print(x, r)
        if len(x) == 3:
            return False

        elif len(x) == 2:
            move = moves[0][r % len(moves[0])]
            beat = dct[moves[0][r % len(moves[0])]]
            moves = [moves[i] for i in range(len(moves)) if moves[i][r] != beat]
            # print(moves)
            res += move
        else:
            res += dct[list(x)[0]]
            return res
        x.clear()
    # print(moves)


t = int(input())

for j in range(t):
    a = int(input())
    moves = [input() for i in range(a)]
    result = main(moves, a)
    if result:
        print('Case #{}: {}'.format(j+1, result))
    else:
        print("Case #2: IMPOSSIBLE")
