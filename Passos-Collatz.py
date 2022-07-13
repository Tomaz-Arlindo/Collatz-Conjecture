### Importa bibliotecas para plot de gráfico e funções ###
import numpy as np
import matplotlib.pyplot as plt

### Cria o array par armazenar os valores dos passos e define o valor inicial de "c" ###
passos = []
c = 1
limite = int(input("defina quantas vezes quer rodar o programa: "))

### Calcula o número de passos para cada valor de "c" até o limite definido pelo usuário ###
for j in range(1, limite + 1):
    i = 0
    while c != 1:
        if (c % 2) == 0:
            c /= 2
        else:
            c = 3 * c + 1
        i += 1
    passos.append(i)
    c = j + 1 #Incrementa o valor de "c" e recomeça o ciclo
print(passos)


### Gráfico ###
### Cria figura define variaveis ###
fig, ax = plt.subplots(figsize = (20, 10))
nomefig = 'Teste-Collatz.png'
fsize = 20
xlab = 'Valor inicial'
ylab = 'Passos Nescessários'


### Eixo y - Número de passos ###
valores = np.array(passos)

### Formata gráfico ###
ax.plot(valores, marker = '.', ls = '', ms = 0.5, color = 'r')
ax.set_xlabel(xlab, fontsize = fsize)
ax.set_ylabel(ylab, fontsize = fsize)
ax.tick_params('y', )
ax.grid(color = 'black')

### Salvar figura ###
#fig.savefig(nomefig)

### Mostra o plot no terminal ###
plt.show()
