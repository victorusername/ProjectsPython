print('=======   Desafio 13   =======')
preco1 = float(input('Digite o valor do produto: '))
precodesc = preco1 - (preco1 * 5 / 100)
print('O valor do produto é R${:.2f}, com desconto de 5% o produto sai por R${:.2f}'.format(preco1, precodesc))
