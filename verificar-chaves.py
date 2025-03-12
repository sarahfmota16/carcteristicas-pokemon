import requests

def obter_informacoes_pokemon(pokemon_nome):
    # Criar a URL para consultar o Pokémon desejado
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_nome.lower()}"
    
    # Fazer a requisição GET para a API
    response = requests.get(url)
    
    if response.status_code == 200:
        # Converter a resposta para formato JSON (dicionário Python)
        data = response.json()
        
        # Listar todas as chaves disponíveis no dicionário 'data'
        print("Chaves disponíveis na resposta:")
        for chave in data.keys():
            print(chave)  # Imprime cada chave encontrada
        
    else:
        print(f"Erro ao acessar a API. Status code: {response.status_code}")
    
obter_informacoes_pokemon("snorlax")
