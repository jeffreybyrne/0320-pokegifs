import json
import requests
import os

giphy_key = os.environ.get("GIPHY_KEY")
pokemon_name = 'pikachu'

poke_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
poke_body = json.loads(poke_response.content)
print(f"The name is {poke_body['name']}")
for type in poke_body['types']:
    print(f"This pokemon has a type of {type['type']['name']}")


giphy_response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={pokemon_name}&limit=1")
giphy_body = json.loads(giphy_response.content)
gif_url = giphy_body['data'][0]['url']
print(f"The location of the gif is: {gif_url}")
