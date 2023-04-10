from turtle import Turtle, Screen
screen = Screen()
tartaruga = Turtle()
tartaruga.penup()

def quadrado (x, y, l):
    tartaruga.goto(x,y)
    tartaruga.pendown()
    tartaruga.goto (x + l, y)
    tartaruga.goto(x + l, y + l)
    tartaruga.goto(x, y + l)
    tartaruga.goto(x,y)
    tartaruga.penup()

#Esta é a função chamada ao se clicar
def clique(x,y):
    if -100 < x < 0 or 100 < x < 200:
        if -100 < y < 0 or -100 < x < 200:
            tartaruga.goto(x,y)
        else:
            print("Não posso ir ai")
    else:
        if 100 > y < 100:
            print("Não posso ir aí")

#Vamos setar um handler pra clique, note que ele retorna a posição x e y do mouse
quadrado (100,100,100)
quadrado (-100,100,100)
quadrado (100,-100,100)
quadrado (-100,-100,100) 

screen.onclick (clique)
screen.listen()
screen.mainloop()