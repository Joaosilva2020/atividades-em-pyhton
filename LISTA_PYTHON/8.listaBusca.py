numeros = [5, 8, 12, 20, 3, 7, 15, 9, 1, 4]

busca = int(input("Digite um número: "))

if busca in numeros:
    print("Número encontrado!")
    print("Posição:", numeros.index(busca))
else:
    print("Número não está na lista.")