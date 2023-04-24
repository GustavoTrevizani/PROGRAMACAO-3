import tkinter as tk
    
def Funcao_1():
    texto.config (text = "7")
def Funcao_2():
    texto.config (text = "4")
def Funcao_3():
    texto.config (text = "1")
def Funcao_4():
    texto.config (text = "0")
def Funcao_5():
    texto.config (text = "8")
def Funcao_6():
    texto.config (text = "5")
def Funcao_7():
    texto.config (text = "2")
def Funcao_8():
    texto.config (text = ",")
def Funcao_9():
    texto.config (text = "9")
def Funcao_10():
    texto.config (text = "6")
def Funcao_11():
    texto.config (text = "3")
def Funcao_12():
    texto.config (text = "=")
def Funcao_13():
    texto.config (text = ":")
def Funcao_14():
    texto.config (text = "x")
def Funcao_15():
    texto.config (text = "-")
def Funcao_16():
    texto.config (text = "+")

def soma(self):
    num1 = self.numero1.get()
    num2 = self.numero2.get()
    resul = num1 + num2
    self.resultado.set(resul)
    
def sub():
    num1 = sub.numero1.get()
    num2 = sub.numero2.get()
    resul = num1 - num2
    self.resultado.set(resul)
    
def mult():
    num1 = mult.numero1.get()
    num2 = mult.numero2.get()
    resul = num1 * num2
    mult.resultado.set(resul)
    
def div():
    num1 = div.numero1.get()
    num2 = div.numero2.get()
    resul = round((num1 / num2),2)
    div.resultado.set(resul)

janela = tk.Tk()
janela.geometry("300x300")
texto = tk.Label (janela, text="Seja bem-vindo a calculadora!")

texto.pack(side='top')

quadro_1 = tk.Frame(janela)
quadro_2 = tk.Frame(janela)
quadro_3 = tk.Frame(janela)
quadro_4 = tk.Frame(janela)

botao_1 = tk.Button(quadro_1, command = Funcao_1, text='7')
botao_1.pack(side = 'top', fill='both', expand=1)
botao_2 = tk.Button(quadro_1, command = Funcao_2, text='4')
botao_2.pack(side = 'top', fill='both', expand=1)
botao_3 = tk.Button(quadro_1, command = Funcao_3, text='1')
botao_3.pack(side = 'top', fill='both', expand=1)
botao_4 = tk.Button(quadro_1, command = Funcao_4, text='0')
botao_4.pack(side = 'top', fill='both', expand=1)
botao_5 = tk.Button(quadro_2, command = Funcao_5, text='8')
botao_5.pack(side = 'top', fill='both', expand =1)
botao_6 = tk.Button(quadro_2, command = Funcao_6, text='5')
botao_6.pack(side = 'top', fill='both', expand =1)
botao_7 = tk.Button(quadro_2, command = Funcao_7, text='2')
botao_7.pack(side = 'top', fill='both', expand =1)
botao_8 = tk.Button(quadro_2, command = Funcao_8, text=',')
botao_8.pack(side = 'top', fill='both', expand =1)
botao_9 = tk.Button(quadro_3, command = Funcao_9, text='9')
botao_9.pack(side = 'top', fill='both', expand =1)
botao_10 = tk.Button(quadro_3, command = Funcao_10, text='6')
botao_10.pack(side = 'top', fill='both', expand =1)
botao_11 = tk.Button(quadro_3, command = Funcao_11, text='3')
botao_11.pack(side = 'top', fill='both', expand =1)
botao_12 = tk.Button(quadro_3, command = Funcao_12, text='=')
botao_12.pack(side = 'top', fill='both', expand =1)
botao_13 = tk.Button(quadro_4, command = div, text=':')
botao_13.pack(side = 'top', fill='both', expand =1)
botao_14 = tk.Button(quadro_4, command = mult, text='x')
botao_14.pack(side = 'top', fill='both', expand =1)
botao_15 = tk.Button(quadro_4, command = sub, text='-')
botao_15.pack(side = 'top', fill='both', expand =1)
botao_16 = tk.Button(quadro_4, command = soma, text='+')
botao_16.pack(side = 'top', fill='both', expand =1)

quadro_1.pack(side='left', fill='both', expand=1)
quadro_2.pack(side='left', fill='both', expand=1)
quadro_3.pack(side='left', fill='both', expand=1)
quadro_4.pack(side='left', fill='both', expand=1)

janela.mainloop()
