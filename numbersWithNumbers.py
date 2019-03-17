"""
Writing n using n's.
Inspiration: https://codegolf.stackexchange.com/questions/117711/displaying-n-with-n

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 29apr2017
"""


def write(number):
    if number is '0':
        s = ['']*5
        s[0] = '000'
        s[1] = '0 0'
        s[2] = '0 0'
        s[3] = '0 0'
        s[4] = '000'

        return s

    elif number is '1':
        s = ['']*5
        s[0] = ' 1 '
        s[1] = ' 1 '
        s[2] = ' 1 '
        s[3] = ' 1 '
        s[4] = ' 1 '

        return s

    elif number is '2':
        s = ['']*5
        s[0] = '222'
        s[1] = '  2'
        s[2] = '222'
        s[3] = '2  '
        s[4] = '222'

        return s

    elif number is '3':
        s = ['']*5
        s[0] = '333'
        s[1] = '  3'
        s[2] = '333'
        s[3] = '  3'
        s[4] = '333'

        return s

    elif number is '4':
        s = ['']*5
        s[0] = '4 4'
        s[1] = '4 4'
        s[2] = '444'
        s[3] = '  4'
        s[4] = '  4'

        return s

    elif number is '5':
        s = ['']*5
        s[0] = '555'
        s[1] = '5  '
        s[2] = '555'
        s[3] = '  5'
        s[4] = '555'

        return s

    elif number is '6':
        s = ['']*5
        s[0] = '666'
        s[1] = '6  '
        s[2] = '666'
        s[3] = '6 6'
        s[4] = '666'

        return s

    elif number is '7':
        s = ['']*5
        s[0] = '777'
        s[1] = '  7'
        s[2] = '  7'
        s[3] = '  7'
        s[4] = '  7'

        return s

    elif number is '8':
        s = ['']*5
        s[0] = '888'
        s[1] = '8 8'
        s[2] = '888'
        s[3] = '8 8'
        s[4] = '888'

        return s

    elif number is '9':
        s = ['']*5
        s[0] = '999'
        s[1] = '9 9'
        s[2] = '999'
        s[3] = '  9'
        s[4] = '999'

        return s


def write_number(number):
    s = ''

    for i in range(5):
        for j in number:
            s += write(j)[i]
            s += '  '
        s += '\n'

    print(s)


while True:
    my_string = input("Input number: ")
    print('')
    write_number(my_string)
