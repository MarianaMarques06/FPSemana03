from collections import deque

entrada = input()
numeros_str = entrada.split()

numeros = []
for n in numeros_str:
    numeros.append(int(n))

pilha = deque(numeros)

print(pilha)

while pilha:
    valor = pilha.pop()
    print(valor * 2)