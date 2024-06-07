import requests
import json

url = 'https://cep.awesomeapi.com.br/json/21221460'
headers = {'Content-Type': 'application/json'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    dados = json.loads(response.text)
    print(dados)
    print(dados.get('address'))