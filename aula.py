import tkinter
import os

def botao():
    endereco = cleiton.get()
    conteudo = os.lsitdir(endereco)
    for i in range(len(conteudo)):
        lista_dir.insert(i, conteudo[i])

    
janela = tkinter.Tk()

cleiton = tkinter.Entry(janela)
cleiton_telas = tkinter.Button(janela, command=botao)
lista_dir = tkinter.Listbox(janela, activestyle='dotbox',selectmode=tkinter.EXTENDED)

cleiton.pack(fill= 'both' , expand=1)
cleiton_telas.pack(fill= 'both' , expand=1)
lista_dir.pack(fill= 'both' , expand=1)

janela.mainloop()