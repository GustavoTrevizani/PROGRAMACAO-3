import random
import tkinter
import sqlite3

import Time
import Registro

def janela_registro():
    global lista_times
    #janela_resposta = Registro.Registro(lista_times)
    lista_times.append (Registro.Registro(lista_times))

def grava_times():
    global lista_times
    try:
        con= sqlite3.connect("tutorial.db")
        cur = con.cursor()
    except:
        print("erro ao conectar")
    cur.execute("CREATE TABLE times(id, nome, jogadores)")
    for i in lista_times:
        cur.execute(f"""
            INSERT INTO times values
            ((i.id), "(i.nome)", "(i.jogadores)")
            """)
    con.commit()
    con.close()
    
def carrega_times():
    global lista_times
    lista_times = []

    file = open("base_de_dados.txt", 'r')
    salvo = iter(file.readlines())
    for i in salvo:
        novo_time = Time.Time(salvo, next(salvo), next(salvo))
        print(novo_time)
        lista_times.append(novo_time)
    file.close()
    
def sorteia_times():
    pass

def imprime_times():
    for i in lista_times:
        print(i.id)
        print(i.nome)
        print(i.jogadores)
        print ("\n")

if __name__=="__main__":
    global lista_times
    lista_times = []

    janela_geral = tkinter.Tk()

    label_geral = tkinter.Label (janela_geral, text="Janela inicial")
    botao_registra = tkinter.Button(janela_geral, text="Registra", command = janela_registro)
    botao_grava = tkinter.Button(janela_geral, text="Grava", command = grava_times)
    botao_carrega = tkinter.Button(janela_geral, text="Carrega", command = carrega_times)
    botao_sorteia = tkinter.Button(janela_geral, text="Sorteia", command = sorteia_times)
    botao_imprime = tkinter.Button(janela_geral, text="Imprime", command = imprime_times)


    label_geral.grid (row = 0, column = 0)
    botao_registra.grid (row=1, column = 0)
    botao_grava.grid(row=2, column=0)
    botao_carrega.grid(row=3, column=0)
    botao_sorteia.grid(row=4, column=0)
    botao_imprime.grid(row=5, column=0)

    try:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
    except:
        print("erro ao conectar")
    try:
        cur.execute("CREATE TABLE times(id, nome, jogadores)")
    except:
        print("erro ao criar")
    con.commit()
    con.close()

    janela_geral.mainloop()
