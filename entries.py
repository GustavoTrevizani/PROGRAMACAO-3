#Importamos o 'tkinter' como 'tk'
import tkinter as tk

#Definimos a função 'calcular_dobro'
def calcular_dobro():
    num = float(entrada.get())
    resultado = num * 2
    texto.config (text = "O dobro é: " + entrada.get())

#Criando a janela
janela = tk.Tk()

#Criando a entrada de texto
entrada = tk.Entry(janela)
entrada.pack()

#Criando o botão de calcular
botao_calcular = tk.Button(janela, command = calcular_dobro)
botao_calcular.pack()

#Criando a label de resultado
label_resultado = tk.Label(janela)
label_resultado.pack()

janela.mainloop()