# Criação de uma tupla com 5 elementos
tupla = (2, 1, 6, 9, 10)

# A linha abaixo está comentada porque geraria erro.
# Tuplas são imutáveis, ou seja, seus valores não podem ser alterados.
# tupla[2] = 15

# Imprime a tupla
print(tupla)

# Mensagem para indicar o fim de uma parte do programa
print('Fim do programa')

# Duas tuplas com siglas de estados brasileiros
estados1 = ('MA', 'SP', 'PA', 'CE', 'AM')
estados2 = ('PN', 'BA', 'BH', 'TO', 'DF', 'SP')

# Concatenação das duas tuplas em uma nova chamada uniestados
uniestados = estados1 + estados2

# Imprime a nova tupla unificada
print(uniestados)

# Conta quantas vezes o estado 'SP' aparece na tupla uniestados
print(uniestados.count('SP'))

# Fatiamento da tupla estados1, pegando do índice 0 até o 2 (o 3 não entra)
print(estados1[0:3])

# Verifica se 'MA' está presente na tupla estados1
print('MA' in estados1)

# Estrutura de repetição para imprimir cada estado presente na tupla uniestados
for brasil in uniestados:
    print(f'Os estados do Brasil: {brasil}')

# Mensagem para indicar o fim de outra parte do programa
print('Fim do programa')

# Converte a tupla estados1 para uma lista, tornando possível alterar seus valores
Uf_brasl = list(estados1)

# Altera o valor do índice 2 para 'AL'
Uf_brasl[2] = 'AL'

# Imprime a lista alterada
print(Uf_brasl)

# Lista de cidades
cidades = ['Belém', 'São Luiz', 'Rio de Janeiro', 'Alagoas']

# Converte a lista de cidades para uma tupla
cidades_br = tuple(cidades)

# Imprime o tipo da variável cidades_br (que será <class 'tuple'>)
print(type(cidades_br))

# Imprime a lista de cidades em ordem alfabética, sem alterar a original
print(sorted(cidades))
