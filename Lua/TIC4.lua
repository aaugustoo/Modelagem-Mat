-- Biblioteca utilizada no código para plotagem gráfica
Plotly = require("plotly")
GraficoX = Plotly.figure()
GraficoV = Plotly.figure()
GraficoXV = Plotly.figure()


-- Valor inicial do eixo horizontal de tempo (T0),
-- valor inicial da posição da massa (X0 no instante T0)
-- e valor inicial da velocidade (V0 no instante T0)
T0 = 0
X0 = 5
V0 = 0


-- Massa (M), constante elástica da mola (K), constante de amortecimento por atrito (A), 
-- comprimento da mola e posição de equilíbrio da massa (L)
M = 2
K = 2000
A = 6
L = 3


-- Valor do passo no eixo horizontal (eixo do tempo)
H = 0.01

-- Valor do limite superior do intervalo 0 <= t <= 1
Limite = 1.0


-- Inicialização da lista que contém os valores do eixo horizontal que farão pares ordenados com as soluções (Tempo)
Tempo = {}

-- Preenchimento da lista Tempo com valores partindo de t0 (condição inicial) e incrementando h até chegar ao limite superior do intervalo
Valor = T0
while Valor <= Limite 
do
    table.insert(Tempo, Valor)
    Valor = Valor + H
end


-- Inicialização das listas que irão conter os valores da posição da massa em um instante de tempo t (X)
-- e velocidade da massa em um instante de tempo t (V)
X = {}
V = {}


-- Função de variação (derivada) da posição da massa em um instante de tempo t,
-- x'(t) no modelo
function F1(t, x, v)
    local resultado = v
    return resultado
end

-- Função de variação (derivada) da velocidade da massa em um instante de tempo t,
-- v'(t) no modelo
function F2(t, x, v)
    local resultado = - K/M*x - A/M*v + K*L/M
    return resultado
end


-- Preenchimento da posição inicial (índice 1) de X e V com os valores da condição inicial do problema,
-- posição inicial X0 em X, velocidade inicial V0 em V
X[1] = X0
V[1] = V0


-- Preenchimento do restante das posições de X e V pelo método de Runge-Kutta,
-- preenchimento das posições da massa (X) em instantes do intervalo de tempo 0 <= t <= 1
-- e preenchimento da velocidade da massa (V) em instantes do intervalo de tempo 0 <= t <= 1,
-- a discretização e a distância entre os instantes t é definida pelo passo h
for n = 1, #Tempo - 1, 1
do
    -- Kn1 da posição da massa (K11) e da velocidade da massa (K21)
    K11 = F1(Tempo[n], X[n], V[n])
    K21 = F2(Tempo[n], X[n], V[n])

    -- Kn2 da posição da massa (K12) e da velocidade da massa (K22)
    K12 = F1(Tempo[n] + 1/2 * H, X[n] + 1/2 * H * K11, V[n] + 1/2 * H * K21)
    K22 = F2(Tempo[n] + 1/2 * H, X[n] + 1/2 * H * K11, V[n] + 1/2 * H * K21)

    -- Kn3 da posição da massa (K13) e da velocidade da massa (K23)
    K13 = F1(Tempo[n] + 1/2 * H, X[n] + 1/2 * H * K12, V[n] + 1/2 * H * K22)
    K23 = F2(Tempo[n] + 1/2 * H, X[n] + 1/2 * H * K12, V[n] + 1/2 * H * K22)

    -- Kn4 da posição da massa (K14) e da velocidade da massa (K24)
    K14 = F1(Tempo[n] + H, X[n] + H * K13, V[n] + H * K23)
    K24 = F2(Tempo[n] + H, X[n] + H * K13, V[n] + H * K23)

    -- Posição da massa (X)
    X[n+1] = X[n] + H * 1/6 * (K11 + 2*K12 + 2*K13 + K14)

    -- Velocidade da massa (V)
    V[n+1] = V[n] + H * 1/6 * (K21 + 2*K22 + 2*K23 + K24)
end


-- Plotagem gráfica

-- Gráfico das posições da massa (X) em relação ao tempo (Tempo)
GraficoX:plot{Tempo, X, mode="lines", ls="-", color="blue", name="posições da massa em função do tempo"}
GraficoX:plot{title="posições asssumidas pela massa no intervalo de tempo 0 <= t <= 1"}
GraficoX:plot{xlabel="tempo"}
GraficoX:plot{ylabel="posição"}
GraficoX:plot{legend="True"}
GraficoX:plot{grid="True"}:show()

-- Gráfico das velocidades da massa (V) em relação ao tempo (Tempo)
GraficoV:plot{Tempo, V, mode="lines", ls="-", color="red", name="velocidades da massa em função do tempo"}
GraficoV:plot{title="velocidades asssumidas pela massa no intervalo de tempo 0 <= t <= 1"}
GraficoV:plot{xlabel="tempo"}
GraficoV:plot{ylabel="velocidade"}
GraficoV:plot{legend="True"}
GraficoV:plot{grid="True"}:show()

-- Gráfico completo (posições e velocidades)
GraficoXV:plot{Tempo, X, mode="lines", ls="-", color="blue", name="posições da massa em função do tempo"}
GraficoXV:plot{Tempo, V, mode="lines", ls="-", color="red", name="velocidades da massa em função do tempo"}
GraficoXV:plot{title="posições e velocidades asssumidas pela massa no intervalo de tempo 0 <= t <= 1"}
GraficoXV:plot{xlabel="tempo"}
GraficoXV:plot{ylabel="posição/velocidade"}
GraficoXV:plot{legend="True"}
GraficoXV:plot{grid="True"}:show()