class IgorDetectedException(BaseException):
    pass


def raise_func(dct):
    if "Igor" in dct:
        raise IgorDetectedException
    else:
        raise KeyError('The wrong key')


def except_func():
    try:
        ipt = input("Enter Igor as a key and his surname as a value,"
                    "with a space as separator: ")
        dct = dict()
        dct[ipt.split()[0]] = ipt.split()[1]
        raise_func(dct)
    except KeyError as e:
        print(e)
        print('wrong key')
    except IndexError as e:
        print(e)
        print("wrong Index")
    except IgorDetectedException as e:
        print(e)
        print("Igor detected!")
    except:
        print("Unknown yet exception")


if __name__ == '__main__':
    except_func()
