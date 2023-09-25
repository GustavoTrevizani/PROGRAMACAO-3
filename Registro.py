import tkinter
import Time
import random

class Registro:

    def __init__(self, lista_times):
        self.janela = tkinter.Tk()

        self.label_desc_janela = tkinter.Label(self.janela, text = "Janela de inscrição")
        self.label_desc_nome = tkinter.Label(self.janela, text = "Nome do Time")
        self.label_desc_time = tkinter.Label(self.janela, text = "Lista de Jogadores")

        self.entry_nome_time = tkinter.Entry(self.janela )
        self.lista_jogadores =tkinter.Listbox(self.janela)
        self.botao_ok = tkinter.Button(self.janela, text = "Ok", command = lambda: self.finaliza(lista_times))

        #teste de cadastro de jogadores
        self.entry_nome_jogador = tkinter.Entry(self.janela)
        self.botao_cadastra_jogador = tkinter.Button(self.janela, command = self.registra_jogador)
        #teste de cadastro de jogadores

        self.botao_apaga_lista = tkinter.Button(self.janela, text="Apagar Lista", command = self.apaga_lista)

        self.label_desc_janela.grid(row=0, column =0)

        self.label_desc_nome.grid(row=1, column =0)
        self.entry_nome_time.grid (row=1, column=1)


        self.label_desc_time.grid(row=2, column =0)
        self.lista_jogadores.grid(row=2, column=1)

        self.botao_ok.grid(row=3, column =1)

        self.entry_nome_jogador.grid(row=4, column=0)
        self.botao_cadastra_jogador.grid (row=4, column=1)

        self.botao_apaga_lista.grid(row=5, column=1)

        self.janela.mainloop()

    
    def registra_jogador(self):
        nome = self.entry_nome_jogador.get()
        if not nome == "": 
            self.lista_jogadores.insert(tkinter.END, nome)
        self.entry_nome_jogador.delete(0,tkinter.END)
        #Para implementar: Teste se o  jogador já está no time

    def apaga_lista(self):
        self.lista_jogadores.delete(0, tkinter.END)


    def finaliza(self, lista_times):
        #Para implementar: Modificar o numero do time
        #resposta
        resposta = Time.Time(1, self.entry_nome_time.get(), self.lista_jogadores.get(0, tkinter.END))
    
        lista_times.append(resposta)
        self.janela.destroy()
   
