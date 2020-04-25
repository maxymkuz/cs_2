test_cases = int(input())
cases = {}
for case in range(test_cases):
    n = int(input())
    cases[case] = [list(map(int, input().split())) for i in range(n)]

for x in cases:
    matrix = cases[x]
    k = sum([matrix[row][row] for row in range(len(matrix))])
    r = sum([0 if len(matrix[row]) == len(set(matrix[row])) else 1
             for row in range(len(matrix))])
    c = 0
    for column in range(len(matrix)):
        col = [matrix[row][column] for row in range(len(matrix))]
        if len(col) != len(set(col)):
            c += 1
    print("Case #{}: {} {} {}".format(x + 1, k, r, c))
