#Bibliotecas
import random

# random.randit -> Números inteiros
n = random.randint(1, 10)
m = random.randint(1, 10)
print(n, m)

# ---------------------------------------------
# Gerar números decimais
n_decimal = random.uniform(1, 10)
numero_decimal = round(n_decimal, 3) # Arredonda
print(f'{n_decimal:.2f}') # Formata para duas casas
print(numero_decimal)