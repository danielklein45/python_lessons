# Question 1
def map_pl(ls_in, fn_check, fn_compute):

    def do_map_pl(ls_in, fn_check, fn_compute):
        items_list = list()
        for item in ls_in:
            # item is a list  - need to map inside it
            if type(item) is list:
                new_list = do_map_pl(item, fn_check, fn_compute)
                items_list.append(new_list)
            # need to check the item
            else:
                new_item = item
                if fn_check(item):
                    new_item = fn_compute(item)
                items_list.append(new_item)
        return items_list

    return do_map_pl(ls_in, fn_check, fn_compute)


# Tests for question 1
ls = [2, -3, 4, [-5, 6, -7], 11, [8, -9, 10]]


def test1_map_pl():
    # returns the value:  [ 2, 3, 4, [5, 6, 7 ], 11, [ 8, 9, 10 ]]
    return map_pl(ls, (lambda x: x < 0), (lambda x: 0-x))


def test2_map_pl():
    # returns the value:  [ 2, 0, 4, [ 0, 6, 0 ], 11, [ 8, 0, 10 ] ]
    return map_pl(ls, (lambda x: x < 0), (lambda x: x-x))


def test3_map_pl():
    # return the value: [ 4, 9, 16, [25, 36, 49 ], 11, [ 64, 9, 10 ]]
    return map_pl(ls, (lambda x: abs(x) < 9), (lambda x: x*x))


def test4_map_pl(z):
    # return [4, -6, 8, [-10, 12, -7], 11, [8, -9, 10]]
    return map_pl(ls, (lambda x: abs(x) < z), (lambda x: x+x))


if __name__ == '__main__':
    print(test1_map_pl())
    print(test2_map_pl())
    print(test3_map_pl())
    print(test4_map_pl(7))
