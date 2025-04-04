# Lista de valores numéricos
valores = [1, 50, -1599, 5, 10.99, 9]

# Encontra e imprime o maior valor da lista
print(max(valores))

# Encontra e imprime o menor valor da lista
print(min(valores))

# Declaração de variáveis
a = -2
b = 4

# Retorna o valor absoluto de 'a' (transforma negativo em positivo)
print(abs(a))

# Calcula 'a' elevado à potência 'b' (ou seja, -2^4 = 16)
print(pow(a, b))

# Declaração de uma variável float
c = 2.6558

# Arredonda o valor de 'c' para 2 casas decimais
print(round(c, 2))

# Indica o fim do primeiro bloco do programa
print('Fim do programa')

# Importa a biblioteca matemática
import math 

# Declaração de variáveis
x = 8
y = 1000

# Calcula a raiz quadrada de 'x'
raiz_quadrada = math.sqrt(x)

# Arredonda para baixo (menor número inteiro próximo à raiz quadrada de x)
print(math.floor(raiz_quadrada))

# Mensagem com erro de digitação ('prorama' deveria ser 'programa')
print('Fim do prorama')

# Calcula o logaritmo de 'y' na base 10
logartmo = math.log10(y)
print(logartmo)

# Imprime o valor de pi da biblioteca math
print(math.pi)

# Calcula e imprime o fatorial de 'x' (8! = 8 × 7 × 6 × ... × 1)
print(math.factorial(x))

# Retorna o resultado da divisão de 'x' por infinito (resultado esperado: 0.0)
print(x / math.inf)
