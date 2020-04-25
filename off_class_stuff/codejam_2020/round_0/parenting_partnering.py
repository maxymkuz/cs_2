test_cases = int(input())
cases = {}
for case in range(test_cases):
    n = int(input())
    cases[case] = [list(map(int, input().split())) for i in range(n)]


def assign_activities(lst):
    lst = [lst[i] + [i] for i in range(len(lst))]
    lst.sort(key=lambda x: x[0])
    free_time = {'C': 0, 'J': 0}
    for i in range(len(lst)):
        if free_time['C'] <= lst[i][0]:
            free_time['C'] = lst[i][1]
            lst[i].append('C')
        elif free_time['J'] <= lst[i][0]:
            free_time['J'] = lst[i][1]
            lst[i].append('J')
        else:
            return "IMPOSSIBLE"
    return "".join([i[-1] for i in sorted(lst, key=lambda x: x[-2])])


for x in cases:
    print("Case #{}: {}".format(x + 1, assign_activities(cases[x])))
