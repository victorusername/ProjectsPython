print('=======   Desafio 14   =======')
salario = float(input('Digite o valor do seu salario: '))
aumento = salario + (salario * 15 / 100)
print('Seu salario atualmente é R${:.2f} com aumento de 15% ficará R${:.2f}'.format(salario, aumento))
