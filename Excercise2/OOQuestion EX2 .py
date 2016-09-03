# -------------------------------------------------------------------------------
# Name:        OO class ex2
# Purpose:     EX2
#
# Author:      Daniel Klein 301344891 Pavel Jirnov 321728131
#
# Created:     3.9.2016
#-------------------------------------------------------------------------------


class Question:
    ''' base class for different kinds of Questions
    '''
    ID_ratz = 0 #  class\static variable

    def __init__(self, q_txt, answer_type, **kw):
        print('CTOR Question' + repr(kw))
        super().__init__(**kw)
        Question.ID_ratz += 1
        self.ID = Question.ID_ratz
        self.q_txt = q_txt
        self.user_answer = None
        self.answer_type = answer_type

    def __repr__ (self):
        sFormat = 'Question( {0!r} )'
        s = sFormat.format(self.q_txt)
        return s
    
    def __str__(self):
        sFormat = 'Q({0:^3d}) {1:s}'
        s = sFormat.format(self.ID, self.q_txt)
        return s
    
    def show_question(self):
        ''' show_question (self):
        can overwrite         with Mixin !!!
        '''
        print(self)

    # can overwrite with Mixin
    def get_input(self):
        ''' get_input(self)
            can overwrite with Mixin !!!
            :return: user answer (can be empty string ==> user did not enter anything
            '''
        return input("Enter your answer : ")

    def get_answer(self):
        ''' get_answer (self)
            can overwrite with Mixin !!!
        '''
        a = self.get_input() # get input from user
        a = convert_answer_type(a, self.answer_type)
        self.user_answer = a
        return self.user_answer

    def response(self):
        ''' response (self)
            can overwrite with Mixin !!!
            show response to user
        '''
        if self.user_answer:
            print('your answer is: ' + str(self.user_answer))
        else:
            print('No answer')

    def ask_question(self):
        ''' ask_question(self):
        Main Template function
        '''
        print('\n')
        self.show_question()
        self.get_answer()
        self.response()
        return self.user_answer


def convert_answer_type( answer, ans_type ):
    '''
    ans_type = int | float | str | [type] | ant_type | any_function
    answer is a string => convert  it ito type
    :return: new answer or None
    '''
    if ans_type is str: return answer
    try:
        if isinstance(ans_type,  list):
            ls1 = answer.split()
            ls2 = list(map(ans_type[0], ls1))
            return ls2
        return ans_type(answer)

    except ValueError as e:
        print('Error !!! ' + str(e))
        return None


class Q_Possible_Answers(Question):
    '''  class Q_Possible_Answers ( Question )
    has some possibe answers
    '''

    def __init__(self, list_answers, **kw):
        print('CTOR Q_Possible_Answers' + repr(kw))
        super().__init__(**kw)
        self.list_answers = list_answers

    def __repr__(self):
        sFormat = 'Q_Possible_Answers( {0!r} , {1!r} )'
        s = sFormat.format(self.q_txt, self.list_answers)
        return s

    # YOU - use the following method: show_possible_answers
    def show_question(self):
        print(self)
        self.show_possible_answers()

    # You
    def show_possible_answers(self):
        for idx, answer in enumerate(self.list_answers):
            print(str(idx+1) + ": " + answer)

    def response(self):
        if not self.user_answer:
            print('No Answer')
            return
        k = self.user_answer
        try:
            k = self.user_answer
            if k:
                ans = self.list_answers[k - 1]
            else:
                ans = ' ILLEGAL'
        except IndexError as e:
            print('IndexError: ' + str(e))
            print('!!! Problem = answer must be in range')
            return

        print("Your Answer is: " + ans)


class Q_Possible_Answers_Multi(Q_Possible_Answers):
    '''  class Q_Possible_Answers_Multi ( Question )
        has some possibe answers
    '''
    def __init__(self, **kw):
        print('CTOR Q_Possible_Answers_Multi' + repr(kw))
        super().__init__(**kw)

    def response(self):
        ans = ""
        if not self.user_answer:
            print('No Answer')
            return
        k = self.user_answer
        try:
            k = self.user_answer
            for answer in k:
                if answer > 0 or answer < len(self.list_answers):
                    ans = self.user_answer
                else:
                    ans = ' ILLEGAL'
        except IndexError as e:
            print('IndexError: ' + str(e))
            print('!!! Problem = answer must be in range')
            return

        print("Your Answer is: " + str(ans))

 
#
#-------------   Check Mixins   --------------------
#
#

class Check_Mixin():
    ''' Check_Mixin is an abstract data type '''
    def __init__(self, right_answer, grade_value, **kw):
        print('CTOR Check_Mixin' + repr(kw))
        super().__init__(**kw)
        self.right_answer = right_answer
        self._grade_value = grade_value
        self._grade_user = None

    def get_grade_user(self):
        return self._grade_user

    grade_user = property(get_grade_user)

    def get_grade_value(self):
        return self._grade_value

    # YOU - define grade_value as property
    grade_value = property(get_grade_value)

    def check(self):
        return self.user_answer != None

    def compute_grade(self):
        self._grade_user = 0
        return 0


class Check_EQ_Mixin (Check_Mixin):
    def __init__(self, **kw):
        print('CTOR Check_Mixin' + repr(kw))
        super().__init__(**kw)

    # YOU check if the value is equal to right_answer
    def check(self):
        return self.user_answer == self.right_answer

    def compute_grade(self):
        # YOU compute grade – if user_answer is equalt to right_answer then 
        # the  grade is grade_value otherwise 0 
        # set calculated grade to grade_user
        if self.check():
            self._grade_user = self._grade_value
        else:
            self._grade_user = 0


