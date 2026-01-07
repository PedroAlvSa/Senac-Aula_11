import os
import random


def gerar_numeros(ini, fim, qtd):
    lst_num = [random.randint(ini, fim) for i in range(qtd)]
    return lst_num


def soma(a ,b):
    x = a + b
    return x


def sub(a1 ,b1):
    x1 = a1 - b1
    return x1


def div(a2 ,b2):
    x2 = a2 / b2
    return x2


def mult(a3 ,b3):
    x3 = a3 * b3
    return x3


# Inicio do algoritmo
inicio = 1
final = 10
quantidade = 2    
lst_numeros = gerar_numeros(inicio, final, quantidade)
print(lst_numeros[0])
print(lst_numeros[1])

num1 = lst_numeros[0]
num2 = lst_numeros[1]
soma = soma(num1, num2)
sub = sub(num1, num2)
mult = mult(num1, num2)
div = div(num1, num2)

print(f'A soma dos números {lst_numeros[0]} e {lst_numeros[1]}: ')
print(soma)
print()
print(f'A subtração dos números {lst_numeros[0]} e {lst_numeros[1]}: ')
print(sub)
print()
print(f'A multiplicação dos números {lst_numeros[0]} e {lst_numeros[1]}: ')
print(mult)
print()
print(f'A divisão dos números {lst_numeros[0]} e {lst_numeros[1]}: ')
print(div)