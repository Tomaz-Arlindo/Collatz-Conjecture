###Importa bibliotecas de gráfico e funções###
import numpy as np
import matplotlib.pyplot as plt

###### Código Caulculadora Conjectura de Collatz ######
c = int(input("Digite um número para o teste de Collatz: "))
i = 0

### Cria o array para inserir os valores intermediarios de "c" ###
collatz = []

### Calcula os valores de "c" e insere-os no array "collatz" ###
while c != 1:
    if (c % 2) == 0:
        c /= 2
        collatz.append(int(c))
    else:
        c = 3 * c + 1
        collatz.append(int(c))
    i += 1
print(collatz)
print(f"Passos necessarios:{i}")


###GRÁFICO###
### Cria gráfico define formatação ###
fig, ax = plt.subplots(figsize = (9, 6))
nomefig = 'Teste-Collatz.png'
fsize = 20
xlab = f'Número de Passos = {i}'
ylab = 'Valores Intermediários'

### Eixo y - valores intermediários ###
valores = np.array(collatz)

### Formatação do gráfico ###
ax.plot(valores, marker = 'o', ls = '-', ms = 5, color = 'r')
ax.set_xlabel(xlab, fontsize = fsize) 
ax.set_ylabel(ylab, fontsize = fsize)
ax.tick_params('y', )
ax.grid(color = 'b')

### Salvar figura ###
#fig.savefig(nomefig)

### Plota o gráfico no terminal ###
plt.show()
