# ENTRIES: 2- O programa possui duas Entries e devolve a soma dos dois;

import tkinter as tk

def soma():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    resultado = num1 + num2
    label_resultado.config(text=f"A soma de {num1} e {num2} é igual a: {resultado}")

janela = tk.Tk()
janela.title("Calculadora de soma")

label_instrucao1 = tk.Label(janela, text="Digite um número:")
entry1 = tk.Entry(janela)
label_instrucao2 = tk.Label(janela, text="Digite outro número:")
entry2 = tk.Entry(janela)
botao_calcular = tk.Button(janela, text="Calcular", command=soma)
label_resultado = tk.Label(janela)

label_instrucao1.pack()
entry1.pack()
label_instrucao2.pack()
entry2.pack()
botao_calcular.pack()
label_resultado.pack()

janela.mainloop()
