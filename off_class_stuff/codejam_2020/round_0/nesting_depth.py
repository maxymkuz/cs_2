number_of_strings = int(input())

string_lst = [input() for i in range(number_of_strings)]


def place_parenthesis(line):
    line_lst = list(line)
    depth = 0
    i = 0
    while i < len(line_lst):
        parenthesis_difference = int(line_lst[i]) - depth
        if parenthesis_difference > 0:
            line_lst.insert(i, "("*parenthesis_difference)
            depth += parenthesis_difference
            i += 1
        elif parenthesis_difference < 0:
            line_lst.insert(i, ")"*abs(parenthesis_difference))
            depth += parenthesis_difference
            i += 1
        i += 1
    if depth > 0:
        line_lst.append(")"*depth)

    return "".join(line_lst)


if __name__ == '__main__':
    for j in range(len(string_lst)):
        print("Case #{}: {}".format(j+1, place_parenthesis(string_lst[j])))
