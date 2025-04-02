

# Inicializa a variável 'num' com o valor 1
num = 1

# Inicia um loop while que será executado enquanto 'num' for menor ou igual a 10
while num <= 10:
    print(num)  # Exibe o valor atual de 'num'
    num += 1  # Incrementa 'num' em 1 a cada iteração

# Após a saída do loop, imprime uma mensagem indicando o fim do laço
print("Fim do laço")

# ---------------------------------------------

# Inicializa a variável 'nome' com o valor None
nome = None

# Inicia um loop infinito (ele só será interrompido com um comando break)
while True:
    print('Digite seu nome, ou x para encerrar o programa: ')  # Solicita um nome ao usuário
    nome = input()  # Captura a entrada do usuário e armazena na variável 'nome'

    # Verifica se o usuário digitou 'x' ou 'X' para sair do loop
    if nome == 'x' or nome == 'X':
        break  # Encerra o loop

    # Se o usuário digitou um nome diferente de 'x' ou 'X', exibe uma mensagem de boas-vindas
    print(f'Seja bem-vindo(a), {nome}')

# Após a saída do loop, imprime uma mensagem de despedida
print('Até a próxima !!')


