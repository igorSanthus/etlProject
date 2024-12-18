import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)
# data = response.json()
# print(data)
url = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1}#obter apenas os comentarios do postId=1
response = requests.get(url, params=params)
comments = response.json()

print(f"Foram encontrados {len(comments)} comentarios.")
print(f"O primeiro comentario é:{comments[0]['name']}")
print(f"Erro: {response.status_code} - {response.text}")