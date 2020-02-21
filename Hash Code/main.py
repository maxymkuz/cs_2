def parse(location):
    """
    Потім
    :param location:
    :return:
    """
    with open(location, 'r', encoding="utf-8") as f:
        counter = 0
        libraries = []
        for line in f:
            line = line.strip().split()
            if len(line) == 0:
                continue
            if counter == 0:
                days = int(line[-1])
            elif counter == 1:
                books_scores = [int(i) for i in line]
            elif counter % 2 == 0:
                signup = int(line[1])
                daily_books = int(line[2])
            else:
                lib_set = sorted([int(i) for i in line], reverse=True, key=lambda x: books_scores[x])
                libraries.append({'signup': signup, 'daily': daily_books, 'books': lib_set, 'idx': (counter - 2)//2})
            counter += 1
        return libraries, books_scores, days


libs, scores, days = parse("d_tough_choices.txt")
days_left = days
scanned = set()
used_libs = []
min_days = 0


def find_best(libs):
    for i, lib in enumerate(libs):
        total_score = sum(map(lambda x: scores[x],
                              [book for book in lib['books'] if book not in scanned]))
        lib['score'] = total_score / lib['signup']
        lib['index'] = i
    maxi = max(libs, key=lambda x: x['score'])
    del libs[maxi['index']]
    return maxi




output_lst = []

while days_left > 0:
    maxi = find_best(libs)

    primary_idx = maxi['idx']
    num_of_books = len(maxi['books'])
    books_indexes = maxi['books']
    output_lst.append([str(primary_idx) + " " + str(num_of_books), ' '.join(list(map(str, books_indexes)))])
    used_libs.append(maxi)
    lib_index = maxi['index']
    days_left -= maxi['signup']
    scanned = scanned | set(maxi['books'])

num_lib = str(len(used_libs))

with open("E.txt", 'w') as f:
    f.write(num_lib + '\n')
    for lib in output_lst:
        f.write(lib[0] + '\n')
        f.write(lib[1] + '\n')

# print(sum(map(lambda x: scores[x], scanned)))
print(sum(map(lambda x: scores[x], scanned)))