import random

numeros = [random.randint(1, 100) for _ in range(10)]

print("Lista original:", numeros)
print("Ordem crescente:", sorted(numeros))
print("Ordem decrescente:", sorted(numeros, reverse=True))