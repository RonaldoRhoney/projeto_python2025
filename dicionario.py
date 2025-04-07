#Dicionários em Python:
elemento = {
    'z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}
print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento["densidade"]}')
print(f'O dicionário possui {len(elemento)} elementos')

# Atualizando uma entrada:
elemento ['grupo'] = 'Alcalinos'
print(elemento)

#Adicionando uma nova entrada ao dicionário:
elemento['periodo'] = 1
print(elemento)

#Excluíndo itens de um dicioário:
#del elemento['grupo']
#print(elemento)

#Apagando todos os elementos do diconário:
#elemento.clear()
#print(elemento)

#Apagando o dicionário por completo:
#del elemento
#print(elemento)  #Surgirá uma mensagem a cusando um ERRO, pois o dicionário já não existe !!!

# O método 'items' mostras os elementos no formato de tuplas:

print(elemento.items())
for elementos in elemento.items():
    print(elementos)
# O método 'keys' mostra apenas as chaves do dicionário:
print(elemento.keys())
for i in elemento.keys():
    print(i)


# O método 'value' mostra  apenas o valores do dicionário:
print(elemento.values())
for mostar_valores in elemento.values():
    print(mostar_valores)

# Mostrndo os elementos em forma de tabela ou relatório:

for r, j in elemento.items():
    print(f'{r}: {j}')
    
