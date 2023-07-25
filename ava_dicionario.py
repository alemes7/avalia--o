import os

print("listar os 6 números")

numeros = [3, 1, 4, 6, 2, 5]
valor = numeros[0]
for N in numeros:
    print(N)

dicio_matriz = {
    (0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0,
    (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0,
    (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0,
    (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0
}
print("Essa é a matriz sem alteração:\n", dicio_matriz, "\n","\n")

print("Essa é a matriz com alteração.\n")
dicio_matriz[(3, 1)] = numeros[3]
dicio_matriz[(1, 2)] = numeros[1]
dicio_matriz[(0, 0)] = numeros[4]
dicio_matriz[(0, 3)] = numeros[5]
dicio_matriz[(2, 2)] = numeros[2]
dicio_matriz[(3, 3)] = numeros[5]
print(dicio_matriz)

os.system("pause")
