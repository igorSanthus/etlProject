from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

#Cria a classe Base para o SQLAlchemy
Base = declarative_base()

class BitcoinPreco(Base):
    """
    Define a tabela no banco de dados
    """
    __tablename__ = "bitcoin_precos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)#Até 50 caracteres
    moeda = Column(String(10), nullable=False)#Até 10 caracteres
    timestamp = Column(DateTime, default=datetime.now)

# def get_db_connection():
#     engine = create_engine(os.getenv("DATABASE_URL"))
#     return engine.connect()