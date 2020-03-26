from collections.abc import Hashable


class NotCorrectInputTypeError(Exception):
    def __init__(self, ipt):
        self.ipt = ipt
        self.type = type(int)


class IptWithDifferentElementsError(Exception):
    def __init__(self, normal_type, element_type):
        self.normal_type = normal_type
        self.element_type = element_type


class UnhashableElemInsideError(Exception):
    def __init__(self, element):
        self.element = element


def is_sorted(ipt):
    """ (list/tuple/string) -> bool
        This function receives list or tuple or string(It throws an error if
    the input is of other type)
        If not all the elements inside input are of the same type,
    raises an error.
        Returns True if all the elements are in ascending order,
    False otherwise
    """
    if type(ipt) not in [list, tuple]:
        raise NotCorrectInputTypeError(ipt)

    if ipt:
        elem_type = type(ipt[0])

    for i in range(1, len(ipt)):
        if not isinstance(ipt[i], Hashable):
            raise UnhashableElemInsideError(ipt[i])
        if not isinstance(ipt[i-1], Hashable):
            raise UnhashableElemInsideError(ipt[i])
        if not isinstance(ipt[i], elem_type):
            raise IptWithDifferentElementsError(elem_type, type(ipt[i]))
        if ipt[i] < ipt[i - 1]:
            return False
    return True
