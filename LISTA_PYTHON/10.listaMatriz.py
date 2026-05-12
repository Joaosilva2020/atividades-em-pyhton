matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Matriz:")
for linha in matriz:
    print(linha)


soma = sum(sum(linha) for linha in matriz)
print("Soma total:", soma)


diagonal = [matriz[i][i] for i in range(3)]
print("Diagonal principal:", diagonal)