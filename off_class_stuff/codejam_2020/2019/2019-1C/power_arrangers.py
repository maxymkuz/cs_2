from itertools import permutations

letters = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
letters_back = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
res = ''
indexes = []
orders = ['' for i in range(120)]
print(orders)

# for i in 'ABCDE':
#     for j in range(6):
#         print(i)

l = list(map(lambda x: [letters_back[i] for i in x],
             list(permutations(range(1, 6)))))

index = 0

for index in range(5):
    for j in range(595):
        if j % 5 == 0:
            place = j // 5
            if orders[place].startswith(res):
                print(j + index)
                i = input()
                if i == 'N':
                    print('That is bad')
                else:
                    letters[i] += 1
                    orders[place] += i

    for i in letters:
        if letters[i] != 24:
            res += i
            print(res)

first = res[0]
letters = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
indexes_2 = []

for i in range(595):
    if i % 5 == 0:
        place = i // 5
        if orders[place].startswith(res):
            print(i + 1)
            x = input()
            if x == 'N':
                print('That is bad')
            else:
                letters[x] += 1
                orders[place] += x

for i in letters:
    if letters[i] != 6:
        res += i
        print(res)
