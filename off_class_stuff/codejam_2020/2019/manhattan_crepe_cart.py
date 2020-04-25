t = int(input())

for k in range(t):
    p, q = list(map(int, input().split()))
    people = [input().split() for l in range(p)]
    people = [[int(i[0]), int(i[1]), i[2]] for i in people]
    people_we = sorted([(person[0], person[2]) for person in people if person[2] \
                        in ('W', 'E')], key=lambda x: x[0])

    num_we = len(people_we)
    grid_we = [0]  # (Coordinate, votes)
    # E - top; W - bottom
    for i in range(num_we):
        if people_we[i][-1] == 'E':
            grid_we.append(people_we[i][0] + 1)
        else:
            grid_we.append(people_we[i][0] - 1)

    grid_we = [[i, 0] for i in list(set(grid_we))]

    for i in people_we:
        pos = i[0]
        if i[-1] == 'E':
            for j in range(len(grid_we)):
                if pos < grid_we[j][0]:
                    grid_we[j][1] += 1
        elif i[-1] == 'W':
            for j in range(len(grid_we)):
                if pos > grid_we[j][0]:
                    grid_we[j][1] += 1

    # finding maximum:
    maximum = [0, 0]
    for i in range(len(grid_we)):
        if grid_we[i][1] > maximum[1]:
            maximum = grid_we[i]
    x = maximum[0]

    ###################################### Y

    people_ns = sorted([(person[1], person[2]) for person in people if person[2] \
                        in ('N', 'S')], key=lambda z: z[0])

    num_ns = len(people_ns)
    grid_ns = [0]  # (Coordinate, votes)
    # N - top; S - bottom
    for i in range(num_ns):
        if people_ns[i][-1] == 'N':
            grid_ns.append(people_ns[i][0] + 1)
        else:
            grid_ns.append(people_ns[i][0] - 1)

    grid_ns = [[i, 0] for i in list(set(grid_ns))]

    for i in people_ns:
        pos = i[0]
        if i[-1] == 'N':
            for j in range(len(grid_ns)):
                if pos < grid_ns[j][0]:
                    grid_ns[j][1] += 1
        elif i[-1] == 'S':
            for j in range(len(grid_ns)):
                if pos > grid_ns[j][0]:
                    grid_ns[j][1] += 1

    # finding maximum:
    maximum = [0, 0]
    for i in range(len(grid_ns)):
        if grid_ns[i][1] > maximum[1]:
            maximum = grid_ns[i]
    y = maximum[0]
    print("Case #{}: {} {}". format(k+1, x, y))
