#-------------------------------------------------------------------------------
# Name:         ListLast
# Purpose:      lLInked List with pointer to last
# Author:       Dr Shimon Cohen
# Created:      June 2016
# Copyright:    (c) Shimon 2016
#
# TODO:  docu... (for class: define Cyclic-Queue
#-------------------------------------------------------------------------------

import copy


class ListLast():

    def __init__(self, item=None):
        # constructor
        self.first = None
        self.last = None
        self.n = 0

        if item == None: return

        if isinstance(item, ListLast):
            self.extend(item)
            return

        if isinstance(item, list):
            self.add_list(item)
            return

        # any other type
        self.push_first(item)

    def __str__(self):
        s = '$ '
        for p in self.gen_on_link4():
            #print(p, s)
            if len(s) > 2 :
                s += ', ' + str(p.val)
            else: s += str(p.val)
        s += ' $'
        return s

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.n

    def __bool__(self):
        return self.n == 0

    def __copy__(self):
        pLL = ListLast()
        pLL.extend(self)
        return pLL

    def __getitem__(self, k):
        if not isinstance(k, int):
            raise TypeError
        if k < 0 or k >= self.n:
            raise IndexError
        val = self.find_k_link(k).val
        if val is None:
            raise KeyError
        return val

    def __iadd__(self, item):
        if isinstance(item, (ListLast, list)):
            if type(item) == list:
                item = ListLast(item)
            self.extend(item)
        else:
            self.push_last(item)
        return self

    def __setitem__(self, k, v):
        self.find_k_link(k).val = v

    def __contains__(self, item):
        if self.find_link(item):
            return True
        return False

    def push_to_empty(self, p):
        self.first = p
        self.last = p

    def find_link(self, val):
        for p in self.gen_on_link4():
            if p.val == val: return p
        return None

    def find_k_link(self, k):
        p = self.first
        while k:
            if not p: return None
            p = p.next
            k -= 1
        return p

    def push_first(self, item):
        p = Link4_ListLast(item)
        if self.first == None:
            self.push_to_empty(p)
            return

        p.next = self.first
        self.first = p

    def push_last(self, item):
        p = Link4_ListLast(item)
        if self.first == None:
            self.push_to_empty(p)
            return

        pLast = self.last
        pLast.next = p
        self.last = p

    def add_list(self, ls):
        ''' add_list(self, ls)
        add normal list at the end of ListLast
        '''
        for x in ls:
            self.push_last(x)
            self.n += 1

    def gen_on_link4(self):
        p = self.first
        while p :
            yield p
            p = p.next

    def extend(self, ls_list_last):
        if not ls_list_last: return self

        if self.first:
            pLast = self.last
            pLast.next = ls_list_last.first
        else:
            self.first = ls_list_last.first
            self.last = ls_list_last.last
        return self

    def go_visit(self, obj_visitor):
        return obj_visitor.go_visit(self)


    def genLL(self):
        k = 0
        current = self.first
        while k < self.n:
            yield current
            k += 1
            current = current.next

    def genLL_sum (self, n):
        k = 0
        sum = 0
        current = self.first
        while k < self.n:
            if current.val > n:
                sum += current.val
                yield sum
            k += 1
            current = current.next


class ListLastT(ListLast):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.k = 0
        self.iter = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if self.k >= self.n:
            raise StopIteration
        self.k += 1
        current = self.iter
        self.iter = self.iter.next
        return current


class ListLast_Iter():
    def __init__(self, objLL):
        self.objLL = objLL
        self.k = 0

    def __iter__(self):
        self.k = 0
        return self

    def __next__(self):
        if self.k >= self.objLL.n:
            raise StopIteration
        val = self.objLL[self.k]
        self.k += 1
        return val


class Link4_ListLast():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, Link4_ListLast):
            return self.val == other.val
        if isinstance(other, int):
            return self.val == other
        return False

    def __lt__(self, other):
        if isinstance(other, Link4_ListLast):
            return self.val < other.val
        if isinstance(other, int):
            return self.val < other
        return False


class VisitorLL():
    def __init__(self):
        self.dict_nums = {}

    def __call__(self, n=None):
        return self.dict_nums

    def go_visit(self, LL):
        for item in LL:
            counter = 0
            if item not in self.dict_nums:
                for x in LL.genLL():
                    if x == item:
                        counter += 1
                self.dict_nums[item] = counter

class VisitorLL_up ():
    def __init__(self):
        self.counter = 0

    def __call__(self, n=None):
        return self.counter

    def go_visit(self, LL):
        prev = None
        for x in LL.genLL():
            if prev is not None and prev < x:
                self.counter += 1
            prev = x



#
# ------------------------------------------------
#

lsL1 = ListLast([4, 5, 6, 7, 5, 4, 5, 5, 7, 6])
lsT1 = ListLastT([8, 7, 6, 8, 5, 6, 3, 6])


def test1():
    def countN(obj, n):
        k = 0
        for x in obj:
            if x == n: k += 1
        return k

    r1 = countN(lsL1, 5)  # use __getitem__
    r2 = countN(lsT1, 6)  # use __iter__
    r3 = countN(lsL1.genLL(), 4)
    r4 = countN(lsT1.genLL(), 3)

    r5 = list(lsL1.genLL_sum(5))

    objV1 = VisitorLL()  # return counts of each number
    lsL1.go_visit(objV1)
    objV1_dict = objV1()
    r6 = list(objV1_dict.items())  # list of pairs

    objV2 = VisitorLL_up()  # count => prev < current
    lsL1.go_visit(objV2)
    r7 = objV2()  # return int

    return (r1, r2, r3, r4, r5, r6, r7)

compL1 = [3, 5, 7, 8, 9, 5, 6, 7, 4, 3]
compL2 = [1, 4, 5, 8, 3, 6, 9, 3, 5, 9]


def test2():
    r1 = [x for x in compL1 if x > 5]
    r2 = [x+y for x, y in zip(compL1, compL2) if y > 5]
    r3 = [x * x if x > 5 else 0 for x in compL1]
    r4 = [x * x if x > 5 else 0 for x in compL1 if x > 3]
    r5 = [(x, y) for x in compL1 if x > 7 for y in compL2 if y > 7]
    r6 = [[b + a for a in compL1 if a < 4] for b in compL2 if b < 4]
    r6 = map(list, r6)
    rs = [r1, r2, r3, r4, r5, r6]
    ls_rs = list(list(ls) for ls in rs)
    for ls in ls_rs: print(ls)
    return ls_rs


''' -----------------   ANSWERS  -------------
[
[7, 8, 9, 6, 7]
[16, 11, 15, 12]
[0, 0, 49, 64, 81, 0, 36, 49, 0, 0]
[0, 49, 64, 81, 0, 36, 49, 0]
[(8, 8), (8, 9), (8, 9), (9, 8), (9, 9), (9, 9)]
[[4, 4], [6, 6], [6, 6]]
]
'''

if __name__ == '__main__':
    print(test1())
    print(test2())








