# Definindo funcções:
# Modularização, Reuso de código e Legibilidade 
...

def mesnagem ():
    print('Estou aprendendo a programar em Python')
    print('Serei um analista de dados !')
mesnagem()

#Definindo funções com argumentos:

def soma_num(a, b):
    print(a + b)
soma_num(100, 99)


def mult_num(r, m):
    return r * m
a = 6
b = 9
c = mult_num(a, b)
print(f'O produtos de {a} e {b} é {c}')


def div_num(div01, div02):
    if div02 != 0:
        return div01 / div02
    else:
        return 'Não pode haver divisão por zero !'

if __name__=='__main__':
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo números: '))

    resultado = div_num(a, b)
    print(f'{a}dividido por {b} é igual a {resultado}')

print('Fim do programa')


# Calculando o quadrado de números:
def quad (val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ ==  '__main__':
    valores = [2, 8, 3, 12, 6]
    result = quad(valores)

    for g in result:
        print(g)
print('Fim do programa')

#5:25:16