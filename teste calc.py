import tkinter as tk

def Funcao_1():
    texto.config(text="7")

def Funcao_2():
    texto.config(text="4")

def Funcao_3():
    texto.config(text="1")

def Funcao_4():
    texto.config(text="0")

def Funcao_5():
    texto.config(text="8")

def Funcao_6():
    texto.config(text="5")

def Funcao_7():
    texto.config(text="2")

def Funcao_8():
    num1 = float(texto["text"])
    num2 = float(texto["text"])
    botao_12.config(command=ponto)
    return num1

def Funcao_9():
    texto.config(text="9")

def Funcao_10():
    texto.config(text="6")

def Funcao_11():
    texto.config(text="3")

def Funcao_12():
    num1 = float(texto["text"])
    botao_12.config(command=igual)
    return num1

def Funcao_13():
    num1 = float(texto["text"])
    botao_12.config(command=div)
    return num1

def Funcao_14():
    num1 = float(texto["text"])
    botao_12.config(command=mult)
    return num1

def Funcao_15():
    num1 = float(texto["text"])
    botao_12.config(command=sub)
    return num1

def Funcao_16():
    num1 = float(texto["text"])
    botao_12.config(command=soma)
    return num1

def Funcao_17():
    texto.config(text="")

def ponto():
    global num1
    if '.' not in texto["text"]:
        texto.config(text=num1+".")
    botao_12.config(command=Funcao_12)
        
def igual():
    num2 = float(texto["text"])
    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "sub":
        resultado = num1 - num2
    elif operacao == "mult":
        resultado = num1 * num2
    elif operacao == "div":
        if num2 == 0:
            resultado = 0
        else:
            resultado = num1 / num2
    else:
        resultado = 0
    texto.config(text=str(resultado))

def soma():
    global operacao, num1
    num1 = float(texto["text"])
    operacao = "soma"
    botao_12.config(command=Funcao_12)

def sub():
    global operacao, num1
    num1 = float(texto["text"])
    operacao = "sub"
    botao_12.config(command=Funcao_12)

def mult():
    global operacao, num1
    num1 = float(texto["text"])
    operacao = "mult"
    botao_12.config(command=Funcao_12)

def div():
    global operacao, num1
    num1 = float(texto["text"])
    operacao = "div"
    botao_12.config(command=Funcao_12)

janela = tk.Tk()
janela.geometry("300x300")
texto = tk.Label (janela, text="Seja bem-vindo a calculadora!")

texto.pack(side='top')

quadro_1 = tk.Frame(janela)
quadro_2 = tk.Frame(janela)
quadro_3 = tk.Frame(janela)
quadro_4 = tk.Frame(janela)
quadro_5 = tk.Frame(janela)

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
botao_8 = tk.Button(quadro_2, command = ponto, text='.')
botao_8.pack(side = 'top', fill='both', expand =1)

botao_9 = tk.Button(quadro_3, command = Funcao_9, text='9')
botao_9.pack(side = 'top', fill='both', expand =1)
botao_10 = tk.Button(quadro_3, command = Funcao_10, text='6')
botao_10.pack(side = 'top', fill='both', expand =1)
botao_11 = tk.Button(quadro_3, command = Funcao_11, text='3')
botao_11.pack(side = 'top', fill='both', expand =1)
botao_12 = tk.Button(quadro_3, command = igual, text='=', bg='orange')
botao_12.pack(side = 'top', fill='both', expand =1)

botao_13 = tk.Button(quadro_4, command = div, text=':', bg='orange')
botao_13.pack(side = 'top', fill='both', expand =1)
botao_14 = tk.Button(quadro_4, command = mult, text='x', bg='orange')
botao_14.pack(side = 'top', fill='both', expand =1)
botao_15 = tk.Button(quadro_4, command = sub, text='-', bg='orange')
botao_15.pack(side = 'top', fill='both', expand =1)
botao_16 = tk.Button(quadro_4, command = soma, text='+', bg='orange')
botao_16.pack(side = 'top', fill='both', expand =1)

botao_17 = tk.Button(quadro_5, command = Funcao_17, text='Apagar', bg='red', fg='white')
botao_17.pack(side = 'top', fill='both', expand =1)


quadro_1.pack(side='left', fill='both', expand=1)
quadro_2.pack(side='left', fill='both', expand=1)
quadro_3.pack(side='left', fill='both', expand=1)
quadro_4.pack(side='left', fill='both', expand=1)
quadro_5.pack(side='bottom', fill='both', expand=1)

janela.mainloop()