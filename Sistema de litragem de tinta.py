print('=======   Desafio 12   =======')
print('Aqui é da Tintas SBC, para continuarmos seu atendimento poderia nos informar esses tamanhos abaixo')
larg = float(input('Largura da parede que deseja pintar: '))
alt = float(input('Altura da parede que deseja pintar: '))
area = larg * alt
print('Sua parede tem a dimensão de {:.2f}larg x {:.2f}altura. Então a área em metros quadrados é {}'.format(larg, alt, area))
print('Portanto para pintar a parede, você precisará de {:.2f} Litros de tinta'.format(area / 2))
