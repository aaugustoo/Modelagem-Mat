# Resolução do PVI {y' = -y³; y(0) = 1} usando os métodos de Euler e Runge-Kutta.
# Gráfico apresentando a diferença de resultado entre o método analítico, de Euler e de Runge-Kutta.

# Import da biblioteca de matemática e da biblioteca de plotagen
import math
import matplotlib.pyplot as grafico

# Ponto fornecido pelo PVI
x0 = 0.0
y0 = 1.0

# Limite do intervalo (0 <= x <= 5)
limite = 5.0

# Passo h
h = 0.1

# Valores do eixo x estarão contidos na lista X
X = []

# Preenchimento de X
valor = x0
while valor <= limite:
    X.append(valor)
    valor += h


# Cada Y representa uma lista com os resultados de cada método de resolução indicado
# Inicialmente são preenchidas com 0 em todas as posições para evitar erros de indície em atribuições futuras
# len(X) é o tamanho da lista X já preenchida, as listas Y devem ter o mesmo tamanho de X para que a resolução esteja correta
Y_Analitico = [0] * len(X)
Y_Euler = [0] * len(X)
Y_Runge_Kutta = [0] * len(X)


# Derivada y' = f(x,y) = -y³
def f(x, y):
    resultado = -(y ** 3)
    return resultado


# Resolução analítica, Y_Analitico começa recebendo y0 na primeira posição graças ao PVI
Y_Analitico[0] = y0
n = 1
while n <= len(X) - 1:
    Y_Analitico[n] = 1/(math.sqrt(2 * X[n] + 1))
    n += 1


# Resolução pelo método de Euler, Y_Euler começa recebendo y0 na primeira posição por definição
# y(n) = y(n-1) + h * f(Xn-1, Yn-1)
Y_Euler[0] = y0
n = 1
while n <= len(X) - 1:
    Y_Euler[n] = Y_Euler[n - 1] + h * f(X[n - 1], Y_Euler[n - 1])
    n += 1


# Resolução pelo método de Runge-Kutta, Y_Runge_Kutta começa recebendo y0 na primeira posição por definição
# y(n) = y(n-1) + 1/6 * h * (Kn1 + 2Kn2 + 2Kn3 + Kn4)
Y_Runge_Kutta[0] = y0
n = 1
while n <= len(X) - 1:
    Kn1 = f(X[n - 1], Y_Runge_Kutta[n - 1])
    Kn2 = f(X[n - 1] + 1/2 * h, Y_Runge_Kutta[n - 1] + 1/2 * h * Kn1)
    Kn3 = f(X[n - 1] + 1/2 * h, Y_Runge_Kutta[n - 1] + 1/2 * h * Kn2)
    Kn4 = f(X[n - 1] + h, Y_Runge_Kutta[n - 1] + h * Kn3)

    Y_Runge_Kutta[n] = Y_Runge_Kutta[n - 1] + h * 1/6 * (Kn1 + 2*Kn2 + 2*Kn3 + Kn4)
    n += 1


# Plotagem do gráfico com os resultados dos três métodos
grafico.plot(X, Y_Runge_Kutta, marker='o', linestyle='--', color='b', label='Método de Runge-Kutta')
grafico.plot(X, Y_Euler, marker='o', linestyle='--', color='r', label='Método de Euler')
grafico.plot(X, Y_Analitico, marker='o', linestyle='-', color='g', label='Solução Exata')

grafico.title('Gráfico com as resoluções do PVI {y\' = -y³; y(0) = 1}, com h = 0.1 e 0 <= x <= 5')
grafico.xlabel('Eixo x')
grafico.ylabel('Eixo y')

grafico.grid(True)
grafico.legend()
grafico.show()