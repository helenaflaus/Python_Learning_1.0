# 038 Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
'''- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
  print(f'O número {n1:.0f} é maior que o número {n2:.0f}.')
elif n2 > n1:
  print(f'O número {n2:.0f} é maior que o número {n1:.0f}.')
elif n1 == n2:
  print(f'O número {n1:.0f} é igual ao número {n2:.0f}.')
