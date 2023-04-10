import tkinter

def acao():
    texto.config(text="Clicou")

janela = tkinter.Tk()
texto = tkinter.Label(janela, text="Ola Tk")
botao = tkinter.Button(janela, text="Clique", command=acao)

janela.geometry("200x200")

texto.pack(side = "left")
botao.pack(side = "right")
janela.mainloop()