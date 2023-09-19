import requests

url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Salvar o conteúdo em um arquivo local
    with open('anatel_bandalarga_capitais.csv', 'wb') as file:
        file.write(response.content)
    print("Arquivo salvo com sucesso!")
else:
    print("Não foi possível baixar o arquivo.")
