def multiplica_constante(lis, constante):
    lis_nova = []
    for num in lis:
        lis_nova.append(num * constante)
    return lis_nova

numeros = []
while True:
    n = int(input())
    if n == 0:
        break
    numeros.append(n)

constante = int(input())
lis_nova = multiplica_constante(numeros, constante)

print(lis_nova)
