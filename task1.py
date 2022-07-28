from fractions import Fraction
def rational_number():
    lst = list(map(int, input("Введите 4 числа через пробел:\n").split()))
    a=lst[0] 
    b = lst[1]
    c = lst[2]
    d = lst[3]
    a = Fraction(a, b) # a =  - рациональное число
    b = Fraction(c, d) # b =  - рациональное число
    print(a,b)
    return a,b
def sum_rational_num(a,b,c,d):
    sum_num = Fraction(a, b) + Fraction(c, d) 
    return sum_num
def minus_rational_num(a,b,c,d):    
    minus_num = Fraction(a, b) - Fraction(c, d)  
    return minus_num
def multiply_rational_num(a,b,c,d):
    mult= Fraction(a, b) * Fraction(c, d)
    return mult
def division_rational_num(a,b,c,d):  
    divis = Fraction(a, b) / Fraction(c, d)
    return divis

#rational_number()
lst = list(map(int, input("Введите 4 числа через пробел:\n").split()))
a =lst[0] 
b = lst[1]
c = lst[2]
d = lst[3]
print(sum_rational_num(a,b,c,d))    
print(minus_rational_num(a,b,c,d))
print(multiply_rational_num(a,b,c,d))
print(division_rational_num(a,b,c,d))