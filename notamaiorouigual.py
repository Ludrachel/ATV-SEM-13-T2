notas = []
for i in range(50):
    nota = float(input())
    notas.append(nota)

notas_acima = []
for i in range(50):
    if notas[i] >= 6:
        notas_acima.append(i)
print(notas_acima)
