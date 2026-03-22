-- Biblioteca plotly realza a plotagem gráfica das soluções
Plotly = require("plotly")
Grafico = Plotly.figure()

-- Ponto de partida do PVI
local x0 = 0.0
local y0 = 1.0

-- Passo h no eixo x 
H = 0.1

-- Limite superior do eixo x
Limite = 5.0

-- Lista (tabela índice-valor) com os valores de x que são pares ordenados das soluções 
X = {}

-- Preenchimento da lista X
for Valor = x0, Limite, H 
do
    table.insert(X, Valor)
end

-- Cada Y representa uma lista com os resultados de cada método de resolução indicado
Y_Analitico = {}
Y_Euler = {}
Y_Runge_Kutta = {}

-- retorna o valor da derivada y' = f(x, y) = -y³
function f(x, y)
    local resultado = -(y * y * y)
    return resultado
end

-- Analítico
Y_Analitico[1] = y0
for n = 2, #X, 1
do
    Y_Analitico[n] = 1/(math.sqrt(2 * X[n] + 1))
end

-- Euler
Y_Euler[1] = y0
for n = 2, #X, 1
do
    Y_Euler[n] = Y_Euler[n - 1] + H * f(X[n - 1], Y_Euler[n - 1])
end

-- Runge-Kutta
Y_Runge_Kutta[1] = y0
for n = 2, #X, 1
do
    local Kn1 = f(X[n - 1], Y_Runge_Kutta[n - 1])
    local Kn2 = f(X[n - 1] + 1/2 * H, Y_Runge_Kutta[n - 1] + 1/2 * H * Kn1)
    local Kn3 = f(X[n - 1] + 1/2 * H, Y_Runge_Kutta[n - 1] + 1/2 * H * Kn2)
    local Kn4 = f(X[n - 1] + H, Y_Runge_Kutta[n - 1] + H * Kn3)

    Y_Runge_Kutta[n] = Y_Runge_Kutta[n - 1] + H * 1/6 * (Kn1 + 2*Kn2 + 2*Kn3 + Kn4)
end

-- Plotagem do gráfico
Grafico:plot{X, Y_Analitico, mode="lines+markers", marker={symbol="circle", color="green"}, ls="-", color="green", name="Solução Real"}
Grafico:plot{X, Y_Euler, mode="lines+markers", marker={symbol="circle", color="red"}, ls="--", color="red", name="Método de Euler"}
Grafico:plot{X, Y_Runge_Kutta, mode="lines+markers", marker={symbol="circle", color="blue"}, ls="--", color="blue", name="Método de Runge-Kutta"}

Grafico:plot{title="Gráfico com as resoluções do PVI {y' = -y³; y(0) = 1}, com h = 0.1 e 0 <= x <= 5"}
Grafico:plot{xlabel="Eixo x"}
Grafico:plot{ylabel="Eixo y"}
Grafico:plot{legend="True"}
Grafico:plot{grid="True"}:show()