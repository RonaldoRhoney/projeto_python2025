paises = { 'Brasil', 'Bulgária', 'Venezuela', 'USA', 'Vaticano'}
print(len(paises))
print('França' not in paises)
print('Argentina' in paises)

for capital in paises:
    print(capital.upper())

print('Fim do rograma')

cidades = ['Bacuri', 'Bacuri', 'Vila-nova', 'Bitíua', 'Portugal', 'Batepé']
print(cidades, end='')
cidades_set = set(cidades)
print(cidades_set)

print('Fim do programa')


clube1 = {'Corinthians', 'São Paulo', 'Remo','Palmeiras', 'Santos', 'Paysandu'}
clube2 = {'Remo', 'Vasco', 'Flamengo', 'Paysandu', 'Botafogo','Volta Redonda'}
print(clube1 == clube2)
print(clube2 != clube2)
print(clube1 | clube2)
print(clube1 & clube1)
print(clube1.union(clube2))
print(clube1.intersection(clube2))
print(clube1 ^ clube2)
print(clube1.symmetric_difference(clube2))

clube1.add('Bahia')
clube2.remove('Flamengo')
clube1.pop()
#clube1.discard()
#clube2.clear()
#clube1.clear()

print('Fim do programa')