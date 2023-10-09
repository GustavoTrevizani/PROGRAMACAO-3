import random
import tkinter

import Time
import Registro

def janela_registro(lista_times):
    #janela_resposta = Registro.Registro(lista_times)
    lista_times.append (Registro.Registro(lista_times))

def imprime_times():
    print(lista_times)
    file = open("base_de_dados.txt", 'w')
    for i in lista_times:
        file.write(str(i.id))
        file.write(str(i.nome))
        time_jogadores = i.jogadores
        for j in time_jogadores:
            file.write(j)
    file.close()

if __name__=="__main__":
    janela_geral = tkinter.Tk()
    lista_times = []

    label_geral = tkinter.Label (janela_geral, text="Janela inicial")
    botao_registra = tkinter.Button(janela_geral, text="Registra", command = lambda: janela_registro(lista_times))
    botao_imprime = tkinter.Button(janela_geral, text="Imprime", command = imprime_times)

    label_geral.grid (row = 0, column = 0)
    botao_registra.grid (row=1, column = 0)
    botao_imprime.grid(row=2, column=0)

    janela_geral.mainloop()
