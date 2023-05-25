def esta_ordenado(lis):
    if sorted(lis) == lis:
        return True
    else:
        return False

n = int(input())
num = []

for i in range(n):
    num.append(float(input()))
if esta_ordenado(num):
    print("LISTA ORDENADA")
else:
    print("LISTA NÃO ORDENADA")

        
