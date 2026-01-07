import os 
import random

def G_N( ini ,fim , qtd ):
    lst_num = [random.randint(ini , fim) for c in range (qtd)]
    return lst_num

def soma (n1 , n2):
    so = n1 + n2
    return so

def menos ( c1 , c2):
    sa = c1 - c2
    return sa

def xx (x1 , x2 ):
    se = x1 * x2
    return se

def div (d1 , d2):
    si = d1 / d2
    return si


inicio = 1
final = 10
quantidade = 2

lst_num = G_N (inicio , final , quantidade)
print(lst_num)
num1 = lst_num[0]
num2 = lst_num[1]

soma = soma (num1 , num2)
menos = menos (num1 , num2)
xx = xx (num1 , num2)
div = div (num1 , num2)

print(soma)
print(menos)
print(xx)
print (div)


m = (lst_num[0] + lst_num[1])
n = (lst_num[0] - lst_num[1])
x = (lst_num[0] * lst_num[1])
d = (lst_num[0] / lst_num[1])
print(lst_num , m , n , x ,d )
print(lst_num[0])
print(lst_num[1])
print (m)
print(n)
print(x)
print(d)