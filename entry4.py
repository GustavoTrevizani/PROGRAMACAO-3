# ENTRIES: 4- Faça um programa que retorna o número de fibonacci escrito na Entry.

import tkinter as tk

def calcular_fibonacci():
    num = int(entry.get())

    if num <= 0:
        resultado = 0
    elif num == 1:
        resultado = 1
    else:
        a = 0
        b = 1
        for i in range(num-1):
            c = a + b
            a = b
            b = c
        resultado = b

    label_resultado.config(text=f"O número de Fibonacci de {num} é {resultado}")

janela = tk.Tk()
janela.title("Calculadora de Fibonacci")

label_instrucao = tk.Label(janela, text="Digite um número:")
entry = tk.Entry(janela)
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_fibonacci)
label_resultado = tk.Label(janela)

label_instrucao.pack()
entry.pack()
botao_calcular.pack()
label_resultado.pack()

janela.mainloop()