# Define uma variável chamada 'mensagem' e atribui a string 'função print'
mensagem = 'função print'

# Exibe o conteúdo da variável 'mensagem' no console
print(mensagem)

# Exibe diretamente uma string na tela
print('Aula de Python')

# Define uma variável chamada 'nome' e atribui a string 'Ronaldo Martins'
nome = 'Ronaldo Martins'

# Exibe a string 'Densenvolver -' seguida do valor da variável 'nome'
print('Densenvolver -', nome)

# Solicita ao usuário que digite seu nome e armazena na variável 'nome1'
nome1 = input('Digite seu nome: ')

# Concatena e exibe uma mensagem personalizada de boas-vindas
print('Olá ' + nome1 + '! Seja bem vindo ao curso !')

# Exibe a mensagem e pula para a próxima linha automaticamente
print('Imprime a mensagem e muda de linha')

# Exibe a mensagem sem quebrar a linha (devido ao parâmetro end='')
print('Imprime a mensagem e permanece na linha.', end='')

# Exibe outra mensagem na mesma linha, já que o 'end' anterior removeu a quebra de linha
print('Imprime a mensagem na mesma linha')

# Declara variáveis nome2 e idade
nome2 = 'Karla'
idade = 29

# Formata uma string utilizando o método .format()
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome2, idade)

# Exibe a mensagem formatada
print(msg_formatada)

# Outra forma de formatação usando f-strings
nome3 = 'Ronaldo Martins'
peso = 69.96

# Utiliza f-string para inserir variáveis diretamente na string
msg = f'Olá, eu sou o {nome3} e meu peso é {peso}'

# Exibe a mensagem formatada
print(msg)

# Declara duas variáveis numéricas
a = 15
b = 25

# Usa f-string para exibir o resultado de uma operação matemática dentro da string
Resposta = f'A soma de {a} com {b} é igual a {a + b}'

# Exibe o resultado da soma
print(Resposta)

# Declara uma variável do tipo float
valor = 259.965315

# Formata o valor para exibição com duas casas decimais
print(f'O valor é {valor:.2f}')

# Define um novo valor para a variável 'valor'
valor = 152.12456

# Exibe o valor formatado com duas casas decimais e entre aspas simples
print(f'O valor é \'{valor:.2f}\'')

# Declara variáveis nome4 e idade
nome4 = 'Lucas'
idade = 45

# Usa tabulação (\t) para alinhar os valores
print(f'Nome:\t{nome4}\tidade:\t{idade}')



