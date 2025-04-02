
# Lista de números com inteiros e floats
lista = [1, 8, 15, 99, 901, 14, 1.9, 10]

# Loop 'for' para percorrer todos os elementos da lista e imprimir um por um
for numero in lista:
    print(numero)
print('Fin do laço')  # Mensagem indicando o fim do loop

# String que será percorrida no loop
palavra = 'ubuntu'

# Loop 'for' que percorre cada letra da palavra 'ubuntu'
for letra in palavra:
    print(letra)
print('Fin do laço!')  # Mensagem indicando o fim do loop

# Loop 'for' com 'range' de 0 até 49 (range(50) gera valores de 0 a 49)
for numero in range(50):
    print(numero)
print('Fim do laço !')  # Mensagem indicando o fim do loop

# Solicita ao usuário que digite seu nome
nome = input('Digite seu nome: ')

# Loop para imprimir o nome 10 vezes, junto com a contagem
for contador in range(10):
    print(f'{contador+1} {nome}')  # Mostra a contagem começando em 1
print('Fim do programa!')  # Mensagem indicando o fim do loop

# Loop 'for' decrescente, começando em 50, diminuindo de 3 em 3, até o valor 2 (não incluso)
for decrescente in range(50, 2, -3):
    print(decrescente)
print('Fim do programa!')  # Mensagem indicando o fim do loop

# Loop 'for' crescente, começando em 2, aumentando de 3 em 3, até o valor 50 (não incluso)
for crescente in range(2, 50, 3):
    print(crescente)
print('Fim do programa!')  # Mensagem indicando o fim do loop

# Tupla contendo estilos musicais
musicas = ('Reggae', 'Brega', 'Pagode', 'Funk', 'MPB', 'Jazz', 'Rock')

# Loop que percorre cada estilo musical na tupla
for music in musicas:
    if music == 'Funk':  # Se a música for 'Funk', o comando 'continue' faz o loop pular essa iteração
        continue
    print(music)  # Imprime o nome da música, exceto 'Funk'
print('Fim do programa')  # Mensagem indicando o fim do loop
