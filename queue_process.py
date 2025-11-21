from collections import deque

entrada = input()
palavras = entrada.split()

fila = deque()
for p in palavras:
    fila.appendleft(p)

print(fila)

for p in palavras:
    if "a" in p.lower():
        print(p)