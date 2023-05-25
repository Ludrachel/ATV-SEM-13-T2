def soma_cumulativa(lis):
    soma = 0
    lis_nova = []
    for i in lis:
        soma += i
        lis_nova.append(soma)
    return lis_nova
num = []
while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)
    lis_nova = soma_cumulativa(num)
print(lis_nova)
    
