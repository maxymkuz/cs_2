import json
import copy


def get_ipt_dict(data):
    """
    If input is a dict:
    :param data:
    :return:
    """
    keys = [i for i in data]
    for i in range(len(keys)):
        print(str(i+1) + ". ", keys[i])
    print("\nA) Enter one of the KEYS, listed above to dive into")
    print("B) Enter '-1' to go one level back")
    inp = input("C) Enter 'print' to print current dictionary: ")
    while True:
        if inp == '-1':
            return -1
        if inp in keys or inp.lower() == 'print':
            return inp
        inp = input("Enter VALID key, listed above: ")


def get_ipt_list(temp_data):
    """
    If input is a list:
    :param temp_data:
    :return:
    """
    while True:
        try:
            print("There are "  + str(len(temp_data)) + " items in this list")
            print("Choose an index of a list item, you want to\
 dive into in range: [0, " + str(len(temp_data) - 1) + "]")
            print("To go back one level, type '-1'")
            print("To print the whole list, enter 'print'")
            ipt = input()
            if ipt.lower() == "print":
                print("\n", temp_data, "\n")
            elif -1 <= int(ipt) and int(ipt) <= len(temp_data) - 1:
                return int(ipt)
        except:
            continue


def return_back(data, used_keys):
    """
    Returns one level up
    :param data:
    :param used_keys:
    :return:
    """
    used_keys = copy.deepcopy(used_keys)[:-1]
    res = copy.deepcopy(data)
    for i in used_keys:
        res = res[i]
    main(data, res, used_keys)

    # return res, used_keys


def main(data, temp_data, used_keys):
    # print(used_keys, temp_data)
    print("\nCurrently your depth is:", len(used_keys))

    if isinstance(temp_data, list):
        index = get_ipt_list(temp_data)
        if index == -1:
            return_back(data, used_keys)
        else:
            used_keys.append(index)
            main(data, copy.deepcopy(temp_data[index]), used_keys)
    elif isinstance(temp_data, dict):
        ipt = get_ipt_dict(temp_data)
        if ipt == -1:
            return_back(data, used_keys)
        elif ipt.lower() == "print":
            print(temp_data)
        else:
            used_keys.append(ipt)
            main(data, temp_data[ipt], used_keys)
    else:
        print("\n", temp_data, "\n")
        while True:
            ipt = input("You have reached the dead end! Enter '-1' to go back: ")
            if ipt == '-1':
                return_back(data, used_keys)
        main(data, temp_data, used_keys)


def welcome():
    with open("account.json") as json_file:
        data = json.load(json_file)
    print("Welcome! This module will help you navigate through any JSON")
    print("file  in a simple way. Just follow the instructions:\n")
    main(data, copy.deepcopy(data), [])

if __name__ == '__main__':
    welcome()
