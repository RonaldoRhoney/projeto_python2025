# Listas representam uma sequência de valores 

# Sintaxe: nome_lista = [valores]
notas = [2, 9, 8, 25, 15, 100]  # Criação de uma lista chamada 'notas' com valores inteiros
print(notas)  # Exibe a lista 'notas' no console

print('Fim do programa')  # Indica o final da execução do código

# Concatenando (juntando) listas:
lista1 = [10, 5, 8, 7, 3, 20]  # Criação da primeira lista
lista2 = [1, 1.999, 9.1, 17, 1000]  # Criação da segunda lista

junta_listas = lista1 + lista2  # Concatenação das duas listas
junta_listas[0] = 2000  # Alteração do primeiro elemento da lista concatenada
print(junta_listas)  # Exibe a lista modificada

print(junta_listas[-2])  # Exibe o penúltimo elemento da lista
print(junta_listas[5])  # Exibe o elemento na posição 5 (índice inicia em 0)
print(junta_listas[0:4])  # Exibe os elementos do índice 0 ao 3 (4 não é incluído)
print(junta_listas[-1:3])  # Retorna uma lista vazia, pois o índice final deve ser maior que o inicial
print(len(junta_listas))  # Retorna o número de elementos na lista
print(sorted(junta_listas, reverse=True))  # Retorna a lista ordenada de forma decrescente
print(sum(junta_listas))  # Retorna a soma de todos os elementos numéricos da lista
print(min(junta_listas))  # Retorna o menor valor da lista
print(max(junta_listas))  # Retorna o maior valor da lista

junta_listas.append(5000)  # Adiciona o valor 5000 ao final da lista
print(junta_listas)  # Exibe a lista após a adição do elemento

junta_listas.pop()  # Remove o último elemento da lista
print(junta_listas)  # Exibe a lista após a remoção do elemento

junta_listas.pop(5)  # Remove o elemento no índice 5 da lista
print(junta_listas)  # Exibe a lista após a remoção

junta_listas.insert(2, 50)  # Insere o valor 50 na posição de índice 2
print(junta_listas)  # Exibe a lista após a inserção

junta_listas.insert(4, 'Boas práticas')  # Insere a string 'Boas práticas' na posição de índice 4
print(junta_listas)  # Exibe a lista após a inserção

print('Boas práticas' in junta_listas)  # Verifica se 'Boas práticas' está na lista (retorna True ou False)

print('Fim do programa')  # Indica o final da execução do código
print('#######')  # Exibe uma separação visual no console

# Laço FOR com lista
frutas = ['Manga', 'AAbacaxi', 'Acerola', 'Kiwi', 'Maracujá', 'Uva']  # Lista de frutas
for fruta in frutas:  # Percorre a lista de frutas
    print(fruta)  # Exibe cada fruta no console

# EXERCÍCIO:

cores = []  # Criação de uma lista vazia para armazenar cores

for conta_cor in range(6):  # Laço que se repete 6 vezes
    print(f'Escreva a sua cor favorita: ')  # Solicita ao usuário uma cor favorita
    cor = input()  # Lê a entrada do usuário
    cores.append(cor)  # Adiciona a cor à lista

cores.sort()  # Ordena a lista de cores em ordem alfabética

print(f'\nAqui estão as suas cores favoritas:')  # Exibe uma mensagem formatada
for cor in cores:  # Percorre a lista de cores
    print(cor)  # Exibe cada cor na tela

print('Fim do programa')  # Indica o final da execução do código
