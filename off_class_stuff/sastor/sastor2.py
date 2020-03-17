n, k = tuple(map(int, input().split()))
# n, k = 5, 3
lst = sorted([int(x) for x in input().split()])
# lst = sorted([-3, 1, 4, 5, 0, 100])

answers = []

answers.append(max(lst) - min(lst))
# print(lst)

for i in range(n + 1):
    lst_trial = lst[:]
    for j in range(i):
        lst_trial[j] += k


    for j in range(i, n):
        lst_trial[j] -= k
    # lst_trial[-1] -= k

    length = max(lst_trial) - min(lst_trial)
    # print(lst_trial, length)
    answers.append(max(lst_trial) - min(lst_trial))



print(min(answers))