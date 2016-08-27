from math import sqrt
import os



def solve_ribuit(a, b, c):
    '''
    :param a, b, c: 3 integer numbers
    :return: tuple(2 solutions to ax^2+bx+c) or None if no solution
    test1: solve_ribuit(1, -3, -4) -> (4.0, -1.0)
    test2: solve_ribuit(1, -3, 4) -> None
    '''
    sol = b*b - 4*a*c
    if sol >= 0:
        sqrt_sol = sqrt(sol)
        final_sol = (-1*b + sqrt_sol)/2*a, (-1*b + -1*sqrt_sol)/2*a

    else:
        final_sol = None

    return final_sol


def str_start_end_same(s, n):
    '''
    :param s: string
    :param n: integer
    :return: True if n first chars are equal to last n chars, else False
    test1:  str_start_end_same('abcdabc', 3) -> True
    test2: str_start_end_same('abcdabd', 1) -> False
    '''
    return s[:n] == s[-n:]


def get_ribua_nam(a, b):
    '''
    :param a: row number
    :param b: column number
    :return: recursively calculated sum of previous column and previous row
    test1:   get_ribua_nam(5, 5) -> 70
    test2:   get_ribua_nam(5, 4) -> 35
    '''
    if a == 1 or b == 1:
        return 1
    return get_ribua_nam(a-1, b) + get_ribua_nam(a, b-1)


def how_is_string(s):
    '''
    :param s: string
    :return: 1 if chars are digits or letters,
             2 if all the chars are digits,
             3 if all the chars are letters
             0 otherwise
    test1: how_is_string('abcd') -> 3
    test2: how_is_string('1234') -> 2
    test3: how_is_string('12b4') -> 1
    test4: how_is_string('1!b4') -> 0
    '''
    ret = 0
    if s.isdigit():
        ret = 2
    elif s.isalpha():
        ret = 3
    elif s.isalnum():
        ret = 1

    return ret


def str_only_letters(s):
    '''
    :param s: string
    :return: return a new string with letters only(spaces not accounted as letters)
    test1: str_only_letters("this is a nice string ( 'hhhhh' ), but we want it with only letters") ->
                                                                    thisisanicestringhhhhhbutwewantitwithonlyletters
    '''
    if "," in s:
        s.replace("'", " ")
    final_string = ""
    for letter in s:
        if letter.isalpha():
            final_string = final_string + letter

    return final_string


def process_line(line):
    signs = ['(', ',', '\n', '.', ')', '$', '#']
    signs_roles = {ord(c): None for c in signs}
    line = line.translate(signs_roles)
    list_of_words = list(line.split(" "))
    return list_of_words


def count_words(count_dict, word_list):
    blacklist_set = {'and', 'or', 'the', 'to', 'of', 'not', 'in', 'for', 'while', 'if', 'as', 'equal', 'a', 'c', 'it',
                     'is', 'are', 'an', 'also', 'with', ''}

    for word in word_list:
        if word.lower() not in blacklist_set:
            if word not in count_dict:
                count_dict[word] = 1
            else:
                count_dict[word] += 1
    return count_dict


def get_top_used_words_from_file(sFile, n):
    '''
    :param sFile : file name
    :param n: n words with highest frequency
    :return: list of characters with frequency
    test get_top_used_words_from_file('textfile.txt', 3) resturns [('Python', 12), ('language', 5), ('interpreter', 3)]
    '''
    count_dict = dict()

    if os.path.exists(sFile):
        with open(sFile, 'r') as file_to_read:
            lines = file_to_read.readlines()

        for line in lines:
            list_of_words = process_line(line)
            count_dict = count_words(count_dict, list_of_words)

    sorted_dict = sorted(count_dict, key=count_dict.get)

    list_to_return = []
    for x in reversed(range(-n, 0)):
        word = sorted_dict[x]
        list_to_return.append((word, count_dict[word]))

    return list_to_return


def calculate(number1, number2, operator):
    #help function for eval_post_fix
    result = None
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == "*":
        result = number2 * number1
    elif operator == "/":
        result = number1 / number2
    return result


def eval_post_fix(expression):
    '''
    :param : literal post expression
    : return : result if the expression is right 
    tests:
    (eval_post_fix("3 4 + 9 5 - *")) -> 28
    (eval_post_fix("3 4 + 9 A - *")) -> error near A , None
    '''
    operator_list = ["+", "-", "*", "/"]
    stack = []
    expression_list = expression.split(" ")
    for item in expression_list:
        if item.isdigit():
            stack.append(int(item))
        elif item in operator_list:
                number1 = stack.pop()
                number2 = stack.pop()
                result = calculate(number2, number1, item)
                if result != None :
                    stack.append(result)
                else:
                    print ("error near "  + number1 + " and " + number2)
        else:
            print ("error near " + item)
            return
    return stack.pop()


def q7():
    #question 7
    s_females = {1, 2, 3, 4, 11, 12}
    s_males = {5, 6, 7, 8}
    s_all = s_females.union(s_males)
    s_natives = {3, 11, 7, 5}
    s_telaviv = {1, 2, 5, 6}
    s_haifa = {3, 7, 8, 11}
    s_jerusalem = s_all - s_telaviv.union(s_haifa)
    s_males_telaviv = s_telaviv.difference(s_females)
    s_females_telaviv_or_Haifa = s_females.difference(s_jerusalem)
    s_are_males_in_Jerusalem = s_males.issuperset(s_jerusalem.difference(s_females)) and (len(s_jerusalem.difference(s_females)) > 0) #checking if result set is not empty list
    s_are_females_not_natives_in_Jerusalem = (s_jerusalem.difference(s_males)).issubset(s_natives) == False




if __name__ == '__main__':
    # print(solve_ribuit(1, -3, -4))
    # print(str_start_end_same('abcdabd', 1))
    # print(get_ribua_nam(5, 4))
    # print(how_is_string('1!b4'))
    # print(str_only_letters("this is a nice string ( 'hhhhh' ), but we want it with only letters"))
    #print(get_top_used_words_from_file('textfile.txt', 3))
    print(eval_post_fix("3 4 + 9 A - *"))
    print(eval_post_fix("3 4 + 9 5 - *"))
    #print(q7())
