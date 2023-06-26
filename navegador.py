import tkinter
import os

#pegar o que foi selecionado
#criar o endereço do que foi selecionado
#verificar se é uma pasta
#acessar se foi uma pasta
#senão, não faço nada

def selecionar_pasta():
    endereco = lista_dir.get(lista_dir.curselection())
    endereco = entrada.get() + endereco
    entrada.delete(0, 10000)
    entrada.insert(0, endereco)
    clique_botao()

def clique_botao():
    lista_dir.delete(0, lista_dir.size())
    endereco = entrada.get()
    try:
        conteudo = os.listdir(endereco)
    except FileNotFoundError:
        lista_dir.insert(0, "Pasta nao encontrada")
    else:
        for i in range(len(conteudo)):
            lista_dir.insert(i, conteudo[i])


janela = tkinter.Tk()

entrada = tkinter.Entry(janela)
botao = tkinter.Button(janela, command=clique_botao)
lista_dir = tkinter.Listbox(janela, activestyle='dotbox',selectmode=tkinter.EXTENDED)
lista_dir.bind('<<ListboxSelect>>', selecionar_pasta)

entrada.pack(fill='both', expand=1)
botao.pack(fill='both', expand=1)
lista_dir.pack(fill='both', expand=1)
