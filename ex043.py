# 043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
'''- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Informe o peso em kilos: '))
altura = float(input('Informe a altura em metros: '))

imc = peso / (altura**2)

if imc < 18.5:
  print('Peso ideal.')
elif imc <= 30:
  print('Está com sobrepeso.')
elif imc <= 40:
  print('Está obeso.')
else:
  print('Está muito obeso.')
