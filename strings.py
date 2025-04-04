# Definindo variáveis de texto
nome = 'Curso de Inglês'
Prof = 'Rhoney'

# Concatenando strings e exibindo resultado
print(nome + ' com ' + Prof)

print('Fim do programa')

# Separando uma frase em palavras com split()
palavras = 'A tecnologia tem  o poder de transformar realidades'
frase = palavras.split()  # Divide a string em uma lista de palavras
print(frase[1])  # Exibe a segunda palavra da lista (índice 1)

# Percorre e imprime cada palavra da lista
for frases in frase:
    print(frases)

print('Fim do programa')

# Pede ao usuário um e-mail
email = input('Digite seu email: ')

# Encontra a posição do caractere '@'
arroba = email.find('@')
print(arroba)

# Separa o e-mail em nome de usuário e domínio
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

print('Fim do programa')

# Tupla de produtos
produtos = 'roupa', 'calçados', 'cosméticos', 'louças'

# Verifica se certos produtos estão na tupla
print('cosméticos' in produtos)  # True
print('bijuterias' in produtos)  # False

# Busca substrings dentro da palavra 'magnésio'
produto1 = 'magnésio'
prod = produto1.find('gnés')  # Retorna o índice de início da substring
print(prod)
prod = produto1.find('loc')  # Retorna -1 se não encontrar
print(prod)

# Manipulação de caixa de texto
coisas = 'roupas de dormir no frio'
print(coisas.upper())      # Tudo em maiúsculas
print(coisas.lower())      # Tudo em minúsculas
print(coisas.capitalize()) # Primeira letra maiúscula
print(coisas.title())      # Primeira letra de cada palavra maiúscula

print('Fim do programa')

# Substituindo parte do texto
suplemento = 'cloreto de magnésio'
novo_suplemento = suplemento.replace('magnésio', 'sódio')
print(suplemento)
print(novo_suplemento)

# Removendo espaços desnecessários
com_espaco = '    apóis quase 3 meses voltei à academia      '
print(com_espaco)
print(com_espaco.lstrip())  # Remove espaços à esquerda
print(com_espaco.rsplit())  # Divide a string a partir da direita
print(com_espaco.strip())   # Remove espaços em ambos os lados

print('Fim do programa')

# Alinhamento de texto
empresa = 'Logística'
print(empresa)
print(empresa.rjust(20))          # Alinha à direita com 20 caracteres
print(empresa.center(20))         # Centraliza com 20 caracteres
print(empresa.ljust(20, "-"))     # Alinha à esquerda, preenchendo com '-'
print(empresa.center(20, "-"))    # Centraliza preenchendo com '-'

print('Fim do programa')

# Verificando prefixos e sufixos
verificar = 'Hoje já não é agora, são 00:01'
print(verificar.startswith('Hoj'))  # True
print(verificar.endswith('bos'))    # False

# Docstring como comentário explicativo de várias linhas
texto = """
Uma docstring (ou documentation string) é um tipo especial de comentário em Python 
usado para documentar funções, classes e módulos. Ela é escrita entre três aspas duplas 
(\"\"\" \"\"\") ou simples (''' ''') e normalmente aparece logo abaixo da definição de uma função, 
classe ou módulo.
"""
print(texto)
