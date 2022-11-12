# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

valor = float(input())
valor2 = valor
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0

moedas100 = 0
moedas50 = 0
moedas25 = 0
moedas10 = 0
moedas5 = 0
moedas1 = 0

if valor > 100:
    notas100 = int(valor/100)
    valor = valor - notas100*100
if valor > 50:
    notas50 = int(valor/50)
    valor = valor - notas50*50
if valor > 20:
    notas20 = int(valor/20)
    valor = valor - notas20*20
if valor > 10:
    notas10 = int(valor/10)
    valor = valor - notas10*10
if valor > 5:
    notas5 = int(valor/5)
    valor = valor - notas5*5
if valor > 2:
    notas2 = int(valor/2)
    valor = valor - notas2*2
    
    
if valor > 1:
    moedas100 = int(valor/1)
    valor = valor - moedas100*1
if valor > 0.5:
    moedas50 = int(valor/0.5)
    valor = valor - moedas50*0.5
if valor > 0.25:
    moedas25 = int(valor/0.25)
    valor = valor - moedas25*0.25
if valor > 0.1:
    moedas10 = int(valor/0.1)
    valor = valor - moedas10*0.1
if valor > 0.05:
    moedas5 = int(valor/0.05)
    valor = valor - moedas5*0.05
if valor > 0.01:
    moedas1 = int(valor/0.01)
    valor = valor - moedas1*0.01


print("NOTAS:")
print(f"{notas100} nota(s) de R$ 100.00")
print(f"{notas50} nota(s) de R$ 50.00")
print(f"{notas20} nota(s) de R$ 20.00")
print(f"{notas10} nota(s) de R$ 10.00")
print(f"{notas5} nota(s) de R$ 5.00")
print(f"{notas2} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moedas100} moeda(s) de R$ 1.00")
print(f"{moedas50} moeda(s) de R$ 0.50")
print(f"{moedas25} moeda(s) de R$ 0.25")
print(f"{moedas10} moeda(s) de R$ 0.10")
print(f"{moedas5} moeda(s) de R$ 0.05")
print(f"{moedas1} moeda(s) de R$ 0.01")