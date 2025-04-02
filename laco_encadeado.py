# Primeiro loop aninhado: Contagem decrescente dentro de uma contagem crescente
for conta_externo in range(1,6):  # Loop externo varia de 1 a 5
    print(f'\nRodada: {conta_externo}')  # Exibe o número da rodada
    for conta_interno in range(5, 0, -1):  # Loop interno conta de 5 a 1 (decrescente)
        print(f'\nValor: {conta_interno}')  # Exibe o valor atual do loop interno

print('Fim das contagens')  # Indica o fim do primeiro conjunto de loops

import random  # Importação da biblioteca para gerar números aleatórios

# Segundo loop aninhado: Geração de números aleatórios em um intervalo
for externo in range(1,6):  # Loop externo varia de 1 a 5
    print(f'\nConjunto {externo}')  # Exibe o número do conjunto atual
    for interno in range(5):  # Loop interno executa 5 vezes
        numero = random.randint(1,100)  # Gera um número aleatório entre 1 e 100
        print(f'Valor:{numero}')  # Exibe o número gerado
print('Fim do laço !')