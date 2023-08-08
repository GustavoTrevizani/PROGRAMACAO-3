import tkinter as tk
from tkinter import filedialog
import os
import zipfile

def selecionar_arquivos():
    arquivos_selecionados = filedialog.askopenfilenames(initialdir= endereco_atual.get() ,title="Selecione os arquivos para compactar",
    filetypes=(("Todos os arquivos", "*.*"),))
    lista_arquivos.delete(0, tk.END)
    for arquivo in arquivos_selecionados:
        lista_arquivos.insert(tk.END, arquivo)

def compactar_arquivos():
    arquivos_selecionados = lista_arquivos.get(0, tk.END)
    arquivo_zip = filedialog.asksaveasfilename(defaultextension=".zip",
    filetypes=(("Arquivo ZIP", "*.zip"), ("Todos os arquivos", "*.*")))
    with zipfile.ZipFile(arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos_selecionados:
            rel_path = os.path.basename(arquivo)
            zipf.write(arquivo, rel_path)

def abrir_pasta():
        os.startfile(endereco_atual.get())

def selecionar_pasta(event):
    selection = lista_dir.curselection()
    if selection:
        folder_name = lista_dir.get(selection)
        endereco_atual.set(os.path.join(endereco_atual.get(), folder_name))
        atualizar_lista()

def atualizar_lista():
    lista_dir.delete(0, tk.END)
    try:
        conteudo = os.listdir(endereco_atual.get())
        for item in conteudo:
            lista_dir.insert(tk.END, item)
    except FileNotFoundError:
        lista_dir.insert(tk.END, "Pasta não encontrada")

def clique_botao():
    endereco_atual.set(entrada.get())
    atualizar_lista()

# Cria a janela principal
janela = tk.Tk()
janela.title("Compactador de Arquivos")

# Botão para selecionar os arquivos a serem compactados
botao_selecionar = tk.Button(janela, text="Selecionar Arquivos", command=selecionar_arquivos)
botao_selecionar.pack(fill='both', expand=1)

# Botão para compactar os arquivos selecionados
botao_compactar = tk.Button(janela, text="Compactar Arquivos", command=compactar_arquivos)
botao_compactar.pack(fill='both', expand=1)

# Lista para exibir os arquivos selecionados
lista_arquivos = tk.Listbox(janela, activestyle='dotbox', selectmode=tk.EXTENDED)
lista_arquivos.pack(fill='both', expand=1)



# Variável para armazenar o endereço atual
endereco_atual = tk.StringVar()

# Entrada de texto para o endereço
entrada = tk.Entry(janela, textvariable=endereco_atual)
entrada.pack(fill='both', expand=1)

# Botão para atualizar a lista de conteúdos da pasta
botao = tk.Button(janela, text="Atualizar", command=clique_botao)
botao.pack(fill='both', expand=1)
botao = tk.Button(janela, text="Abrir Pasta Atual", command=abrir_pasta)
botao.pack(fill='both', expand=1)

lista_dir = tk.Listbox(janela, activestyle='dotbox', selectmode=tk.EXTENDED)
lista_dir.bind('<<ListboxSelect>>', selecionar_pasta)
lista_dir.pack(fill='both', expand=1)

# Executa o loop principal do Tkinter
janela.mainloop()
