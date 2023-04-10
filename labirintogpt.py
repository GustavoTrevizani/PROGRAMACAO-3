import turtle
import random

# Cria uma janela para desenhar
window = turtle.Screen()
window.bgcolor('white')
window.title('Labirinto')

# Define as dimensões do labirinto
largura_celula = 20
altura_celula = 20
num_linhas = 20
num_colunas = 20

# Cria uma tartaruga para desenhar o labirinto
tartaruga = turtle.Turtle()
tartaruga.speed(0)
tartaruga.penup()

# Cria uma matriz para representar as células do labirinto
labirinto = []
for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        linha.append(1)
    labirinto.append(linha)

# Cria a função para desenhar uma célula do labirinto
def desenhar_celula(x, y):
    tartaruga.goto(x - largura_celula/2, y - altura_celula/2)
    tartaruga.begin_fill()
    for i in range(4):
        tartaruga.forward(largura_celula)
        tartaruga.left(90)
    tartaruga.end_fill()

# Cria a função para desenhar o labirinto
def desenhar_labirinto():
    for i in range(num_linhas):
        for j in range(num_colunas):
            if labirinto[i][j] == 1:
                x = j * largura_celula
                y = i * altura_celula
                desenhar_celula(x, y)

# Define as paredes do labirinto usando o algoritmo de Kruskal
paredes = []
for i in range(num_linhas):
    for j in range(num_colunas):
        if i > 0:
            paredes.append([(i, j), (i-1, j)])
        if j > 0:
            paredes.append([(i, j), (i, j-1)])
random.shuffle(paredes)

for parede in paredes:
    celula1 = parede[0]
    celula2 = parede[1]

    linha1 = celula1[0]
    coluna1 = celula1[1]
    linha2 = celula2[0]
    coluna2 = celula2[1]

    if labirinto[linha1][coluna1] != labirinto[linha2][coluna2]:
        labirinto[linha1][coluna1] = labirinto[linha2][coluna2] = 0
        x1 = coluna1 * largura_celula
        y1 = linha1 * altura_celula
        x2 = coluna2 * largura_celula
        y2 = linha2 * altura_celula
        tartaruga.color('white')
        tartaruga.goto(x1, y1)
        tartaruga.pendown()
        tartaruga.goto(x2, y2)
        tartaruga.penup()

# Desenha o labirinto final
tartaruga.color('black')
desenhar_labirinto()

# Esconde a tartaruga e finaliza o programa
tartaruga.hideturtle()
turtle.done()