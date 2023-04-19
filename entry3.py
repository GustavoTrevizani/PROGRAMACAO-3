# ENTRIES: 3- O programa possui duas entries, uma label e um botão. Ao se clicar no botão, o texto na label troca entre o da primeira e o da segunda Entry.

import tkinter as tk

def trocar_texto():
    texto1 = entry1.get()
    texto2 = entry2.get()
    if label["text"] == texto1:
        label.config(text=texto2)
    else: 
        label.config(text=texto1)

janela = tk.Tk()
janela.title("Troca de texto")

label_instrucao1 = tk.Label(janela, text="Digite um texto:")
entry1 = tk.Entry(janela)
label_instrucao2 = tk.Label(janela, text="Digite outro texto:")
entry2 = tk.Entry(janela)
botao_trocar = tk.Button(janela, text="Trocar", command=trocar_texto)
label = tk.Label(janela, text="Texto inicial")

label_instrucao1.pack()
entry1.pack()
label_instrucao2.pack()
entry2.pack()
botao_trocar.pack()
label.pack()

janela.mainloop()