tupla = (2, 1, 6, 9, 10)
#tupla[2] = 15 não pode ser alterada 
print(tupla)

print('Fim do programa')

estados1 = ('MA', 'SP', 'PA', 'CE', 'AM')
estados2 = ('PN', 'BA', 'BH', 'TO', 'DF','SP')
uniestados = estados1 + estados2
print(uniestados)
print(uniestados.count('SP'))
print(estados1[0:3])
print('MA' in estados1)

for brasil in uniestados:
    print(f'Os estados do Brasil: {brasil}')

print('Fim do programa')

Uf_brasl = list(estados1)
Uf_brasl[2] = 'AL'
print(Uf_brasl)

cidades = ['Belém', 'São Luiz', 'Rio de Janeiro', 'Alagoas']
cidades_br = tuple(cidades)
print(type(cidades_br))


print(sorted(cidades))