-- Biblioteca plotly para a realização da plotagem gráfica
Plotly = require("plotly")
Grafico = Plotly.figure()


-- Valores iniciais para o eixo de tempo (T0), para a quantidade de predadores (X0) e para a quantidade de presas (Y0)
T0 = 0
X0 = 4
Y0 = 4


-- Valores das constantes presentes nas derivadas x' e y' (a, b, c, d)
A = 0.16
B = 0.08
C = 0.9
D = 4.5


-- Valor do passo no eixo horizontal (eixo do tempo)
H = 0.001


-- Valor do limite superior do intervalo 0 <= t <= 16
Limite = 16


-- Inicialização das listas (tabelas indicie-valor) que contém os valores do eixo horizontal (Tempo),
-- da quantidade de predadores em um instante t (Xpreda)
-- e da quantidade de presas em um instante t (Ypresa)
Tempo = {}
Xpreda = {}
Ypresa = {}


-- Preenchimento da lista Tempo com valores partindo de t0 (condição inicial) e incrementando h até chegar no limite superior do intervalo
Valor = T0
while Valor <= Limite
do
    table.insert(Tempo, Valor)
    Valor = Valor + H
end


-- Inicialização de Xpreda e Ypresa com os valores da condição inicial, lua tem o indicie 1 como o inicial
Xpreda[1] = X0
Ypresa[1] = Y0


-- Funções de variação (derivadas) da quantidade de predadores (F1) e da quantidade de presas (F2)
function F1(t, x, y)
    local resultado = -A*x + B*x*y
    return resultado
end

function F2(t, x, y)
    local resultado = D*y - C*x*y
    return resultado
end


-- Preenchimento do restante das posições das listas Xpreda e Ypresa utilizando o método de Euler
for n = 1, #Tempo - 1, 1
do
    -- Lista da quantidade de predadores em um instante t
    Xpreda[n+1] = Xpreda[n] + H*F1(Tempo[n], Xpreda[n], Ypresa[n])

    -- Lista da quantidade de presas em um instante t
    Ypresa[n+1] = Ypresa[n] + H*F2(Tempo[n], Xpreda[n], Ypresa[n])
end


-- Plotagem gráfica
Grafico:plot{Tempo, Xpreda, mode="lines", ls="-", color="red", name="Predadores"}
Grafico:plot{Tempo, Ypresa, mode="lines", ls="-", color="blue", name="Presas"}

Grafico:plot{title="Modelo Predador-Presa pelo método de Euler"}
Grafico:plot{xlabel="tempo"}
Grafico:plot{ylabel="quantidade de predadores/presas"}

Grafico:plot{legend="True"}
Grafico:plot{grid="True"}:show()