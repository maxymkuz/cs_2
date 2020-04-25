import ctypes

n_12 = ctypes.c_int(12)
n_14 = ctypes.c_int(11)

arr = (ctypes.py_object * 5)()
arr[0] = 11


class Multiset:
    """Multiset() produces a newly constructed emptymulti
    set. __init__ : None -> Multiset
    """

    def __init__(self): def

    empty(
        self):  # self.empty() produces True if self is empty.# empty: Multiset -> Booldef contains (self, value):
    # value in self produces True if
    # value is an item in self.# contains : Multiset Any -> Bool
