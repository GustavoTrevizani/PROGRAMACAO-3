num_lista = []

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    num_lista.append(num)

sorted_lista = sorted(num_lista, reverse=True)

print("Lista de números inseridos, ordenada:", sorted_lista)
