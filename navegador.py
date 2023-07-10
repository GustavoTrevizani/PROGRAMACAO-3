import tkinter
import os

#transformar o que ele acha que é pasta, em arquivo de texto 

def selecionar_pasta(arg):
    endereco = entrada.get()
    if not endereco.endswith("\\"):
        endereco += "\\"
    endereco =  endereco +  lista_dir.get(lista_dir.curselection()) + "\\"

    # Adicionar barras invertidas extras onde necessário
    endereco = endereco.replace("\\\\", "\\")
        
    if os.path.isdir(endereco):  # Verifica se é um diretório
        entrada.delete(0, tkinter.END)
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
