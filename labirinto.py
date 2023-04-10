from turtle import Turtle, Screen
screen = Screen()
tartaruga = Turtle()

#FUNÇÕES DE MOVIMENTO
def movimento_direita():
    tartaruga.setheading(360)
    tartaruga.fd(20)
    limite(300,-100,90,-90)

def movimento_esquerda():
    tartaruga.setheading(180)
    tartaruga.fd(20)
    limite(300,-100,90,-90)

def movimento_cima():
    tartaruga.setheading(90)
    tartaruga.fd(20)
    limite(300,-100,90,-90)
    
def movimento_baixo():
    tartaruga.setheading(270)
    tartaruga.fd(20)
    limite(300,-100,90,-90)

#FUNÇÕES PARA CRIAR O LABIRINTO
def quadrado(tamanhoy,tamanhox,a1,b1):
    tartaruga.penup()
    tartaruga.goto(a1,b1)
    tartaruga.pendown()
    tartaruga.forward(tamanhoy) 
    tartaruga.left(90) 
    tartaruga.forward(tamanhox) 
    tartaruga.left(90) 
    tartaruga.forward(tamanhoy)
    tartaruga.left(90)
    tartaruga.forward(tamanhox)
    tartaruga.left(90)
    tartaruga.penup()
    tartaruga.goto(0,0)
    tartaruga.pendown()

#DEFINE OS VALORES DE LIMITE DO LABIRINTO
def limite(tamanhoycima,tamanhoybaixo,tamanhoxcima,tamanhoxbaixo):
    if(tartaruga.ycor() > tamanhoycima) or (tartaruga.ycor() < tamanhoybaixo) or (tartaruga.xcor() > tamanhoxcima) or (tartaruga.xcor() < tamanhoxbaixo):
        tartaruga.undo()
        tartaruga.home()
        tartaruga.write("Cuidado! Você não pode sair do quadrado!")

#DEFINE A POSIÇÃO DO "QUADRADO" DO LABIRINTO
quadrado(200,400,-100,-100)

#DEFINE AS TECLAS
screen.onkeypress(movimento_direita, "Right")
screen.onkeypress(movimento_esquerda, "Left")
screen.onkeypress(movimento_cima, "Up")
screen.onkeypress(movimento_baixo, "Down")

tartaruga.penup()
screen.listen()
screen.mainloop()