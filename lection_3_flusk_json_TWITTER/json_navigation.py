import json
import copy


def get_ipt_dict(data):
    keys = [i for i in data]
    for i in range(len(keys)):
        print(str(i+1) + ". ", keys[i])
    inp = input("Enter one of the keys, listed above: ")
    while True:
        if inp == '-1':
            return -1
        if inp not in keys:
            inp = input("Enter VALID key, listed above: ")
        else:
            return inp


def get_ipt_list(temp_data):
    while True:
        print("There are "  + str(len(temp_data)) + " items in this list")
        print("Choose an index of a list item, you want to\
dive into in range: [0, " + str(len(temp_data)) + "]")
        print("To go back one level, type '-1'")
        print("To print the whole list, enter 'print'")
        ipt = input()
        if ipt == "print":
            print(temp_data)
        elif -1 <= int(ipt) and int(ipt) <= len(temp_data) - 1:
            return int(ipt)


def return_back(data, used_keys):
    used_keys = copy.deepcopy(used_keys)[:-1]
    res = copy.deepcopy(data)
    for i in used_keys:
        res = res[i]
    main(data, temp_data, used_keys)

    return res, used_keys


def main(data, temp_data, used_keys):
    print(used_keys, temp_data)
    print("Currently your depth is:", len(used_keys))

    if isinstance(temp_data, list):
        index = get_ipt_list(temp_data)
        if index == -1:
            return_back(data, used_keys)
        else:
            used_keys.append(index)
            temp_data = copy.deepcopy(temp_data[index])
            main(data, temp_data, used_keys)
    elif isinstance(temp_data, dict):
        ipt = get_ipt_dict(temp_data)
        if ipt == -1:
            return_back(data, used_keys)

        used_keys.append(ipt)
        temp_data = temp_data[ipt]
        main(data, temp_data, used_keys)
    else:
        print(temp_data)
        ipt = input("You have reached the dead end! Enter '-1' to go back")
        if ipt == '-1':
            return_back(data, used_keys)
        main(data, temp_data, used_keys)



with open("account.json") as json_file:
    data = json.load(json_file)
depth = 0
used_keys = []
temp_data = copy.deepcopy(data)
main(data, temp_data, used_keys)
