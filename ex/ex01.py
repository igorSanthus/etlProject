import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response.headers)
#GET: Pegar dados da internet(select * from tabela) 
#POST: Enviar dados para a internet(insert into tabela)
#PUT: Atualizar dados da internet(update tabela set coluna = valor where id = 1)
#DELETE: Deletar dados da internet(delete from tabela where id = 1)
