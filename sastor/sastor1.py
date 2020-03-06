n = int(input())
lst = []
for i in range(n):
    lst.append(tuple(map(int, input().split())))

max_x = max([i[0] for i in lst])
max_y = max([i[1] for i in lst])

res = 0

for i in range(n):
    res += max_x - lst[i][0] + max_y - lst[i][1]

print(res)