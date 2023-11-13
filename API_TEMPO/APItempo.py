import requests
import tkinter as tk
import sqlite3

def obter_tempo():
    API_KEY = "932e77f9c6a4210d081bed7075319f95"
    cidade = "riozinho"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    descricao = requisicao_dic['weather'][0]['description']
    temperatura_kelvin = requisicao_dic['main']['temp']
    temperatura_celsius = temperatura_kelvin - 273.15

    label_descricao.config(text=descricao)
    label_temperatura.config(text=f"{temperatura:.2f}ºC")

    inserir_temperatura_no_banco(temperatura_celsius)

def criar_tabela():
    conn = sqlite3.connect("temperaturas.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS temperaturas (id INTEGER PRIMARY KEY, temperatura REAL)")
    conn.commit()
    conn.close()

def inserir_temperatura_no_banco(temperatura):
    conn = sqlite3.connect("temperaturas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO temperaturas (temperatura) VALUES (?)", (temperatura,))
    conn.commit()
    conn.close()

criar_tabela()

root = tk.Tk()
root.title("Previsão do Tempo")

label_descricao = tk.Label(root, text="", font=("Helvetica", 14))
label_descricao.pack(pady=10)

label_temperatura = tk.Label(root, text="", font=("Helvetica", 18, "bold"))
label_temperatura.pack(pady=10)

botao_atualizar = tk.Button(root, text="Atualizar Tempo", command=obter_tempo)
botao_atualizar.pack(pady=20)

obter_tempo()

root.mainloop()
