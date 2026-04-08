# Biblioteca utilizada no código para plotagem gráfica
import matplotlib.pyplot as grafico


# Valores iniciais para o eixo de tempo (t0), 
# para a quantidade de elementos da espécie 1 (x0) 
# e para a quantidade de elementos da espécie 2 (y0)
t0 = 0
x0 = 5.0
y0 = 3.0


# Valores das constantes presentes na derivada x' (a1, b1, c1)
a1 = 1.0
b1 = 0.1
c1 = 0.05

# Valores das constantes presentes na derivada y' (a2, b2, c2)
a2 = 1.7
b2 = 0.1
c2 = 0.15


# Valor do passo no eixo horizontal (eixo do tempo)
h = 0.01

# Valor do limite superior do intervalo 0 <= t <= 60
limite = 60


# Inicialização da lista que contém os valores do eixo horizontal que farão pares ordenados com as soluções (Tempo)
Tempo = []

# Preenchimento da lista Tempo com valores partindo de t0 (condição inicial) e incrementando h até chegar no limite superior do intervalo
valor = t0
while valor <= limite:
    Tempo.append(valor)
    valor += h


# Listas que contém as quantidades das espécies 1 (Xe) e 2 (Ye) em relação ao tempo usando o método de Euler,
# ambas foram inicializadas com a mesma quantidade de posições da lista Tempo, com o valor 0 em todas as suas posições
Xe = [0] * len(Tempo)
Ye = [0] * len(Tempo)

# Listas que contém as quantidades das espécies 1 (Xrk) e 2 (Yrk) em relação ao tempo usando o método de Runge-Kutta,
# ambas foram inicializadas com a mesma quantidade de posições da lista Tempo, com o valor 0 em todas as suas posições
Xrk = [0] * len(Tempo)
Yrk = [0] * len(Tempo)


# Função de variação (derivada) da quantidade de elementos da espécie 1, 
# x' no modelo
def f1(t, x, y):
    resultado = a1*x - b1*(x*x) - c1*x*y
    return resultado

# Função de variação (derivada) da quantidade de elementos da espécie 2,
# y' no modelo
def f2(t, x, y):
    resultado = a2*y - b2*(y*y) - c2*x*y
    return resultado


# Preenchimento das posições iniciais (índice 0) de Xe e Xrk com o valor da condição inicial do problema,
# quantidade de elementos inicial da espécie 1
Xe[0] = x0
Xrk[0] = x0

# Preenchimento das posições iniciais (índice 0) de Ye e Yrk com o valor da condição inicial do problema,
# quantidade de elementos inicial da espécie 2
Ye[0] = y0
Yrk[0] = y0


# Preenchimento do restante das posições das listas Xe e Ye utilizando o método de Euler,
# quantidades dos elementos das espécies 1 e 2 em relação ao tempo pelo método de Euler
n = 0
while n < len(Tempo) - 1:
    # Espécie 1 (Xe)
    Xe[n+1] = Xe[n] + h*f1(Tempo[n], Xe[n], Ye[n])

    # Espécie 2 (Ye)
    Ye[n+1] = Ye[n] + h*f2(Tempo[n], Xe[n], Ye[n])

    n += 1


# Preenchimento do restante das posições das listas Xrk e Yrk utilizando o método de Runge-Kutta,
# quantidades dos elementos das espécies 1 e 2 em relação ao tempo pelo método de Runge-Kutta
n = 0
while n < len(Tempo) - 1:
    # Kn1 da espécie 1 (Kn11) e Kn1 da espécie 2 (Kn21)
    Kn11 = f1(Tempo[n], Xrk[n], Yrk[n])
    Kn21 = f2(Tempo[n], Xrk[n], Yrk[n])

    # Kn2 da espécie 1 (Kn12) e Kn2 da espécie 2 (Kn22)
    Kn12 = f1(Tempo[n] + 1/2 * h, Xrk[n] + 1/2 * h * Kn11, Yrk[n] + 1/2 * h * Kn21)
    Kn22 = f2(Tempo[n] + 1/2 * h, Xrk[n] + 1/2 * h * Kn11, Yrk[n] + 1/2 * h * Kn21)

    # Kn3 da espécie 1 (Kn13) e Kn3 da espécie 2 (Kn23)
    Kn13 = f1(Tempo[n] + 1/2 * h, Xrk[n] + 1/2 * h * Kn12, Yrk[n] + 1/2 * h * Kn22)
    Kn23 = f2(Tempo[n] + 1/2 * h, Xrk[n] + 1/2 * h * Kn12, Yrk[n] + 1/2 * h * Kn22)

    # Kn4 da espécie 1 (Kn14) e Kn4 da espécie 2 (Kn24)
    Kn14 = f1(Tempo[n] + h, Xrk[n] + h * Kn13, Yrk[n] + h * Kn23)
    Kn24 = f2(Tempo[n] + h, Xrk[n] + h * Kn13, Yrk[n] + h * Kn23)

    # Espécie 1 (Xrk)
    Xrk[n+1] = Xrk[n] + h * 1/6 * (Kn11 + 2*Kn12 + 2*Kn13 + Kn14)

    # Espécie 2 (Yrk)
    Yrk[n+1] = Yrk[n] + h * 1/6 * (Kn21 + 2*Kn22 + 2*Kn23 + Kn24)

    n += 1


# Plotagem gráfica

# Espécie 1
grafico.plot(Tempo, Xe, linestyle='-', color='g', label='Espécie 1 por Euler')
grafico.plot(Tempo, Xrk, linestyle='-', color='r', label='Espécie 1 por Runge-Kutta')

# Espécie 2
grafico.plot(Tempo, Ye, linestyle='-', color='y', label='Espécie 2 por Euler')
grafico.plot(Tempo, Yrk, linestyle='-', color='b', label='Espécie 2 por Runge-Kutta')

grafico.title('Modelo de competição entre espécies - Euler e Runge-Kutta')
grafico.xlabel('Tempo')
grafico.ylabel('Quantidade de elementos das espécies')

grafico.grid(True)
grafico.legend()
grafico.show()