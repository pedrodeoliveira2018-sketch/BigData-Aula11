import os 
import random

def G_N( ini ,fim , qtd ):
    lst_num = [random.randint(ini , fim) for c in range (qtd)]
    return lst_num



inicio = 1
final = 10
quantidade = 2

lst_num = G_N (inicio , final , quantidade)
print(lst_num)






# lst = G_N 
    
# n = random.randint(1, 10)
# lst = [random.randint(1, 10) for num in range(2)]
# print(lst)