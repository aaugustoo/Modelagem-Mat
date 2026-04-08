-- Biblioteca utilizada no código para plotagem gráfica
Plotly = require("plotly")
Grafico = Plotly.figure()


-- Valores iniciais para o eixo de tempo (t0), 
-- para a quantidade de elementos da espécie 1 (x0) 
-- e para a quantidade de elementos da espécie 2 (y0)
T0 = 0
X0 = 5.0
Y0 = 3.0


-- Valores das constantes presentes na derivada x' (a1, b1, c1)
A1 = 1.0
B1 = 0.1
C1 = 0.05

-- Valores das constantes presentes na derivada y' (a2, b2, c2)
A2 = 1.7
B2 = 0.1
C2 = 0.15


-- Valor do passo no eixo horizontal (eixo do tempo)
H = 0.01

-- Valor do limite superior do intervalo 0 <= t <= 60
Limite = 60


-- Inicialização da lista que contém os valores do eixo horizontal que farão pares ordenados com as soluções (Tempo)
Tempo = {}

-- Preenchimento da lista Tempo com valores partindo de t0 (condição inicial) e incrementando h até chegar no limite superior do intervalo
Valor = T0
while Valor <= Limite
do
    table.insert(Tempo, Valor)
    Valor = Valor + H
end


-- Listas que posteriormente terão as quantidades das espécies 1 (Xe) e 2 (Ye) em relação ao tempo usando o método de Euler
Xe = {}
Ye = {}

-- Listas que posteriormente terão as quantidades das espécies 1 (Xrk) e 2 (Yrk) em relação ao tempo usando o método de Runge-Kutta
Xrk = {}
Yrk = {}


-- Função de variação (derivada) da quantidade de elementos da espécie 1, 
-- x' no modelo
function F1(t, x, y)
    local resultado = A1*x - B1*(x*x) - C1*x*y
    return resultado
end

-- Função de variação (derivada) da quantidade de elementos da espécie 2, 
-- y' no modelo
function F2(t, x, y)
    local resultado = A2*y - B2*(y*y) - C2*x*y
    return resultado
end


-- Preenchimento das posições iniciais (índice 1) de Xe e Xrk com o valor da condição inicial do problema,
-- quantidade de elementos inicial da espécie 1
Xe[1] = X0
Xrk[1] = X0

-- Preenchimento das posições iniciais (índice 1) de Ye e Yrk com o valor da condição inicial do problema,
-- quantidade de elementos inicial da espécie 2
Ye[1] = Y0
Yrk[1] = Y0


-- Preenchimento do restante das posições das listas Xe e Ye utilizando o método de Euler,
-- quantidades dos elementos das espécies 1 e 2 em relação ao tempo pelo método de Euler
for n = 1, #Tempo - 1, 1
do
    -- Espécie 1 (Xe)
    Xe[n+1] = Xe[n] + H*F1(Tempo[n], Xe[n], Ye[n])

    -- Espécie 2 (Ye)
    Ye[n+1] = Ye[n] + H*F2(Tempo[n], Xe[n], Ye[n])
end


-- Preenchimento do restante das posições das listas Xrk e Yrk utilizando o método de Runge-Kutta,
-- quantidades dos elementos das espécies 1 e 2 em relação ao tempo pelo método de Runge-Kutta
for n = 1, #Tempo - 1, 1
do
    -- Kn1 da espécie 1 (K11) e Kn1 da espécie 2 (K21)
    K11 = F1(Tempo[n], Xrk[n], Yrk[n])
    K21 = F2(Tempo[n], Xrk[n], Yrk[n])

    -- Kn2 da espécie 1 (K12) e Kn2 da espécie 2 (K22)
    K12 = F1(Tempo[n] + 1/2 * H, Xrk[n] + 1/2 * H * K11, Yrk[n] + 1/2 * H * K21)
    K22 = F2(Tempo[n] + 1/2 * H, Xrk[n] + 1/2 * H * K11, Yrk[n] + 1/2 * H * K21)

    -- Kn3 da espécie 1 (K13) e Kn3 da espécie 2 (K23)
    K13 = F1(Tempo[n] + 1/2 * H, Xrk[n] + 1/2 * H * K12, Yrk[n] + 1/2 * H * K22)
    K23 = F2(Tempo[n] + 1/2 * H, Xrk[n] + 1/2 * H * K12, Yrk[n] + 1/2 * H * K22)

    -- Kn4 da espécie 1 (K14) e Kn4 da espécie 2 (K24)
    K14 = F1(Tempo[n] + H, Xrk[n] + H * K13, Yrk[n] + H * K23)
    K24 = F2(Tempo[n] + H, Xrk[n] + H * K13, Yrk[n] + H * K23)

    -- Espécie 1 (Xrk)
    Xrk[n+1] = Xrk[n] + H * 1/6 * (K11 + 2*K12 + 2*K13 + K14)

    -- Espécie 2 (Yrk)
    Yrk[n+1] = Yrk[n] + H * 1/6 * (K21 + 2*K22 + 2*K23 + K24)
end


-- Plotagem gráfica

-- Espécie 1
Grafico:plot{Tempo, Xe, mode="lines", ls="-", color="green", name="Espécie 1 por Euler"}
Grafico:plot{Tempo, Xrk, mode="lines", ls="-", color="red", name="Espécie 1 por Runge-Kutta"}

-- Espécie 2
Grafico:plot{Tempo, Ye, mode="lines", ls="-", color="yellow", name="Espécie 2 por Euler"}
Grafico:plot{Tempo, Yrk, mode="lines", ls="-", color="blue", name="Espécie 2 por Runge-Kutta"}

Grafico:plot{title="Modelo de competição entre espécies - Euler e Runge-Kutta"}
Grafico:plot{xlabel="tempo"}
Grafico:plot{ylabel="quantidade de elementos das espécies"}

Grafico:plot{legend="True"}
Grafico:plot{grid="True"}:show()