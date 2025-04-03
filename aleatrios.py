import random

#valor = random.randint(1,30)
#print(valor)

print('Gerar cinco números aleatórios entre 1 e 50:\n')
for contador in range(5):
    numero = random.randint(1,50)
    print(f'Números gerados: {numero}')


print('Fim do programa')

valor = random.random()
print(f'O número gerado foi: {round(valor * 10, 2)}')

print('Fim do programa')


valor1 = random.uniform(1,100)
print(f'O número gerado, foi: {round(valor1, 3)}')

print('Fim do programa')

lista = [1, 99, 14, 25, 50, 45, 20, 30, 11, 10, 1, 78, 3]
numero = random.choice(lista)
print(f'O número escolhido foi: {numero}')

print('Fim do programa')

lista1 = [1, 99, 14, 25, 50, 45, 20, 30, 11, 10, 1, 78, 3]
numero1 = random.sample(lista1, 4)
print(f'Os números escolhidos, foram: {numero1}')

print('Fim do programa')

lista3 = [1, 99, 14, 25, 50, 45, 20, 30, 11, 10, 1, 78, 3]
print(f'Exibindo a lista original:{lista3}')
print(f'Agora, a lista está embaralhada:')
nlista = random.shuffle(lista3)
print(lista3)

print('Fim do progarama')