import requests
import tkinter as tk
import sqlite3

def obter_tempo():
    API_KEY = "932e77f9c6a4210d081bed7075319f95"
    cidade = entrada_cidade.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    #print(requisicao_dic)

    descricao = requisicao_dic['weather'][0]['description']
    temperatura= requisicao_dic['main']['temp'] - 273.15

    label_descricao.config(text=descricao)
    label_temperatura.config(text=f"{temperatura:.2f}ºC")

    con = sqlite3.connect("previsao_tempo.db")
    cur = con.cursor()

    try:
        cur.execute('''CREATE TABLE temp
        (descricao_temp, temperatura)''')
    except:
        print ("Tabela criada")
    finally:
        cur.execute(f"insert into temp values ('{descricao}', '{temperatura:.2f}')")
        con.commit()
        con.close()

root = tk.Tk()
root.title("Previsão do Tempo")

label_descricao = tk.Label(root, text="", font=("Helvetica", 14))
label_descricao.pack(pady=10)

label_temperatura = tk.Label(root, text="", font=("Helvetica", 18, "bold"))
label_temperatura.pack(pady=10)

entrada_cidade = tk.Entry(root, font=("Helvetica", 12))
entrada_cidade.pack(pady=10)

botao_atualizar = tk.Button(root, text="Atualizar Tempo", command=obter_tempo)
botao_atualizar.pack(pady=20)

root.mainloop()