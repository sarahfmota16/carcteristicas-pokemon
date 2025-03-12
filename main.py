import requests

# Função para obter informações de um Pokémon
def obter_informacoes_pokemon(pokemon_nome):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_nome.lower()}"  # URL da API com o nome do Pokémon e utiliza o lower para padronizar o nome e deixar em minúsculo

    response = requests.get(url) #requisitando a API

    if response.status_code == 200: #verificando se a requisição foi bem sucedida
        data = response.json() #transformando de json para python

        nome = data['name'].capitalize() #capitalize deixa a primeira letra maiuscula e as restantes minusculas
        id_pokemon = data['id']
        tipos = [tipo['type']['name'].capitalize() for tipo in data['types']]
        habilidades = [habilidade['ability']['name'].capitalize() for habilidade in data['abilities']]

        # Exibindo as informações
        print(f"\nPokémon: {nome}")
        print(f"ID: {id_pokemon}")
        print(f"Tipos: {', '.join(tipos)}")
        print(f"Habilidades: {', '.join(habilidades)}")
    else:
        print("Pokémon não encontrado. Verifique o nome e tente novamente.")

def main():
    pokemon_nome = input("Digite o nome de um Pokémon: ")
    obter_informacoes_pokemon(pokemon_nome)

if __name__ == "__main__":
    main()