class Check_Range_Mixin(Check_Mixin):
    # YOU complete CTOR = constructor
    def __init__(self, range_from, range_to, **kw):
        print('CTOR Check_Range_Mixin')
        self.range_from = range_from
        self.range_to = range_to
        super().__init__(**kw)

    def check(self):
        # YOU – return True if user_answer is in range
        return self.range_from < self.user_answer or self.range_to > self.user_answer
        
    def compute_grade(self):
        # YOU – if user answer is exactly like right_answer then the grade is grade_value
        # if within the range but not exactly right_answer then subtract 2 points – otherwise 0
        if self.right_answer == self.user_answer:
            self._grade_user = self._grade_value
        elif self.check():
            self._grade_user = self._grade_value - 2
        else:
            self._grade_user = 0


# Q_Possible_Answers
class Check_American_Mixin(Check_EQ_Mixin):
    def __init__(self, **kw):
        print('Check_American_Mixin' + repr(kw))
        super().__init__(**kw)

    def compute_grade(self):
        # YOU if user_answer is equal to the right_answer then return grade_value
        # otherwise subtract (1 divided by the length)  * grade_value
        # do not forget tp set grade_user to the computed grade
        if self.user_answer == self.right_answer:
            self._grade_user = self._grade_value
        else:
            self._grade_user = self._grade_value - (1/len(self.list_answers) * self._grade_value)


class Check_American_Multi_Mixin(Check_Mixin):
    def __init__(self, **kw):
        print('CTOR Check_American_Multi_Mixin' + repr(kw))
        super().__init__(**kw)

    def compute_grade(self):
        self._grade_user = 0
        for answer in self.user_answer:
            if answer in self.right_answer:
                self._grade_user += self._grade_value/len(self.right_answer)

#
#
#-------------   Test Questions   --------------------
#
#


class Test_Q_Eq (Check_EQ_Mixin, Question):
    '''q_txt=<str> , right_answer= <int>, grade_value=<int>'''
    # YOU
    def __init__(self, **kw):
        print('CTOR TEST_Q_Eq')
        super().__init__(**kw)


class Test_Q_Range(Check_Range_Mixin, Question):
    def __init__(self, **kw):
        print('CTOR Test_Q_Range' + repr(kw))
        super().__init__(**kw)


# YOU
class Test_Q_American(Check_American_Mixin, Q_Possible_Answers):
    def __init__(self, **kw):
        print('CTOR Test__American' + repr(kw))
        super().__init__(**kw)


class Test_Q_American_Multi(Check_American_Multi_Mixin, Q_Possible_Answers_Multi):
    def __init__(self, **kw):
        print('CTOR Test__American_Multi' + repr(kw))
        super().__init__(**kw)

 
#
#
# -------------   Sheelon Test Classes   --------------------
#
#

class Sheelon:

    def __init__(self, *list_Qs):
        self.list_Qs = list_Qs

    def run_sheelon(self):
        for  q in self.list_Qs:
            q.ask_question()

    def show (self):
        for q in self.list_Qs:
            print(str(q) + ' => ' + str(q.user_answer))

    def do(self):
        self.run_sheelon()
        self.show()

    # You
    def __call__(self):
        self.do()

    # YOU
    def __len__(self):
        return len(self.list_Qs)


class Sheelon_Test(Sheelon):
            
    def show(self):
        final_grade = 0

        for q in self.list_Qs:
            q.compute_grade()

            if q.user_answer is not None:
                final_grade += q.grade_user
                sFormat = '{0} : {1}  grade= {2:2.0f} out of= {3}'
                s = sFormat.format(q.ID, q.user_answer, q.grade_user, q.grade_value)
                print(s)
            else:
                print(str(q) + ' ==> No user answer')

        print('Final Grade: ' + str(final_grade))


def test():
    global q1, q2, q3, q4, q5, q6, q7, q8, q9, test1, sheelon1

    print('q1')
    q1 = Question(q_txt='What is your name ?', answer_type=str)

    print('q2')
    q2 = Question(q_txt='What is your address ?', answer_type=str)

    print('q3')
    ls1_answers = ['Haifa', 'Aco', 'TelAviv', 'Jerusalem']
    q3 = Q_Possible_Answers(q_txt='Which is your loved city?', list_answers=ls1_answers, answer_type=int)

    print('q4')
    q4 = Test_Q_Eq(q_txt="How many days in the six days war?",
                     right_answer= 6, grade_value=10, answer_type=int)

    print('q5')
    q5 = Test_Q_American(q_txt='Which is the capital of Israel?', list_answers=ls1_answers,
                         right_answer= 4, grade_value=12, answer_type=int)

    print('q6')
    q6 = Test_Q_Range(q_txt='What is the value of PI?', range_from=3.14, range_to=3.15,
                      right_answer=3.1417, grade_value=8, answer_type=float)

    print('q7')
    ls2_answers = ['Haifa', 'Aco', 'TelAviv', 'Jerusalem', 'Eilat', 'Arad', 'Gedera']
    q7 = Test_Q_American_Multi(q_txt='Which are big cities?', list_answers=ls2_answers, grade_value=12,
                               right_answer=[1,3,4], answer_type=[int])

    sheelon1 = Sheelon(q1, q2, q3)
    sheelon1()

    test1 = Sheelon_Test(q4, q5, q6, q7)
    test1()


if __name__ == '__main__':
    # write tests in main
    test()
    pass
