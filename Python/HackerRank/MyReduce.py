#from __future__ import print_function
# from fractions import Fraction
#
# def product(fracs):
#     #print (fracs[0])
#     t = reduce(lambda x,y : x*y,fracs)
#     return t.numerator, t.denominator
#
#
#
#
#
# if __name__ == '__main__':
#     fracs = []
#     for _ in range(input()):
#         fracs.append(Fraction(*map(int, raw_input().split())))
#     result = product(fracs)
#     print(*result)


l = [1,2,3,4,5]

print reduce(lambda x,y: x*y,l)