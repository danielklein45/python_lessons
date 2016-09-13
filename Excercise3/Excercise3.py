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


# Question 2 - part 1
def f321_algorithm(n):
    if n % 2 == 0:
        z = n // 2
    else:
        z = n * 3 + 1
    return z


def list321(n):

    def f321_generator(n):
        nonlocal number_of_steps
        if n == 1:
            yield 1
            number_of_steps += 1
            return
        yield n
        number_of_steps += 1
        z = f321_algorithm(n)
        for w in f321_generator(z):
            yield w

    number_of_steps = 0
    g = f321_generator(n)
    for x in g:
        pass
    return number_of_steps


# Question 2 - part 2
def f321_with_cache():
    dict_nums = {}
    number_of_steps = 0

    def cache321(n):
        nonlocal dict_nums
        nonlocal number_of_steps

        # reached the end of algorithm
        if n == 1:
            number_of_steps += 1
            return 0
        # check if n in cache
        if n in dict_nums:
            return dict_nums[n]
        # n is not in cache
        else:
            z = f321_algorithm(n)
            dict_nums[n] = cache321(z)
            number_of_steps += 1

        return number_of_steps

    # return the dictionary
    cache321.get_cache = dict_nums
    return cache321


# Question 3
ls_none = None  # global variable


def check_none_wrapper(func):
    def wrf(*args, **kwargs):
        ls_none = []
        print(args, kwargs)
        for idx, arg in enumerate(args):
            if arg is None:
                print("Positional arg no {0} is None".format(idx))
                ls_none.append(idx)
        for idx, arg in enumerate(kwargs):
            if kwargs[arg] is None:
                print("keyword arg ==> {0} is None".format(arg))
                ls_none.append(arg)
        print("ls_none = {0}".format(ls_none))
        _result = func(*args, **kwargs)
        return _result

    return wrf


def add3(a=None, b=None, c=None):
    if a is None:
        a = 0
    if b is None:
        b = 0
    if c is None:
        c = 0
    return a+b+c


def test_check_none():
    for k in range(1, 5):
        if k == 1:
            add3_with_check = check_none_wrapper(add3)
            r1 = add3_with_check(1, 2, 3)
        if k == 2:
            add3_with_check = check_none_wrapper(add3)
            r2 = add3_with_check(1, 2, None)
        if k == 3:
            add3_with_check = check_none_wrapper(add3)
            r3 = add3_with_check(1, b=None)
        if k == 4:
            add3_with_check = check_none_wrapper(add3)
            r4 = add3_with_check(1, None, c=None)
    return (r1, r2, r3, r4)


# Bonus
def test_do_calc():
    for k in range(1, 5):
        if k == 1:
            r1 = do_calc(1, 7, 4)
        if k == 2:
            r2 = do_calc(2, 7, 4)
        if k == 3:
            r3 = do_calc(3, 7, 4)
        if k == 4:
            r4 = do_calc(4, 7, 4)

    return (r1, r2, r3, r4)


def do_calc(k, a, b):
    DictCases = {1: lambda a, b: a + b,
                 2: lambda a, b: a - b,
                 3: lambda a, b: a * b,
                 4: lambda a, b: a / b,
                 'default': lambda x: a + b}
    func = sc_switch(k, DictCases)
    return func(a, b)


def sc_switch(k, zDictCases):
    """
    simulate switch statement with cases in Dict
    'default' is used if case was not found
    if 'default is not defined in
    :param zDictCases: dictionary with cases
    :param k: selected case
    :return:
    """
    if k in zDictCases:
        fn = zDictCases[k]
        return fn

    if 'default' in zDictCases:
        fn = zDictCases['default']
        return fn

    return None


if __name__ == '__main__':
    # test question1
    print("Question1")
    print(test1_map_pl())
    print(test2_map_pl())
    print(test3_map_pl())
    print(test4_map_pl(7))
    print("Question2 - part1")
    # test question2 - part 1 - return 17
    print(list321(7))
    # test question2 - part 2
    print("Question2 - part2")
    f321 = f321_with_cache()
    # print 10 and create cache
    print(f321(13))
    d = f321.get_cache
    print(sorted(d.items()))
    # print 17 and append cache
    print(f321(7))
    d = f321.get_cache
    print(sorted(d.items()))
    print("Question3")
    print(test_check_none())
    print("Bonus")
    print(test_do_calc())


