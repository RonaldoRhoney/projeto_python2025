import random  # Importa o módulo random para geração de números aleatórios

# O trecho abaixo foi comentado, mas serviria para gerar um número aleatório entre 1 e 30
# valor = random.randint(1,30)
# print(valor)

# Geração de cinco números aleatórios entre 1 e 50
print('Gerar cinco números aleatórios entre 1 e 50:\n')
for contador in range(5):  # Loop que se repete 5 vezes
    numero = random.randint(1, 50)  # Gera um número aleatório inteiro entre 1 e 50
    print(f'Números gerados: {numero}')  # Exibe o número gerado

print('Fim do programa')

# Geração de um número aleatório entre 0 e 1 e multiplicação por 10
valor = random.random()  # Gera um número decimal entre 0 e 1
print(f'O número gerado foi: {round(valor * 10, 2)}')  # Multiplica o número por 10 e arredonda para 2 casas decimais

print('Fim do programa')

# Geração de um número decimal aleatório entre 1 e 100
valor1 = random.uniform(1, 100)  # Gera um número decimal entre 1 e 100
print(f'O número gerado foi: {round(valor1, 3)}')  # Exibe o número gerado, arredondado para 3 casas decimais

print('Fim do programa')

# Escolha aleatória de um número dentro de uma lista
lista = [1, 99, 14, 25, 50, 45, 20, 30, 11, 10, 1, 78, 3]
numero = random.choice(lista)  # Escolhe aleatoriamente um número da lista
print(f'O número escolhido foi: {numero}')  # Exibe o número escolhido

print('Fim do programa')

# Seleção de quatro números aleatórios distintos dentro de uma lista
lista1 = [1, 99, 14, 25, 50, 45, 20, 30, 11, 10, 1, 78, 3]
numero1 = random.sample(lista1, 4)  # Seleciona 4 números aleatórios da lista (sem repetição)
print(f'Os números escolhidos foram: {numero1}')  # Exibe os números escolhidos

print('Fim do programa')

# Embaralhamento de uma lista
lista3 = [1, 99, 14, 25, 50, 45, 20, 30, 11, 10, 1, 78, 3]
print(f'Exibindo a lista original: {lista3}')  # Exibe a lista original
print(f'Agora, a lista está embaralhada:')
random.shuffle(lista3)  # Embaralha a lista original
print(lista3)  # Exibe a lista embaralhada

print('Fim do programa')