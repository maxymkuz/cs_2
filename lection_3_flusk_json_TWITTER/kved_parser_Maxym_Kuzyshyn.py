import json
import pprint


def get_input():
    """
    Receives and returns an input from user
    :return: str
    """
    n = input("Please, enter classCode")
    return n


def main(ipt):
    """
    search through the kved.json file and returning
    dict with essential stuff
    :param ipt: str
    :return: dict
    """
    with open("kved.json", 'r', encoding="utf-8") as f:
        dct = {}
        file = json.load(f)
        for sec in file['sections'][0]:
            for i in sec["divisions"]:
                for group in i['groups']:
                    for clas_s in group['classes']:
                        if clas_s['classCode'] == ipt:
                            dct['name'] = clas_s['className']
                            dct['type'] = 'class'
                            dct['parent'] = {
                                "name": group['groupName'],
                                "type": "group",
                                "num_children": len(group['classes']),
                                "parent": {
                                    "name": i['divisionName'],
                                    "type": "division",
                                    "num_children": len(i['groups']),
                                    "parent": {
                                        "name": sec["sectionName"],
                                        "type": "section",
                                        "num_children": len(sec["divisions"])
                                    }}}
                            return dct
    print("Your inpput parameters are wrong or there does't exist such class")


if __name__ == '__main__':
    ipt = get_input()
    with open('kved_results.json', 'w') as f:
        json.dump(main(ipt), f, ensure_ascii=False, indent=4)
