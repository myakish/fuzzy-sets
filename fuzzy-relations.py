#!/usr/bin/env python3
#НЕЧЕТКИЕ ОТНОШЕНИЯ
import copy#импортируем, чтобы копировать не по ссылке
n=(int)(input("Введите размерность матриц: "))
a = []
b=[]
c=[]


print ("Заполним матрицу A:")
for i in range(n):
    row = input("Введите i-ую строку: ").split()#разбиваем строку по пробелам
    for i in range(len(row)):
        row[i] = float(row[i])#берем вещественные числа
    a.append(row)#добавляем в список


print ("Заполним матрицу B:")#аналогично заполняем b
for i in range(n):
    row = input("Введите i-ую строку: ").split()
    for i in range(len(row)):
        row[i] = float(row[i])
    b.append(row)


def maximum(m1,m2):#начало функции объединения
    n1=copy.deepcopy(m1)#копируем не по ссылке
    n2=copy.deepcopy(m2)
    for i in range(n):
        for j in range(n):
            if n1[i][j]<n2[i][j]:#выбираем максимальные
                n1[i][j]=n2[i][j]
    print("Результат объединения A и B: ",n1)
maximum(a,b)


def minimum(m1,m2):#начало функции пересечения
    n1 = copy.deepcopy(m1)
    n2 = copy.deepcopy(m2)
    for i in range(n):
        for j in range(n):
            if n1[i][j] >= n2[i][j]:#выбираем минимальный
                n1[i][j] = n2[i][j]
    print("Результат пересечения A с B: ", n1)
minimum(a,b)


def dopolnenie(m1,m2):#начало функции дополнения
    n1 = copy.deepcopy(m1)
    n2 = copy.deepcopy(m2)
    for i in range(n):
        for j in range(n):
            n1[i][j]=1-n1[i][j]
            n2[i][j]=1-n2[i][j]
    print("Дополнение A: ", n1)
    print("Дополнение B: ", n2)
dopolnenie(a,b)


def composition(m1,m2):#начало функции композиция
    n1=copy.deepcopy(m1)
    n2=copy.deepcopy(m2)
    for k in range(n):
        for i in range(n):
            min = []#сбрасываем массив минимумов
            for j in range(n):
                if n1[k][j]>=n2[j][i]:#выбираем минимальный
                    min.append(n2[j][i])
                else:
                    min.append(n1[k][j])
            max=0#обнуляем максимум
            for x in min:
                if x>max:#ищем максимум в массиве минимума
                    max=x
            print (max)
            c.append(max)
    print ("Композиция A и B: ",c)
composition(a,b)

