# O programa recebe um número por uma Entry e devolve, na label, o seu dobro;

import tkinter as tk

def calcular_dobro():
    num = int(entry.get())
    resultado = num * 2
    label_resultado.config(text=f"O dobro de {num} é {resultado}")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de dobro")

# Cria os widgets
label_instrucao = tk.Label(janela, text="Digite um número:")
entry = tk.Entry(janela)
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_dobro)
label_resultado = tk.Label(janela)

# Posiciona os widgets na janela
label_instrucao.pack()
entry.pack()
botao_calcular.pack()
label_resultado.pack()

# Inicia o loop principal da janela
janela.mainloop()
