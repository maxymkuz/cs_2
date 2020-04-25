answers = [10**9]


def recursive(x, y, jump):
    if jump >= min(answers):
        return False
    if 
    if x == 0 and y == 0:
        answers.append(jump)
        return ['1']

    if jump == 1:
        if x % 2 == 1 and y % 2 == 1:
            return False
        if x % 2 == 0 and y % 2 == 0:
            return False
        if x % 2 == 1:
            east = recursive(x - jump, y, jump * 2)
            west = recursive(x + jump, y, jump * 2)
            if east and west:
                if len(east) < len(west):
                    east.append('E')
                    return east
                else:
                    west.append('W')
                    return west
            if east:
                east.append('E')
                return east
            if west:
                west.append('W')
                return west

        if y % 2 == 1:

            north = recursive(x, y - jump, jump * 2)
            south = recursive(x, y + jump, jump * 2)
            if north and south:
                if len(north) < len(south):
                    north.append('N')
                    return north
                else:
                    south.append('S')
                    return south
            if north:
                north.append('N')
                return north
            if south:
                south.append('S')
                return south
        return False

    if y == 0:
        east = recursive(x - jump, y, jump * 2)
        west = recursive(x + jump, y, jump * 2)
        if east and west:
            if len(east) < len(west):
                east.append('E')
                return east
            else:
                west.append('W')
                return west
        if east:
            east.append('E')
            return east
        if west:
            west.append('W')
            return west

    if x == 0:
        north = recursive(x, y - jump, jump * 2)
        south = recursive(x, y + jump, jump * 2)
        if north and south:
            if len(north) < len(south):
                north.append('N')
                return north
            else:
                south.append('S')
                return south
        if north:
            north.append('N')
            return north
        if south:
            south.append('S')
            return south

    if x % 2 == 0 and y % 2 == 0:
        x /= 2
        y /= 2

    if x % 2 == 1 and y % 2 == 1:  # Just in case
        return False
    if x % 2 == 0 and y % 2 == 0:  # also hz
        return False

    if x % 2 == 1:
        x *= 2
        y *= 2
        east = recursive(x - jump, y, jump * 2)
        west = recursive(x + jump, y, jump * 2)
        if east and west:
            if len(east) < len(west):
                east.append('E')
                return east
            else:
                west.append('W')
                return west
        if east:
            east.append('E')
            return east
        if west:
            west.append('W')
            return west

    if y % 2 == 1:
        x *= 2
        y *= 2

        north = recursive(x, y - jump, jump * 2)
        south = recursive(x, y + jump, jump * 2)
        if north and south:
            if len(north) < len(south):
                north.append('N')
                return north
            else:
                south.append('S')
                return south
        if north:
            north.append('N')
            return north
        if south:
            south.append('S')
            return south
    return False

t = int(input())

for case in range(t):
    answers = [10**9]
    x, y = list(map(int, input().split()))
    res = recursive(x, y, 1)
    if res:
        res = ''.join(res[1:][::-1])
        print('Case #{}: '.format(case+1) + res)
    else:
        print('Case #{}: IMPOSSIBLE'.format(case+1))
