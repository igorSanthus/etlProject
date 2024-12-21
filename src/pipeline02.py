import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database import Base,BitcoinPreco
import os
from dotenv import load_dotenv

#Carrega variáveis de ambiente do arquivo .env
load_dotenv()

#Lê as variáveis de ambiente do arquivo .env (sem SSL)
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST=os.getenv("POSTGRES_HOST")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")
POSTGRES_DB=os.getenv("POSTGRES_DB")

#Cria a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#Cria a engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

#Cria a sessão de conexão com o banco de dados
Session = sessionmaker(bind=engine)

def criar_tabela():
    #Cria a tabela no banco de dados, se ela não existir
    Base.metadata.create_all(bind=engine)
    print("Tabela criada com sucesso")

def extract_dados_bitcoin():
    print("Extraindo dados")
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        print(f"Erro ao extrair dados: {response.status_code}")
        return None

def transform_dados_bitcoin(dados_json):
    print("Transformando dados")
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now()

    dados_transformados = {
       'valor': valor,
       'criptomoeda': criptomoeda,
       'moeda': moeda,
       'timestamp': timestamp
    }   
    return dados_transformados

# def salvar_dados_tinydb(dados,db_name="bitcoin.json"):
#     print("Salvando dados no banco de dados")
#     db = TinyDB(db_name)
#     db.insert(dados)
#     print("Dados salvos com sucesso")  

def salvar_dados_postgres(dados):
    print("Salvando dados no banco de dados")
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL") 

if __name__ == "__main__":
    criar_tabela()
    print("Iniciando ETL com atualização a cada 15 segundos(CTRL+C para parar)")

    while True:
        try:
            dados_json = extract_dados_bitcoin()
            if dados_json:
                dados_transformados = transform_dados_bitcoin(dados_json)
                print("Dados transformados",dados_transformados)
                salvar_dados_postgres(dados_transformados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("ETL interrompido pelo usuário")
            break
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(15)
    #print(dados_transformados)
   