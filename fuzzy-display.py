import random
import copy
#НЕЧЕТКИЕ ОТОБРАЖЕНИЯ
x={}
y=[]
f=[]
nx=(int)(input("Введите количество элементов x: "))#задаем размер словаря с x-ами
for i in range(nx):#вводим значения х-ов
    key="x"+str(i+1)
    x[key]=(float)(input("Введите значение x"+(str)(i+1)+": "))
print(x)

ny=(int)(input("Введите количество элементов y: "))#задаем размер списка с у-ами
for i in range(ny):
    row = input("Введите x-ы для y"+ (str)(i+1)+": ").split()#
    for i in range(len(row)):
        row[i] = str(row[i])#
    y.append(row)
print (y)
for i in range(len(y)):#находим соответствия в списке и словаре
    for j in range(len(y[i])):
        for k in x:
            if y[i][j]==k:
                y[i][j]=x[k]
print("Подставим для каждого х свое значение: ", y)

for i in range(len(y)):#копируем только максимальные значения в другой список
    a=max(y[i])
    f.append(a)

print ("Найдем для каждого y максимальное значение x: ",f)

for i in range(len(f)):#возвращаем x-ы на место
    for k in x:
        if f[i]==x[k]:
            f[i]=k

print ("Запишем в виде x-ов: ",f)

