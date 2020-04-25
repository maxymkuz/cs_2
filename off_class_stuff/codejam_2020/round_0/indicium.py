def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l


def make_diagonal(n, results=[], result=[]):
    if len(result) == n:
        results.append(result)
        return results
    for i in range(1, n+1):
        new_result = result[:]+[i]
        make_diagonal(n, results, new_result)
    return results



def check(a):
    l = len(a)
    for i in range(l):
        b = [0] * (l + 1)
        for j in range(l):
            b[a[i][j]] += 1
            if b[a[i][j]] == 2:
                return False
    for i in range(l):
        b = [0] * (l + 1)
        for j in range(l):
            b[a[j][i]] += 1
            if b[a[j][i]] == 2:
                return False
    return True


def print_ans(a, l):
    if a is None:
        print("Case #{}: IMPOSSIBLE".format(l + 1))
    else:
        print("Case #{}: POSSIBLE".format(l + 1))
        for i in a:
            print(' '.join([str(k) for k in i]))


def check_sum(arr, k):
    return sum([arr[i][i] for i in range(len(arr))]) == k


def check_column(arr, current_row):
    for col in range(len(arr)):
        elem = arr[current_row][col]
        for row in range(current_row):
            if arr[row][col] == elem:
                return False
    return True


def generate_arrays(permutations, arr, k, current_row=0):
    if current_row == len(arr):
        if check_sum(arr, k):
            # if check(arr):
                # print_ans(arr)
            return arr
        return None
    for i in permutations:
        arr[current_row] = i
        if not check_column(arr, current_row):
            continue
        if sum([arr[i][i] for i in range(current_row)]) + \
                (n - current_row)*n < k:
            continue
        if sum([arr[i][i] for i in range(current_row)]) > k - (n-current_row):
            continue

        if k == 25:
            if arr[0][0] != 5:
                continue
        if generate_arrays(permutations, arr, k, current_row+1) is not None:
            return arr
# n = 5
# l = 1
# permutations = permutation([i + 1 for i in range(n)])
# for k in range(30):
#     print(k)
#     print_ans(generate_arrays(permutations, [([0]*n)[:]]*n, k), k-1)

t = int(input())
inputs = [list(map(int, input().split())) for i in range(t)]
for l in range(t):
    n, k = inputs[l]
    if n > 5:
        print("I don't know yet")
    permutations = permutation([i + 1 for i in range(n)])
    print_ans(generate_arrays(permutations, [([0]*n)[:]]*n, k), l)
