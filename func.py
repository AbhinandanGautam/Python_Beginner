'''
built-in function
'''
# int() , float() , eval() , len() , max() , min() etc

'''
Modules
'''
import math as m # import all function of math
# from math import cos, sin, pi (import some function from math)
# from math import * (import all function and we don't have to use math.__)
# print(dir(math)) to see all function of math
print(m.pi)

'''
user-defined function
'''
def greet(name):
    print('Good Morning, ',name)

greet(input())


def sum_of_list(a):
    return sum(a)

m = [1,2,3,4]
print(sum_of_list(m))