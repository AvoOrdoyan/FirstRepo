#Ex_1
# age = int(input('qani tarekanes? '))
# if age < 18:
#     print('You are under 18')
# else:
#     print('You are over 18')
import time

#Ex_2
# a = float(input('a = '))
# b = float(input('b = '))
# if a * b % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
# x = float(input('x = '))
# y = float(input('y = '))
# if x > y:
#     print(x)
# elif y > x:
#     print(y)
# text = 'hello '
# print(text[1])

# Ex_1
# text = 'hello world '
# print(len(text))
# print(text[0])
# print(text[10])
#
# Ex_1
# Mail = 'av.ordoyan15@mail.ru'
# if '@' and '.' and '.ru' in Mail:
#     print('valid')
# elif '@.' in mail:
#     print('invalid')
# else:
#     print('invalid')

# Heraxosahamar = int(input(' '))
# if len(Heraxosahamar)==12:
#     print('+374' + Heraxosahamar)
# else:
#     print('false')

# a = float(input('a =  ))
# b = float(input('b =  ))
# c = float(input('c =  ))
# D = float(b**2 - 4*a*c)
#
# x = -b / (2 * a)
# x1 = (-b + D ** 0.5) / 2*a
# x2 = (-b - D ** 0.5) / 2*a
# if D == 0:
#     print(x)
# if D < 0:
#     print("False")
# if D > 0:
#     print(x1, x2)

# Homework



# z = ("0 - Exit",
# "1 - Repeat this message",
# "2 - Add one apple to cart (apple price is 1$)",
# "3 - Remove one apple from cart",
# "4 - Add one chocolate to cart (chocolate price is 3$)",
# "5 - Remove one chocolate from cart",
# "6 - Show my cart",
# "7 - Show checkout information",)

# apple = 0
# chocolade = 0

# while True:
#    n = input("n = ")
#    if n == "0":
#        print("Exit")
#        break
#    elif n == "1":
#        print(z, end=" ")
#    elif n == "2":
#        apple += 1
#        print(apple)
#    elif n == "3" and apple > 0:
#        apple -= 1
#        print(apple)
#    elif n == "4":
#        chocolade += 1
#        print(chocolade)
#    elif n == "5" and chocolade > 0:
#        chocolade -= 1
#       print(chocolade)

# Ex_47
# Amis = input('Amis? ')
#if Amis == 'Hunvar':
#    Amis = 1
#elif Amis == 'Petrvar':
#    Amis = 2
#elif Amis == 'Mart':
#    Amis = 3
#elif Amis == 'April':
#    Amis = 4
#elif Amis == 'Mayis':
#    Amis = 5
#elif Amis == 'Hunis':
#    Amis = 6
#elif Amis == 'Hulis':
#    Amis = 7
#elif Amis == 'Ogostos':
#    Amis = 8
#elif Amis == 'September':
#    Amis = 9
#elif Amis == 'Hoktember':
#    Amis = 10
#elif Amis == 'Noyember':
#    Amis = 11
#elif Amis == 'Dektember':
#    Amis = 12
#day = int(input('Or? '))
#if Amis >= 3 and day >= 20:
#    print('Garun')
#elif Amis == 4:
#    print('Garun')
#elif Amis == 4:
#    print('Garun')
#elif Amis == 4:
#   print('Garun')
#elif Amis == 5:
#    print('Garun')
#elif Amis == 6 and day <= 20:

#   print('Amar')
#elif Amis == 6 and day >= 21:
#    print('Amar')
#elif Amis == 7:
#    print('Amar')
#elif Amis == 8:
#    print('Amar')
#elif Amis == 9 and day <= 21:
#    print('Ashun')
#elif Amis == 10:
#    print('Ashun')
#elif Amis == 11:
#    print('Ashun')
#elif Amis == 12 and day <= 20:
#    print('Ashun')
#elif Amis == 12 and day >= 21:
#    print('Dzmer')
#elif Amis == 1:
#    print('Dzmer')
#elif Amis == 2:
#    print('Dzmer')
#elif Amis == 3 and day <= 19:
#    print('Dzmer')
# n = int(input())


# Ex_1
# list_1 = [1, 3, 66, 4, 6, 7, 8, 9, 33, 54, 77, 79]
# list_1.sort(reverse=True)
# for i in list_1:
#     if int(i) % 2 == 0:
#         print(i)
#         break

# Ex_2


# list_1 = []
# list_2 = []
# num_list = [1, 3, 66, 4, 6, 7, 8, 9, 33, 54, 77, 79]
#
# for i in num_list:
#     if int(i) % 2 == 0:
#         list_1.append(i)
#     else:
#         list_2.append(i)
# print(list_1, list_2)



