# Biblioteca 
import random

n = random.randint(1, 10)
m = random.randint(1, 10)
print(n,m)

# -------------------------------------------------
# Gerar numeros decimais

n_dicinal = random.uniform(1,10)
numero_decimal = round(n_dicinal,1) #Arredondar 
print(f'{n_dicinal:2f}') # formatar 
print(numero_decimal)