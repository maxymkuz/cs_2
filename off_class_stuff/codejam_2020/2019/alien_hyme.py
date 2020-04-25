lst = ['CAMERA', 'LOETDADA', 'OCLAHOMA', 'HMERA', 'HRA', 'HRA', 'HRY',
       'CAMERY', 'HERA', 'KDNERA', 'HA', 'JY', 'AY', 'YA']

lst = sorted([i[::-1] for i in lst])
solutions = []

def difference(str1, str2):
    dif = 0
    for j in range(len(str1)):
        if str1[j] == str2[j]:
            dif += 1
        else:
            return dif
    return dif


lst[0] = [0, lst[0], True]

for i in range(1, len(lst)):
    lst[i] = [difference(lst[i], lst[i-1][1]), lst[i], True]

for i in range(1, len(lst)-1):
    if lst[i][0] > lst[i-1][0] and lst[i][0] > lst[i+1][0]:
        print(lst[i], lst[i-1])
        solutions.append((lst[i][1], lst[i-1][1], difference(lst[i][1],
                                                             lst[i-1][1])))
        lst[i][-1], lst[i-1][-1] = False, False
# lst.sort(key=lambda x: x[0], reverse=True)
print(lst)
