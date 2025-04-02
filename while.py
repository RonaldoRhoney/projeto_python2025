num = 1

while (num <= 10):
    print(num)
    num += 1
print("Fim do laço")


nome = None

while True:
    print('Digite seu nome, ou x para encerrar o programa: ')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Seja bem vindo(a), {nome}')
print('Até a próxima !!')