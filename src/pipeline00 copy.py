import requests
from tinydb import TinyDB

def extract_dados_bitcoin():
    print("Extraindo dados")
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json()
    return dados

def transform_dados_bitcoin(dados):
    print("Transformando dados")
    valor = dados['data']['amount']
    cripto = dados['data']['base']
    moeda = dados['data']['currency']

    dados_transformados = {
       'valor': valor,
       'cripto': cripto,
       'moeda': moeda
    }   
    return dados_transformados

def salvar_dados_tinydb(dados,db_name="bitcoin.json"):
    print("Salvando dados no banco de dados")
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos com sucesso")  

if __name__ == "__main__":
    dados_json = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados_json)
    #salvar_dados_tinydb(dados_transformados)
    print(dados_transformados)

   