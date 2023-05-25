lis = []
for i in range(100):
    lis.append(int(input()))
    lista_ordenada = sorted(lis)

lis_nova = []
for i in range(len(lista_ordenada)):
    if i % 2 == 0:
        lis_nova.append(lista_ordenada[i] * 3)
    else:
        lis_nova.append(lista_ordenada[i] * 5)
print(lis_nova)
