import requests

# link do open_weather: https://openweathermap.org/

API_KEY = "932e77f9c6a4210d081bed7075319f95"
cidade = "riozinho"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
print(requisicao_dic)
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f"{temperatura:f}ºC")
