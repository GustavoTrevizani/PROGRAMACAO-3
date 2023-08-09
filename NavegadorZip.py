import tkinter 
from tkinter import filedialog
import os
import zipfile

def selecionar_arquivos():
    arquivos_selecionados = tkinter.filedialog.askopenfilenames(initialdir=entrada.get(),
                            title="Selecione os arquivos que você deseja compactar", filetypes=(("Todos os arquivos", "*.*"),))
    for arquivo in arquivos_selecionados:
        lista_dir.insert(tkinter.END, arquivo)

def compactar_arquivos():
    arquivos_selecionados = lista_dir.get(0, tkinter.END)
    arquivo_zip = filedialog.asksaveasfilename(defaultextension=".zip",
    filetypes=(("Arquivo ZIP", "*.zip"), ("Todos os arquivos", "*.*")))
    with zipfile.ZipFile(arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos_selecionados:
            rel_path = os.path.basename(arquivo)
            zipf.write(arquivo, rel_path)
        
def selecionar_pasta(arg):
    endereco = entrada.get()
    if not endereco.endswith("\\"):
        endereco += "\\"
    endereco =  endereco +  lista_dir.get(lista_dir.curselection()) + "\\"

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
botao_selecionar = tkinter.Button(janela, text="Selecionar Arquivos", command=selecionar_arquivos)
botao_compactar = tkinter.Button(janela, text="Compactar Arquivos", command=compactar_arquivos)
lista_dir = tkinter.Listbox(janela, activestyle='dotbox',selectmode=tkinter.EXTENDED)
lista_dir.bind('<<ListboxSelect>>', selecionar_pasta)

entrada.pack(fill='both', expand=1)
botao.pack(fill='both', expand=1)
botao_selecionar.pack(fill='both', expand=1)
botao_compactar.pack(fill='both', expand=1)
lista_dir.pack(fill='both', expand=1)

janela.mainloop()
