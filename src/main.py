from addition import *
from multiplication import *
from subtraction import *
from divition import *
from square02 import *



def main():
    print('SYMBOLS: + - * / sqrt')
    print('1) +')
    print('2) -')
    print('3) *')
    print('4) /')
    print('5) sqrt')



    choosing = input('Choose one of the following symbols: ')

    n_1 = int(input('Add a number: '))
    n_2 = int(input('Add anothet one number: '))

    if choosing == '+':
        addition(n_1, n_2)
    elif choosing == '-':
        subtraction(n_1, n_2)
    elif choosing == '*':
        multiplication(n_1, n_2)
    elif choosing == '/':
        divition(n_1, n_2)
    elif choosing == 'sqrt':
        square(n_1, n_2)

main()