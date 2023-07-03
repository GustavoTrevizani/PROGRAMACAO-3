import tkinter
import os

#transformar o que ele acha que é pasta, em arquivo de texto
#quando apagar uma barra, ele tem que adicionar outra 

def selecionar_pasta(arg):
    endereco = lista_dir.get(lista_dir.curselection())
    endereco = entrada.get() + endereco + "\\"

    # Adicionar barras invertidas extras onde necessário
    endereco = endereco.replace("\\\\", "\\")
    if not endereco.endswith("\\"):
        endereco += "\\"
        
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
            #if os.path.isdir(os.path.join(endereco, conteudo[i])):
                #conteudo[i] += ".txt"
            lista_dir.insert(i, conteudo[i])


janela = tkinter.Tk()

entrada = tkinter.Entry(janela)
botao = tkinter.Button(janela, command=clique_botao)
lista_dir = tkinter.Listbox(janela, activestyle='dotbox',selectmode=tkinter.EXTENDED)
lista_dir.bind('<<ListboxSelect>>', selecionar_pasta)

entrada.pack(fill='both', expand=1)
botao.pack(fill='both', expand=1)
lista_dir.pack(fill='both', expand=1)
