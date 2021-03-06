import random
import requests
import json
from django.http import JsonResponse
import os

giphy_key = os.environ.get("GIPHY_KEY")


def find_gif(name):
    giphy_response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={name}")
    if giphy_response.status_code == 403:
        return ''
    else:
        giphy_body = json.loads(giphy_response.content)
        if len(giphy_body['data']) == 0:
            return ''
        else:
            rand_num = random.randint(0, len(giphy_body['data'])-1)
            return giphy_body['data'][rand_num]['url']


def pokemon(request, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    res = requests.get(api_url)
    if res.status_code == 404:
        return JsonResponse({'error': f'pokemon {id} not found'})
    else:
        body = json.loads(res.content)
        name = body["name"]
        types = []
        for type in body['types']:
            types.append(type['type']['name'])
        gif_url = find_gif(name)
        return JsonResponse({'id': id, 'name': name, 'types': types, 'gif': gif_url})


def team(request):
    list_of_pokemon = []
    for num in range(1, 7):
        id = random.randint(1, 807)
        api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
        res = requests.get(api_url)
        body = json.loads(res.content)
        name = body["name"]
        types = []
        for type in body['types']:
            types.append(type['type']['name'])
        gif_url = find_gif(name)
        pokemon = {'id': id, 'name': name, 'types': types, 'gif': gif_url}
        # print(pokemon)
        list_of_pokemon.append(pokemon)
        value = {'team': list_of_pokemon}
    return JsonResponse(value)
