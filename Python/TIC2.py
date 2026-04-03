# Biblioteca utilizada no código para plotagem gráfica
import matplotlib.pyplot as grafico


# Valores iniciais para o eixo de tempo (t0), para a quantidade de predadores (x0) e para a quantidade de presas (y0)
t0 = 0
x0 = 4
y0 = 4


# Valores das constantes presentes nas derivadas x' e y' (a, b, c, d)
a = 0.16
b = 0.08
c = 0.9
d = 4.5


# Valor do passo no eixo horizontal (eixo do tempo)
h = 0.001


# Valor do limite superior do intervalo 0 <= t <= 16
limite = 16


# Inicialização da lista que contém os valores do eixo horizontal que farão pares ordenados com as soluções (Tempo),
# da lista que contém a quantidade de predadores em um instante t (Xpreda)
# e da lista que contém a quantidade de presas em um instante t (Ypresa)
Tempo = []
Xpreda = []
Ypresa = []


# Preenchimento da lista Tempo com valores partindo de t0 (condição inicial) e incrementando h até chegar no limite superior do intervalo
valor = t0
while valor <= limite:
    Tempo.append(valor)
    valor += h


# As listas Xpreda e Ypresa tem a mesma quantidade de posições que a lista Tempo,
# por isso serão preenchidas inicialmente com 0 na quantidade de posições que a lista Tempo possui,
# isso permitirá a manipulação de índices em Xpreda e Ypresa posteriormente no código
Xpreda = [0] * len(Tempo)
Ypresa = [0] * len(Tempo)


# Preenchimento das posições iniciais (índice 0) de Xpreda e Ypresa com os valores da condição inicial do problema
Xpreda[0] = x0
Ypresa[0] = y0


# Funções de variação (derivadas) da quantidade de predadores (f1) e da quantidade de presas (f2)
def f1(t, x, y):
    resultado = -a*x + b*x*y
    return resultado

def f2(t, x, y):
    resultado = d*y - c*x*y
    return resultado


# Preenchimento do restante das posições das listas Xpreda e Ypresa utilizando o método de Euler
n = 0
while n < len(Tempo) - 1:
    # Lista da quantidade de predadores em um instante t
    Xpreda[n+1] = Xpreda[n] + h*f1(Tempo[n], Xpreda[n], Ypresa[n])

    # Lista da quantidade de presas em um instante t
    Ypresa[n+1] = Ypresa[n] + h*f2(Tempo[n], Xpreda[n], Ypresa[n])

    n += 1


# Plotagem gráfica
grafico.plot(Tempo, Xpreda, linestyle='-', color='r', label='Predadores')
grafico.plot(Tempo, Ypresa, linestyle='-', color='b', label='Presas')

grafico.title('Modelo Predador-Presa pelo método de Euler')
grafico.xlabel('Tempo')
grafico.ylabel('Quantidade de predadores/presas')

grafico.grid(True)
grafico.legend()
grafico.show()