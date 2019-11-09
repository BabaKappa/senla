'''Задача 1'''
#n = int(input('Введите число N'))
#prime = []
#q = 0
#i=1
#while i<=n:
#    for j in range(2,i):
#        if i % j == 0:
#            q += 1
#    if q == 0:
#        prime.append(i)
#    else:
#        q = 0
#    i+=1
#print(prime)


'''Задача 2'''
#n = int(input('Введите число N'))
#piz=[]
#a = 0
#b = 1
#piz.append(a)
#piz.append(b)
#i=2
#while i<n:
#    c = a + b
#    piz.append(c)
#    a = b
#    b = c
#    i+=1
#print(piz)


'''Задача 3'''
#line1 = input('Введите начало и конец первого отрезка(через пробел)- ').split(' ')
#a = int(line1[0])
#b = int(line1[1])
#line2 = input('Введите начало и конец второго отрезка(через пробел)- ').split(' ')
#c = int(line2[0])
#d = int(line2[1])
#k = 0
#if a>b:
#    a,b=b,a
#if c>d:
#    c,d=d,c
#for i in range(a,b+1):
#    for j in range(c,d+1):
#        if i == j:
#            k += 1
#if k == 0:
#    print('Отрезки не пересекаются')
#elif k != 0:
#    print('Отрезки пересекаются')
#else:
#    print('ERROR!!!')


'''Задача 4'''
#numb = input('Введите два числа (через пробел)- ').split(' ')
#a = old1 = int(numb[0])
#b = old2 = int(numb[1])
#while old1 % old2 != 0:
#    new = old1 % old2
#    old1 = old2
#    old2 = new
#nod = new
#nok = (a * b) / nod
#print('НОД чисел a и b =', nod)
#print('НОК чисел a и b =', nok)


'''Задача 5'''
#string1 = str(input('Введите слово - '))
#string2 = str(string1[::-1])
#if string1 == string2:
#    print('Слово - палиндром')
#else:
#    print('Слово не палиндром')#


'''Задача 6'''
#strold = str(input())
#strnew = ''
#k=0
#basis = (0,1,2,3,4,5,6,7,8,9)
#for elem in (strold):
#    for i in basis:
#        if str(elem)==str(i):
#            k+=1
#    if k==0:
#        strnew+=elem
#    else:
#        k=0
#print(strnew)