from addition import *
from multiplication import *
from subtraction import *
from divition import *
from square02 import *
from power import *
from remaining import *
from floor_divition import *
from scnd_grade import *

def main():
    print('SYMBOLS: + - * / sqrt')
    print('1) +')
    print('2) -')
    print('3) *')
    print('4) /')
    print('5) sqrt')
    print('6) **')
    print('7) //')
    print('8) 2nd grade')


    choosing = input('Choose one of the following symbols: ')
    
    if choosing == '2nd grade':
        add_a = input('Add a: ')
        add_b = input('Add b: ')
        add_c = input('Add c: ')
        scnd_grade(add_a, add_b, add_c)
        exit()

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
    
    elif choosing == '**':
        power(n_1, n_2)
    
    elif choosing == '//':
        floor(n_1, n_2)



main()