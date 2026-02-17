import math

def descobrir_quadrado(graos):
    return int(math.log2(graos)) + 1

graos = int(input("Informe o número de grãos: "))

print(descobrir_quadrado(graos))

# Complexidade de Tempo: O(1)