# Ex_4
# l1 = []

# txt = input('txt ? ')
# lst = txt.split(', ')
# for i in lst:
#     if int(i) % 3 == 0:
#         a = int(i) ** 3
#         l1.append(a)
# print(l1)

# t1 = (1, 2, -3, 4)
# t2 = (3, 5, 2, 1)
# t3 = (2, -2, 0, 1)
# for i in range(len(t1))
#     print(t1(i) + t2(i) + t3(i))
# dict1 = {'S  001': ['Math',
# 'Pyhton'], 'S   002': ['Math'
# 'English']}
# for i in dict1:
# d1 = {'item': 45.50, 'item2': 35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for i in d1:
# n = 3
# float(input('n = '))
#
# if n == 2000:
#     print('Дракон')
# elif n == 2001:
#     print('Змея')
# elif n == 2002:
#     print('Лошадь')
# elif n == 2003:
#     print('Коза')
# elif n == 2004:
#     print('Обезьяна ')
# elif n == 2005:
#     print('Петух')
# elif n == 2006:
#     print('Собака')
# elif n == 2007:
#     print('Свинья')
# elif n == 2008:
#     print('Крыса')
# elif n == 2009:
#     print('Бык')
# elif n == 2010:
#     print('Тигр')
# elif n == 2011:
#     print('Кролик')
# else:
#     print('false')



# set1 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
# set2 = {20, 14, ('pyhton', 'c', 12), 10, 11}
# print(set1 ^ set2)
# print(set1 & set2)
# print(set1 - set2)
# print(set1 | set2)


# set1 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
# set2 = {20, 14, ('pyhton', 'c', 12), 10, 11}
# print(set1.issubset(set2))

# import random
# for i in range(10, 99)

# Ex_1
# def f(x, y):
#     return [x + y]
# print(f(1, 7))
#
# def f(x, y):
#     return [x - y]
# print(f(1, 7))
#
# def f(x, y):
#     return [x * y]
# print(f(1, 7))
#
# def f(x, y):
#     return [x / y]
# print(f(1, 7))
#ex1
# 0 = c
# 1 = s
# 2 = r
# 3 = t
# def circle(r):
#     import math
#     return (r**2 * math.pi)
# def square(a):
#     return a**2
# def rectangle(x,y):
#     return x*y
# def triangle(b,h):
#     return b*h/2
# def area():
#     form = int(input("n = "))
#     if form not in range(4):
#         return "Wrong input. Try again."
#     elif form == 0:
#         r = float(input("r = "))
#         return circle(r)
#     elif form == 1:
#         a = float(input("a = "))
#         return square(a)
#     elif form == 2:
#         x = float(input("x = "))
#         y = float(input("y = "))
#         return rectangle(x,y)
#     else:
#         b = float(input("b = "))
#         h = float(input("h = "))
#         return triangle(b,h)
# print(area())



# Ex_1

# lst = ['Vahan', 'Avo', 'Samvel', 'Mayis', 'Varazdat']
# for i in lst:
#     if len(i) <= 5:
#         time.sleep(2)
#         print(i)





# Ex_4

# import time
# print(time.strftime('%A', time.localtime()))

# Ex_3

# import random
# def dance(girls,boys):
#     n = min(len(girls), len(boys))
#     random.shuffle(boys)
#     random.shuffle(girls)
#     for i in range(n):
#         p = f'{girls[i]}-{boys[i]}'
#         print(p)
# b = ['Gor', 'Vahe', 'Vardan', 'Karen', 'Ashot']
# g = ['Gohar', 'Ani', 'Tatev']
# dance(g,b)

# import Faker
#
# f = faker.Faker(locale="hy-am")
# for i in range(10):
#     print(f.name())




# 1․ Գրել Calculator class, որը․
#    - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
#    - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
#    - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
#    - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__):




class Calculator:
    def gumar(self, x, y):
        return x + y
    def hanum(self, x, y):
        return x - y
    def bazmapatkum(self, x, y):
        return x * y
    def bajanum(self, x, y):
        if y != 0:
            return x / y
        else:
            return ('Tivy cheq karox bajanel 0-i vra')

calculator = Calculator()


result = calculator.gumar(7, 5)
print('7 + 5 =', result)

result = calculator.hanum(7, 5)
print('7 - 5 =', result)

result = calculator.bazmapatkum(7, 5)
print('7 * 5 =', result)

result = calculator.bajanum(15, 5)
print('15 / 5 =', result)

result = calculator.bajanum(7, 0)
print('7 / 0 =', result)

