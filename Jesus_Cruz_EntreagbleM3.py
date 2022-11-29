import numpy as np
import matplotlib.pyplot as plt
from random import randint
niveles = 12
columna = [0]*(niveles)
for h in range(3000):
  stored = -1
  for j in range(niveles):
    stored += randint(0, 1)
  columna[stored] += 1
print('Se arrojaron 3000 canicas')
print(columna)
plt.suptitle('Simulacion de maquina de Galton')
plt.xlabel('Distribucion de canicas')
plt.ylabel('Cantidad de canicas')
plt.bar(np.arange(0, 12), columna, width=.7)
plt.show()