# Biblioteca utilizada para a plotagem gráfica
import matplotlib.pyplot as GraficoX
import matplotlib.pyplot as GraficoV
import matplotlib.pyplot as GraficoXV


# Valor inicial do eixo horizontal de tempo (t0),
# valor inicial da posição da massa (x0 no instante t0)
# e valor inicial da velocidade (v0 no instante t0)
t0 = 0
x0 = 5
v0 = 0


# Massa (m), constante elástica da mola (k), constante de amortecimento por atrito (a), 
# comprimento da mola e posição de equilíbrio da massa (L) 
m = 2
k = 2000
a = 6
L = 3


# Valor do passo no eixo horizontal (eixo do tempo)
h = 0.01

# Valor do limite superior do intervalo 0 <= t <= 1
limite = 1.0


# Inicialização da lista que contém os valores do eixo horizontal que farão pares ordenados com as soluções (Tempo)
Tempo = []

# Preenchimento da lista Tempo com valores partindo de t0 (condição inicial) e incrementando h até chegar ao limite superior do intervalo
valor = t0
while valor <= limite:
    Tempo.append(valor)
    valor += h


# Inicialização das listas que irão conter os valores da posição da massa em um instante de tempo t (X)
# e velocidade da massa em um instante de tempo t (V),
# ambas foram inicializadas com a mesma quantidade de posições da lista Tempo, com o valor 0 em todas as suas posições
X = [0] * len(Tempo)
V = [0] * len(Tempo)


# Função de variação (derivada) da posição da massa em um instante de tempo t,
# x'(t) no modelo
def f1(t, x, v):
    resultado = v
    return resultado

# Função de variação (derivada) da velocidade da massa em um instante de tempo t,
# v'(t) no modelo
def f2(t, x, v):
    resultado = - k/m*x - a/m*v + k*L/m
    return resultado


# Preenchimento das posições iniciais (indície 0) de X e V com os valores da condição inicial do problema,
# posição inicial x0 em X, velocidade inicial v0 em V
X[0] = x0
V[0] = v0


# Preenchimento do restante das posições de X e V pelo método de Runge-Kutta,
# preenchimento das posições da massa (X) em instantes do intervalo de tempo 0 <= t <= 1
# e preenchimento da velocidade da massa (V) em instantes do intervalo de tempo 0 <= t <= 1,
# a discretização e a distância entre os instantes t é definida pelo passo h
n = 0
while n < len(Tempo) - 1:
    # Kn1 da posição da massa (K11) e da velocidade da massa (K21)
    K11 = f1(Tempo[n], X[n], V[n])
    K21 = f2(Tempo[n], X[n], V[n])

    # Kn2 da posição da massa (K12) e da velocidade da massa (K22)
    K12 = f1(Tempo[n] + 1/2 * h, X[n] + 1/2 * h * K11, V[n] + 1/2 * h * K21)
    K22 = f2(Tempo[n] + 1/2 * h, X[n] + 1/2 * h * K11, V[n] + 1/2 * h * K21)

    # Kn3 da posição da massa (K13) e da velocidade da massa (K23)
    K13 = f1(Tempo[n] + 1/2 * h, X[n] + 1/2 * h * K12, V[n] + 1/2 * h * K22)
    K23 = f2(Tempo[n] + 1/2 * h, X[n] + 1/2 * h * K12, V[n] + 1/2 * h * K22)

    # Kn4 da posição da massa (K14) e da velocidade da massa (K24)
    K14 = f1(Tempo[n] + h, X[n] + h * K13, V[n] + h * K23)
    K24 = f2(Tempo[n] + h, X[n] + h * K13, V[n] + h * K23)

    # Posição da massa (X)
    X[n+1] = X[n] + h * 1/6 * (K11 + 2*K12 + 2*K13 + K14)

    # Velocidade da massa (V)
    V[n+1] = V[n] + h * 1/6 * (K21 + 2*K22 + 2*K23 + K24)

    n += 1


# Plotagem gráfica

# Gráfico das posições da massa (X) em relação ao tempo (Tempo) 
GraficoX.plot(Tempo, X, linestyle= '-', color='b', label='posições da massa em função do tempo')
GraficoX.title('posições asssumidas pela massa no intervalo de tempo 0 <= t <= 1')
GraficoX.xlabel('tempo')
GraficoX.ylabel('posição')
GraficoX.grid(True)
GraficoX.legend()
GraficoX.show()

# Gráfico das velocidades da massa (V) em relação ao tempo (Tempo) 
GraficoV.plot(Tempo, V, linestyle= '-', color='r', label='velocidades da massa em função do tempo')
GraficoV.title('velocidades asssumidas pela massa no intervalo de tempo 0 <= t <= 1')
GraficoV.xlabel('tempo')
GraficoV.ylabel('velocidade')
GraficoV.grid(True)
GraficoV.legend()
GraficoV.show()

# Gráfico completo (posições e velocidades)
GraficoXV.plot(Tempo, X, linestyle= '-', color='b', label='posições da massa em função do tempo')
GraficoXV.plot(Tempo, V, linestyle= '-', color='r', label='velocidades da massa em função do tempo')
GraficoXV.title('posições e velocidades asssumidas pela massa no intervalo de tempo 0 <= t <= 1')
GraficoXV.xlabel('tempo')
GraficoXV.ylabel('posição/velocidade')
GraficoXV.grid(True)
GraficoXV.legend()
GraficoXV.show() 